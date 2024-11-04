<script setup>

import { RouterView } from "vue-router";
import NavInfluencer from '@/components/Influencer/NavInfluencer.vue';
import store from '@/store';

</script>


<template>

  <RouterView />

  <div class="card" style="width: 80rem ;">
    <div v-if="userInfo">
      <ul class="list-group list-group-flush">


        <li class="list-group-item"><b>Total Number of Campaigns : </b> {{ userInfo.number_of_camp }} </li>
        <li class="list-group-item"><b>Public Campaigns Count : </b> {{ userInfo.number_of_public_camp }} </li>
        <li class="list-group-item"><b>Private Campaigns Count : </b> {{ userInfo.number_of_private_camp }} </li>

      </ul>
    </div>
    <div v-else> Loading... </div>
  </div>
  <br>
  <br>
  <br>
  <br>
  <hr>
  <hr>

  <hr>
  <br>
  <br>

  <div class="container-xxl  ">
    <div class="card mx-auto" style="width: 80rem;">
      <div class="card-body">
        <h5 class="card-title">Approve Sponsors</h5>
        <div v-if="userInfo.sponsors_to_approve && userInfo.sponsors_to_approve.length">
          <table class="table  table-striped-columns ">
            <thead>
              <tr class="table-info">
                <th scope="col">id</th>
                <th scope="col">name</th>
                <th scope="col">industry</th>
                <th scope="col">budget</th>
                <th scope="col">approved</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="sponsor in userInfo.sponsors_to_approve" :key="sponsor.id" class="table-success">
                <!-- <th scope="row">1</th> -->
                <td>{{ sponsor.id }}</td>
                <td>{{ sponsor.name }}</td>
                <td>{{ sponsor.industry }}</td>
                <td>{{ sponsor.budget }}</td>
                <td>{{ sponsor.approved }}</td>
              </tr>
            </tbody>
          </table>
        </div>
        <div v-else>
          Loading sponsors or no sponsors to approve...
        </div>



      </div>
    </div>
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
    InfluencerInfo() {
      fetch(import.meta.env.VITE_BASEURL + "/adminDashboard", {
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
    this.InfluencerInfo();
  }



}

</script>