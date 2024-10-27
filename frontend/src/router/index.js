import { createRouter, createWebHistory } from 'vue-router'
import store from '@/store'; 
import HomeView from '../views/Homeview.vue'

import LoginView from '../views/LoginView.vue'

import SponsorRegister from '@/views/SponsorRegister.vue'

import InfluencerRegister from '@/views/InfluencerRegister.vue';
import SponsorDashboard from '@/views/Sponsor/SponsorDashboard.vue';
import CreateCampaign from '@/views/Sponsor/CreateCampaign.vue';

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
      name: 'signin' ,
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

    },
    {
      path:'/dashboardSponsor',
      name:'sponsorDashboard',
      component:SponsorDashboard,
      children:[
        {
          path: "createCampaign",
          name: "createCampaign",
          component:CreateCampaign
        },
      ]
    }
    
  ]
})


router.beforeEach((to , from , next ) =>{
  const roles=store.getters.getRoles;
  const token=store.getters.getToken;
  console.log("Roles:", roles);
  console.log("Token:", token);


  if(!roles.includes("admin") && to.fullPath.startsWith("/admin")){
    return next('/');
  }
  if(!token && ((to.fullPath.startsWith("/adminDashboard")) ||(to.fullPath.startsWith("/influencerDashboard")) ||(to.fullPath.startsWith("/sponsorDashboard")) )){
    return  next('/');
  }
  if(!roles.includes("influencer") && to.fullPath.startsWith("/influencerDashboard")){
    return  next('/');
  }
  if(!roles.includes("sponsor") && to.fullPath.startsWith("/sponsorDashboard")){
    return  next('/');
  }
  if(to.fullPath.startsWith("signout")){
    return  next('/');
  }
  next()
});


export default router
