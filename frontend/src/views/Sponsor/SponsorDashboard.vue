<script setup>
import NavSponsor from '@/components/Sponsor/NavSponsor.vue';
import { RouterView } from "vue-router";
import { ref } from 'vue';

import CreateCampaign from './CreateCampaign.vue';
import router from '@/router';
import { RouterLink } from 'vue-router';
import store from '@/store';
import { onMounted } from 'vue';
</script>
<template>
   

<NavSponsor/>

<RouterView/>


  <div class="card" style="width: 56rem ;">
  <img src="/Users/linisha/Documents/MAD2/frontend/src/assets/Home Page.png" class="card-img-top" alt="Image">
 
   
  <div v-if="userInfo">
  <ul class="list-group list-group-flush">


    <li class="list-group-item"><b>Name : </b> {{ userInfo.username }}      </li>
    <li class="list-group-item"><b>Your ID : </b>    {{ userInfo.id}}                      </li>
    <li class="list-group-item"><b>Your Email : </b>    {{ userInfo.email}}                      </li>
    <li class="list-group-item"><b>Your Industry Name : </b>   {{ userInfo.name }}                  </li>
    <li class="list-group-item"><b>Industry : </b>          {{ userInfo.industry }}                        </li>
    <li class="list-group-item"><b>Your Budget : </b>            {{ userInfo.budget }}                   </li>
  </ul>
</div>
<div v-else> Loading... </div>
</div>



</template>

<script>
 export default {
  data() {
    return {
      userInfo: null
    };
  },

  methods: {
    sponsorInfo() {
      fetch(import.meta.env.VITE_BASEURL + "/userInfo", {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
                        'Authentication-Token': store.getters.getToken
        },
      })
      .then(x => {
        return x.json()
      })
      .then(data => {
        this.userInfo = data;
      })
      .catch(error => {
        console.error('Failed to fetch user info:', error)
      });
    }
  },
  mounted() {
    this.sponsorInfo();
  }
  

 
 }
</script>

<style scoped>

</style>