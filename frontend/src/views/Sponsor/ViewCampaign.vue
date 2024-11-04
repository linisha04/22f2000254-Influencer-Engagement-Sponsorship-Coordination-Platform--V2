<script setup>
import NavSponsor from '@/components/Sponsor/NavSponsor.vue';
import store from '@/store';
import router from "@/router";
import { RouterView } from "vue-router";



</script>

<template>
 <div class="container mt-5">
        <div class="card mx-auto" style="width: 80rem;">
            <div class="card-body">
                <h5 class="card-title">Campaigns</h5>

<table class="table table-dark table-striped-columns " >
    <thead>
    <tr>
      <th scope="col">id</th>
      <th scope="col">campaignName</th>
      <th scope="col">visibility</th>
      <th scope="col">budget</th>
      <th scope="col">niche</th>
      <th scope="col">goals</th>
    </tr>
  </thead>
  <tbody>
    <tr v-for="camp in userCamps" :key="camp.id">
        <!-- <th scope="row">{{ camp.id }}</th> -->
      <td>{{ camp['id'] }}</td>
      <td>{{ camp['campaignName'] }}</td>
      <td>{{ camp['visibility'] }}</td>
      <td>{{ camp['budget'] }}</td>
      <td>{{ camp['niche'] }}</td>
      <td>{{ camp['goals'] }}</td>
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
            userCamps:null
        }
    },
    methods:{
        userCampaigns(){
            fetch(import.meta.env.VITE_BASEURL+"/viewCampaign",{
                method:'GET',
                headers:{
                    "Content-Type": "application/json",
                    "Authentication-Token": store.getters.getToken

                },

            }).then((x=>{
                return x.json()
            })) .then(data => {
                console.log("Fetched campaigns:", data);
               
        this.userCamps = data;
       
      })
        }
    },
    mounted() {

    this.userCampaigns();
  }
  

    
}



</script>   

<style>

</style>