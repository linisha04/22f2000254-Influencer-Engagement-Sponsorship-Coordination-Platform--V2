<script setup>
import NavSponsor from '@/components/Sponsor/NavSponsor.vue';
import { RouterView } from "vue-router";
import { ref } from 'vue';
import router from '@/router';
import store from '@/store';
import { onMounted } from 'vue';
</script>
<template>



  <RouterView />

  <div v-if="userInfo && !userInfo.approved">
    <div class="d-flex justify-content-center align-items-center vh-100">
      <div class="card" style="width: 48rem;">

        <div class="card-body">
          <h5 class="card-title">wait till admin approves You</h5>

          <button type="button" @click="router.push({ name: 'homeView' })">Go Back</button>

        </div>
      </div>
    </div>



  </div>

  <div v-else-if="userInfo">
    <NavSponsor />


    <div class="card" style="width:max-content ;">
      <img src="/Users/linisha/Documents/PROJECT_MAD2/MAD2/frontend/src/assets/Home Page.png" class="card-img-top" alt="Image">



      <ul class="list-group list-group-flush">


        <li class="list-group-item"><b>Name : </b> {{ userInfo.username }} </li>
        <li class="list-group-item"><b>Your ID : </b> {{ userInfo.id }} </li>
        <li class="list-group-item"><b>Your Email : </b> {{ userInfo.email }} </li>
        <li class="list-group-item"><b>Your Industry Name : </b> {{ userInfo.name }} </li>
        <li class="list-group-item"><b>Industry : </b> {{ userInfo.industry }} </li>
        <li class="list-group-item"><b>Your Budget : </b> {{ userInfo.budget }} </li>
        <li class="list-group-item"><b> approved : </b> {{ userInfo.approved }} </li>
      </ul>

    </div>
  </div>

  <div v-else>






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
  },





}
</script>

<style scoped></style>