<script setup>
import { RouterView } from "vue-router";
import store from '@/store';

</script>
<template>
    <div class="container-xxl  ">
           <div class="card mx-auto" style="width: 80rem;">
               <div class="card-body">
                   <h5 class="card-title">Campaigns</h5>
   
   <table class="table  table-striped-columns " >
       <thead>
       <tr class="table-info">
         <th scope="col">id</th>
         <th scope="col">campaignName</th>
         <th scope="col">visibility</th>
         <th scope="col">budget</th>
         <th scope="col">niche</th>
         <th scope="col">goals</th>
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
       </tr>
     </tbody>
   </table>
   
   
   
   </div>
           </div>
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