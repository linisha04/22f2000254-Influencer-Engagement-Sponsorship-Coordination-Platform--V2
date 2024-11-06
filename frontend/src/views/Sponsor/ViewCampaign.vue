<script setup>
import NavSponsor from '@/components/Sponsor/NavSponsor.vue';
import store from '@/store';
import router from "@/router";
import { RouterView } from "vue-router";



</script>

<template>


  <table class="table  table-striped-columns fixed-top ">
    <thead>
      <tr>
        <th scope="col" class="table-light">id</th>
        <th scope="col" class="table-light">campaignName</th>
        <th scope="col" class="table-light">visibility</th>
        <th scope="col" class="table-light">budget</th>
        <th scope="col" class="table-light">niche</th>
        <th scope="col" class="table-light">goals</th>
        <th scope="col" class="table-light">Update</th>
        <th scope="col" class="table-light">Delete</th>
        <th scope="col" class="table-light">View Ad Requests</th>
        <th scope="col" class="table-light">Create Ad Requests</th>
        <th scope="col" class="table-light"><button>
            <RouterLink class="nav-link active" aria-current="page" to="/sponsorView/dashboardSponsor">Dashboard</RouterLink>
          </button></th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="camp in userCamps" :key="camp.id">
       
        <td class="table-warning">{{ camp['id'] }}</td>
        <td class="table-warning">{{ camp['campaignName'] }}</td>
        <td class="table-warning"> {{ camp['visibility'] }}</td>
        <td class="table-warning">{{ camp['budget'] }}</td>
        <td class="table-warning">{{ camp['niche'] }}</td>
        <td class="table-warning">{{ camp['goals'] }}</td>
        <td class="table-warning"><button @click="updateCampaign(camp.id)">Update</button></td>
        <td class="table-danger"><button @click="deleteCampaign(camp.id)">Delete</button></td>
        <td class="table-success"><button @click="router.push(`/viewAdRequests/campaign_id/${camp.id}`)">View Ad Requests</button></td>
        <td class="table-primary"><button  @click="router.push(`/createAdRequest/campaign_id/${camp.id}`)" >Create Ad Requests</button></td>
       

      </tr>
    </tbody>
  </table>





</template>


<script>

export default {
  data() {
    return {
      userCamps: null
    }
  },
  methods: {
    userCampaigns() {
      fetch(import.meta.env.VITE_BASEURL + "/viewCampaign", {
        method: 'GET',
        headers: {
          "Content-Type": "application/json",
          "Authentication-Token": store.getters.getToken

        },

      }).then((x => {
        return x.json()
      })).then(data => {
        console.log("Fetched campaigns:", data);

        this.userCamps = data;

      })
    },
    deleteCampaign(id) {
      fetch(import.meta.env.VITE_BASEURL + `/deleteCampaign/${id}`,
        {
          method: "DELETE",
          headers: {
            "Authentication-Token": store.getters.getToken
          }
        }).then(x => {
          return router.push({ name: "sponsorDashboard" })
        })

    },
    // createAdRequest(campaign_id){
    //   fetch(import.meta.env.VITE_BASEURL)

    // }
  },
  mounted() {

    this.userCampaigns();
  }



}



</script>

<style></style>