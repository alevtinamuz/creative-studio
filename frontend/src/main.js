import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import axios from 'axios'

const app = createApp(App)

// const socket = new Sock('http://127.0.0.1:8000'); // Замените localhost:8080 на URL вашего сервера

// app.config.globalProperties.$socket = socket;

axios.defaults.baseURL = 'http://127.0.0.1:8000'

app.use(createPinia())
app.use(router, axios)

app.mount('#app')
