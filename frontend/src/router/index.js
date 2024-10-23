import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/Homeview.vue'

import LoginView from '../views/LoginView.vue'

import SponsorRegister from '@/views/SponsorRegister.vue'

import InfluencerRegister from '@/views/InfluencerRegister.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'homeView',
      component: HomeView
    },
    {
      path: '/signin' ,
      name: 'loginView' ,
      component: LoginView
    },
    {
      path: '/sponsorRegister' ,
      name: 'sponsorRegister' ,
      component: SponsorRegister
    },
    {
      path: '/influencerRegister' ,
      name: 'influencerRegister' ,
      component: InfluencerRegister

    }
    
  ]
})

export default router
