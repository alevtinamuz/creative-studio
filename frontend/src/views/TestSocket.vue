<template>
    <div>
      <section>
        <div>
          <h1>Online Presence Indicator</h1>
          <div>
            <span class="">{{ onlineUsersCount }}</span> users online
          </div>
        </div>
        <div>
          <h1>Online Users</h1>
          <ul>
            <li v-for="user in onlineUsers" :key="user">{{ user.name }}</li>
          </ul>
        </div>
      </section>
    </div>
  </template>
  
  <script>
  import { ref, onBeforeUnmount } from 'vue'
  
  export default {
    data() {
      return {
        isAuthenticated: false,
        user: '',
        onlineUsersCount: 0,
        messages: [],
        onlineUsers: [],
      };
    },
    mounted() {
      const socket = ref(null) // Создаем реактивный объект для хранения ссылки на WebSocket
  
      // Открываем соединение WebSocket
      socket.value = new WebSocket('ws://localhost:8000/ws/');
  
      // Обработчик события открытия соединения
      socket.value.onopen = () => {
        const user = { id: sessionStorage.getItem('user.id'), name: sessionStorage.getItem('user.name') };
        socket.value.send(JSON.stringify({ type: 'user_info', user: user }));
      };
  
      // Обработчик события закрытия соединения
      socket.value.onclose = () => {
        const user = { id: sessionStorage.getItem('user.id'), name: sessionStorage.getItem('user.name') };
        socket.value.send(JSON.stringify({ type: 'user_out', user: user }));
      };
  
      // Обработчик события получения сообщения
      socket.value.onmessage = (event) => {
        const data = JSON.parse(event.data);
        this.onlineUsers = data.users.map((user) => user = JSON.stringify(user));
        this.onlineUsers = Array.from(new Set(this.onlineUsers));
        this.onlineUsers = this.onlineUsers.map((user) => user = JSON.parse(user));
        this.onlineUsersCount = this.onlineUsers.length
      };
  
      // Обработчик жизненного цикла beforeUnmount
      onBeforeUnmount(() => {
        if (socket.value) {
          socket.value.close()
        }
      })
    },
  };
  </script>
  