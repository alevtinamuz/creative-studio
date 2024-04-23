import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import SignUpView from '../views/SignUpView.vue'
import LoginView from '../views/LoginView.vue'
import FeedView from '../views/FeedView.vue'
import SearchFriendsView from '../views/SearchFriendsView.vue'
import SearchCanvasesView from '../views/SearchCanvasesView.vue'
import CreateCanvasView from '../views/CreateCanvasView.vue'
import EditCanvasView from '@/views/EditCanvasView.vue'
import TestSocket from '@/views/TestSocket.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignUpView,
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView,
    },
    {
      path: '/profile',
      name: 'feed',
      component: FeedView,
    },
    {
      path: '/search_friends',
      name: 'search_friends',
      component: SearchFriendsView,
    },
    {
      path: '/search_canvases',
      name: 'search_canvases',
      component: SearchCanvasesView,
    },
    ,
    {
      path: '/create_canvas',
      name: 'create_canvas',
      component: CreateCanvasView,
    },
    {
      // path: '/edit_canvas',
      path: '/edit_canvas/:id',
      name: 'edit_canvas',
      component: EditCanvasView,
    },
    {
      path: '/test',
      name: 'test',
      component: TestSocket,
    },
  ]
})

export default router
