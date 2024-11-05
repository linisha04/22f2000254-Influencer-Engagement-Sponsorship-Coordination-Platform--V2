<script setup>
import store from '@/store';
import router from "@/router";
import NavSponsor from '@/components/Sponsor/NavSponsor.vue';</script>
<template>

<div v-if="getAdRequests && getAdRequests.length>0">

    <table class="table  table-striped-columns fixed-top ">
    <thead>
      <tr>
        <th scope="col" class="table-light">id</th>
        <th scope="col" class="table-light">campaign_id</th>
        <th scope="col" class="table-light">visibility</th>
        <th scope="col" class="table-light">name</th>
        <th scope="col" class="table-light">influencer_id</th>
        <th scope="col" class="table-light">requirements</th>
        <th scope="col" class="table-light">amount</th>
        <th scope="col" class="table-light">status</th>
        <th scope="col" class="table-light">created_by</th>
        <th scope="col" class="table-light">sent_to</th>
        <th scope="col" class="table-light">Delete</th>
        <th scope="col" class="table-light">Update</th>
        <th scope="col" class="table-light">Create Ad Requests</th>
        <th scope="col" class="table-light"><button>
            <RouterLink class="nav-link active" aria-current="page" to="/sponsorView/dashboardSponsor">Dashboard</RouterLink>
          </button></th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="ad in getAdRequests" :key="ad.id">
       
        <td class="table-warning">{{ ad.id }}</td>
        <td class="table-warning">{{ ad.campaign_id }}</td>
        <td class="table-warning">{{ ad.name }}</td>
        <td class="table-warning">{{ ad.influencer_id }}</td>
        <td class="table-warning">{{ ad.requirements }}</td>
        <td class="table-warning">{{ ad.amount }}</td>
        <td class="table-warning">{{ ad.status }}</td>
        <td class="table-warning">{{ ad.created_by }}</td>
        <td class="table-warning">{{ ad.sent_to }}</td>
        <td class="table-warning"><button @click="updateCampaign(camp.id)">Update</button></td>
        <td class="table-danger"><button @click="deleteCampaign(camp.id)">Delete</button></td>
       

      </tr>
    </tbody>
  </table>

</div>
<div></div>

</template>
<script>

export default {
    props:{
        id:{
            id:{required : true}
        }
    },
    data(){
        return{
            getAdRequests:null,
          

        }
    },
    methods:{
        getAds(){
            fetch(import.meta.env.VITE_BASEURL+`/getAdRequest/${this.id}`,
            {
        method: 'GET',
        headers: {
          "Content-Type": "application/json",
          "Authentication-Token": store.getters.getToken

        },

      }).then((x => {
        return x.json()
      })).then(data => {
        console.log("Fetched ads:", data);

        this.getAdRequests = data;

      })
        }
    }
}


</script>