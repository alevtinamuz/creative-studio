import './assets/main.css';
import { createApp } from 'vue';
import { createPinia } from 'pinia';
import App from './App.vue';
import router from './router';
import axios from 'axios';
// import { io } from 'socket.io-client';
// import VueSocketIO from 'vue-socket.io';

const app = createApp(App);

axios.defaults.baseURL = 'http://127.0.0.1:8000';

app.use(createPinia());
app.use(router, axios);

// const socket = io('ws://localhost:8000'); // Создаем экземпляр сокета

// app.use(VueSocketIO, socket);

app.mount('#app');
