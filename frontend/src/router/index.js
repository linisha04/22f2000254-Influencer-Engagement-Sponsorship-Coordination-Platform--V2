import { createRouter, createWebHistory } from 'vue-router'
import store from '@/store'; 
import HomeView from '../views/Homeview.vue'
import LoginView from '../views/LoginView.vue'

import SponsorRegister from '@/views/SponsorRegister.vue'
import InfluencerRegister from '@/views/InfluencerRegister.vue';

import CreateAdRequest from '@/views/createAdRequest.vue';
import ViewAdRequests from '@/views/ViewAdRequests.vue';
import UpdateAdRequest from '@/views/UpdateAdRequest.vue';
import SearchView from '@/views/SearchView.vue';

import SponsorDashboard from '@/views/Sponsor/SponsorDashboard.vue';
import CreateCampaign from '@/views/Sponsor/CreateCampaign.vue';
import SponsorView from '@/views/Sponsor/SponsorView.vue';
import ViewCampaign from '@/views/Sponsor/ViewCampaign.vue';
import UpdateCampaign from '@/views/Sponsor/UpdateCampaign.vue';

import InfluencerView from '@/views/Influencer/InfluencerView.vue';
import DashboardInfluencer from '@/views/Influencer/DashboardInfluencer.vue';
import CampaignsPublic from '@/views/Influencer/CampaignsPublic.vue'


import AdminView from '@/views/admin/AdminView.vue';
import AdminDashboard from '@/views/admin/AdminDashboard.vue';
import AllCampaigns from '@/views/admin/AllCampaigns.vue';
import FlagUsers from '@/views/admin/FlagUsers.vue';
import AllAds from '@/views/admin/AllAds.vue';


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
      path:'/createAdRequest/campaign_id/:id',
      name:'CreateAdRequest',
      component:CreateAdRequest,
      meta: {  requiresAuth: true},
      props: true
    },
    {
      path:'/viewAdRequests/campaign_id/:id',
      name:'ViewAdRequests',
      component:ViewAdRequests,
      meta: {  requiresAuth: true},
      props: true
    },
    {

      path:'/updateAdRequests/AdID/:id',
      name:'UpdateAdRequests',
      component:UpdateAdRequest,
      meta:{requiresAuth: true},
      props:true

    },
    {
     path:'/search/keyword/:word',
     name:'SearchView',
     component:SearchView,
     meta:{  requiresAuth: true},
     props:true
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
        },
        {
          path:'updateCampaign/:id',
          name:'updateCampaign',
          component:UpdateCampaign,
          meta: {  requiresAuth: true,roleRequired: 'sponsor' },
          props:true


        }
      ]
    },
    {
      path:'/influencerView',
      name:'InfluencerView',
      component:InfluencerView,
      meta: {  requiresAuth: true,roleRequired: 'influencer' },
      children:[
        {
          path:"dashboardInfluencer",
          name:"influencerDashboard",
          component:DashboardInfluencer,
          meta: {  requiresAuth: true,roleRequired: 'influencer' },

        },
        {
          path:"campaignsPublic",
          name:"CampaignsPublic",
          component:CampaignsPublic,
          meta: {  requiresAuth: true,roleRequired: 'influencer' },
      },

      ]
    },
    {
      path:'/adminView',
      name:'AdminView',
      component:AdminView,
      meta: {  requiresAuth: true,roleRequired: 'admin' },
      children:[
        {
          path:'adminDashboard',
          name:'AdminDashboard',
          component:AdminDashboard,
          meta: {  requiresAuth: true,roleRequired: 'admin' }
        },
        {
          path:'allCampaigns',
          name:'AllCampaigns',
          component:AllCampaigns,
          meta:{requiresAuth:true , roleRequired:'admin'}
        },
        {
          path:'flagUsers',
          name:'FlagUsers',
          component:FlagUsers,
          meta:{requiresAuth:true , roleRequired:'admin'}
        },
        {
          path:'allAds',
          name:'AllAds',
          component:AllAds,
          meta:{requiresAuth:true , roleRequired:'admin'}
        }
        
      ]

    }
    
  ]

})


router.beforeEach((to, from, next) => {
  const roles = store.getters.getRoles;
  const token = store.getters.getToken;
 
 
  console.log("Roles:", roles);
  console.log("Token:", token);
  
  
  if(!store.getters.getRoles.includes("admin") && to.fullPath.startsWith("/adminView")){
    return next("/");
  }
  if(!store.getters.getToken && (to.fullPath.startsWith("/admin") || to.fullPath.startsWith("/influencerView")||to.fullPath.startsWith("/sponsorView"))){
    return next("/");
  }
  if(!store.getters.getRoles.includes("influencer") && to.fullPath.startsWith("/influencerView")){
    return next("/");
  }
  if(!store.getters.getRoles.includes("sponsor") && to.fullPath.startsWith("/sponsorView")){
    return next("/");
  }
  next();

   

});

export default router;















