import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import SignUpView from '../views/SignUpView.vue'
import LoginView from '../views/LoginView.vue'
import FeedView from '../views/FeedView.vue'
import SearchFriendsView from '../views/SearchFriendsView.vue'
import SearchCanvasesView from '../views/SearchCanvasesView.vue'
import CanvasView from '../views/CanvasView.vue'


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
      path: '/feed',
      name: 'feed',
      component: FeedView,
    },
    {
      path: '/searchfriends',
      name: 'searchfriends',
      component: SearchFriendsView,
    },
    {
      path: '/searchcanvases',
      name: 'searchcanvases',
      component: SearchCanvasesView,
    },
    ,
    {
      path: '/canvas',
      name: 'canvas',
      component: CanvasView,
    },
  ]
})

export default router
