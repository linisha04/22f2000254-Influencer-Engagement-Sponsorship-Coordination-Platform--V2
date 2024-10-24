import { createRouter, createWebHistory } from 'vue-router'
import store from '@/store'; 
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


router.beforeEach((to , from , next ) =>{
  if(!store.getters.getRoles.includes("admin") && to.fullPath.startsWith("/admin")){
    return router.push("/")
  }
  if(!store.getters.getToken && ((to.fullPath.startsWith("/adminDashboard")) ||(to.fullPath.startsWith("/influencerDashboard")) ||(to.fullPath.startsWith("/sponsorDashboard")) )){
    return router.push("/")
  }
  if(!store.getters.getRoles.includes("infuencer") && to.fullPath.startsWith("/influencerDashboard")){
    return router.push("/")
  }
  if(!store.getters.getRoles.includes("sponsor") && to.fullPath.startsWith("/sponsorDashboard")){
    return router.push("/")
  }
  next()
});


export default router
