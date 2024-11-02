import { createRouter, createWebHistory } from 'vue-router'
import store from '@/store'; 
import HomeView from '../views/Homeview.vue'
import LoginView from '../views/LoginView.vue'

import SponsorRegister from '@/views/SponsorRegister.vue'
import InfluencerRegister from '@/views/InfluencerRegister.vue';


import SponsorDashboard from '@/views/Sponsor/SponsorDashboard.vue';
import CreateCampaign from '@/views/Sponsor/CreateCampaign.vue';
import SponsorView from '@/views/Sponsor/SponsorView.vue';
import ViewCampaign from '@/views/Sponsor/ViewCampaign.vue';


import DashboardInfluencer from '@/views/Influencer/DashboardInfluencer.vue';
import CampaignsPublic from '@/views/Influencer/CampaignsPublic.vue';



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
      path:'/sponsorView',
      name:'SponsorView',
      component:SponsorView,
      meta: {  requiresAuth: true,roleRequired: 'sponsor' },
      children:[
        {
          path: "createCampaign",
          name: "createCampaign",
          component:CreateCampaign,
          meta: {  requiresAuth: true,roleRequired: 'sponsor' ,showcard:false},
        
        },
        {
          path:'dashboardSponsor',
          name:'sponsorDashboard',
          component:SponsorDashboard,
          meta: {  requiresAuth: true,roleRequired: 'sponsor' },
        },
        {
          path:'viewCampaign',
          name:'ViewCampaign',
          component:ViewCampaign,
          meta: {  requiresAuth: true,roleRequired: 'sponsor' },
        }
      ]
    },
    {
      path:'/dashboardInfluencer',
      name:'DashboardInfluencer',
      component:DashboardInfluencer,
      children:[
        {
          path:"campaignsPublic",
          name:"campaignsPublic",
          component:CampaignsPublic
      },

      ]
    }
    
  ]

})


router.beforeEach((to, from, next) => {
  const roles = store.getters.getRoles;
  const token = store.getters.getToken;
 
 
  console.log("Roles:", roles);
  console.log("Token:", token);
  
  


  if (to.matched.some(record => record.meta.requiresAuth && !token)) {
    next('/signin');
  } else {
    const requiredRole = to.matched.find(record => record.meta.roleRequired)?.meta.roleRequired;
    if (requiredRole && !roles.includes(requiredRole)) {
      next('/'); // Redirect to home or an unauthorized page
    } else {
      next();
    }
  }

    if(to.fullPath.startsWith("signout")){
    store.commit("setUser", {token: null, roles: []});
    console.log("logged out")
  next('/');
  }
 

});

export default router;

// router.beforeEach((to , from , next ) =>{
//   const roles=store.getters.getRoles;
//   const token=store.getters.getToken;
//   console.log("Roles:", roles);
//   console.log("Token:", token);

//   if (to.matched.some(record => record.meta.requiresAuth && !token)) {
//     return next('/');
//   }
//   if (to.matched.some(record => record.meta.roleRequired && !roles.includes(record.meta.roleRequired))) {
//     return next('/');
//   }

//   if(!roles.includes("influencer") && to.name=="DashboardInfluencer"){
//     return  next('/');
//   }
//   if(!roles.includes("sponsor") && to.name==("sponsorDashboard")){
//     return  next('/');
//   }
//   if(to.fullPath.startsWith("signout")){
//     store.commit("setUser", {token: null, roles: []});
//   next('/');
//   }
//   next()
// });


// export default router




















  // if(!roles.includes("admin") && to.fullPath.startsWith("/admin")){
  //   return next('/');
  // }
  // if(!token && ((to.name ==("adminDashboard")) ||(to.fullPath.startsWith("/influencerDashboard")) ||(to.fullPath.startsWith("/sponsorDashboard")) )){
  //   return  next('/');
  // }