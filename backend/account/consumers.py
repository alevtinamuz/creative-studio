import json

from channels.generic.websocket import WebsocketConsumer


class Consumer(WebsocketConsumer):

    connections = []
    users = []

    def update_indicator(self, msg):
        for connection in self.connections:
            connection.send(
                text_data=json.dumps(
                    {
                        "msg": f"{self.user} {msg}",
                        "online": f"{len(self.connections)}",
                        "users": [user for user in self.users],                        
                    }
                )
            )
        self.update_all_clients()

    def connect(self):
       self.accept()
       self.user = None
       self.update_all_clients()


    def disconnect(self, code):
        self.update_indicator(msg="Disconnected")
        self.connections.remove(self)
        self.users.remove(self.user)
        self.update_all_clients()
        return super().disconnect(code)

    

    def receive(self, text_data):
        data = json.loads(text_data)
        if data.get('type') == 'user_info':
           self.user = data['user']
           self.connections.append(self)
           self.users.append(data['user'])
           self.update_indicator(msg="Connected")
           self.update_all_clients()
        elif data.get('type') == 'user_out':
            self.connections.remove(self)
            self.users.remove(data['user'])
            self.update_indicator(msg="Disconnected")
            self.update_all_clients()
        elif data.get('type') == 'draw':
            self.update_all_clients()


    def close(self, code=None, reason=None):
        self.connections.remove(self)
        self.users.remove(self.user)
        self.update_indicator(msg="Disconnected")
        self.update_all_clients()
        super().close(code, reason)

    def update_all_clients(self):
        for connection in self.connections:
            text_data = json.dumps({
                "msg": f"User joined or left.",
                "online": len(self.connections),
                "users": [user for user in self.users],
            })
            connection.send(text_data)

    