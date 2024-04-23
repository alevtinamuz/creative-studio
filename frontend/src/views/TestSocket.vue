<!-- OnlinePresenceIndicator.vue -->
<template>
    <div>
      <section>
        <div>
          <div>
  
            <h1 class="title">Online Presence Indicator</h1>
            <div><span class="">{{ onlineUsersCount }}</span> users online</div>
            <!-- <ul>
              <li v-for="message in messages" :key="message">{{ message }}</li>
            </ul> -->
            <div>{{ messages }}</div>
          </div>
          <div class="column">
            <div class="box">
              <h1 class="title">Online Users</h1>
              <ul>
                <li class="on-us" v-for="user in onlineUsers" :key="user">{{ user }}</li>
              </ul>
            </div>
          </div>
        </div>
      </section>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
          isAuthenticated: false,
          user: '',
          onlineUsersCount: 0,
          messages: [],
          onlineUsers: []
      };
    },
    mounted() {
      const ws = new WebSocket('ws://localhost:8000/ws/');
      ws.onmessage = (event) => {
        const data = JSON.parse(event.data);
        this.onlineUsersCount = data.online;
        this.messages = data.msg;
        this.onlineUsers = data.users;
        console.log(this.messages)
      };
    }
  };
  </script>
  
  <style>
  /* Add your CSS styles here */
  </style>
  