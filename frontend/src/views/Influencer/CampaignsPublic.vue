<script setup>
import { RouterView } from "vue-router";
import store from '@/store';
import router from "@/router";


</script>
<template>
  
    <div class="container-xxl  ">
           
   <table class="table  table-striped-columns fixed-top " >
       <thead>
       <tr class="table-info">
         <th scope="col">id</th>
         <th scope="col">campaignName</th>
         <th scope="col">visibility</th>
         <th scope="col">budget</th>
         <th scope="col">niche</th>
         <th scope="col">goals</th>
         <th scope="col">Create Ad req <button type="button" @click="router.push({name:'influencerDashboard'})">Dashboard</button></th>
       </tr>
     </thead>
     <tbody>
       <tr v-for="camp in userCamps" :key="camp.id" class="table-success">
         <!-- <th scope="row">1</th> -->
         <td>{{ camp.id }}</td>
         <td>{{ camp.campaignName }}</td>
         <td>{{ camp.visibility }}</td>
         <td>{{ camp.budget }}</td>
         <td>{{ camp.niche }}</td>
  
         <td>{{ camp.goals }}</td>
         <td class="table-primary">
          <button  @click="router.push(`/createAdRequest/campaign_id/${camp.id}`)" >Create Ad Requests</button>
          <button  @click="router.push(`/viewAdRequests/campaign_id/${camp.id}`)" >view Ad Requests</button>
        
        </td>

       </tr>
     </tbody>
   </table>
   
   
   
  
         
       </div>
</template>

<script>


export default {
    data(){
        return {
            userCamps:[]
        }
    },
    methods:{
        userCampaigns(){
            fetch(import.meta.env.VITE_BASEURL+"/campaignsPublic",{
                method:'GET',
                headers:{
                    "Content-Type": "application/json",
                    "Authentication-Token": store.getters.getToken

                },

            }).then((x=>{
                return x.json()
            })) .then(data => {
               
        this.userCamps = data;
       
      })
        }
    },
    mounted() {

    this.userCampaigns();
  }
  

    
}




</script>