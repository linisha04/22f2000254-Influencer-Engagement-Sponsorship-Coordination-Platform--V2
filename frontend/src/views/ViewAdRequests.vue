<script setup>
import store from '@/store';
import router from "@/router";
import NavSponsor from '@/components/Sponsor/NavSponsor.vue';</script>
<template>

  <div v-if="getAdRequests && getAdRequests.length > 0">

    <table class="table  table-striped-columns  ">
      <thead>
        <tr>
          <th scope="col" class="table-light">AD Info</th>
          <th scope="col" class="table-light">

              <div v-if="store.getters.getRoles == 'sponsor'">
                <button type="button" @click='router.push({ name: "sponsorDashboard" })'>Dashboard</button>
              </div>

              <div v-else>
             
                <button @click='router.push({ name: "influencerDashboard" })'>Dashboard</button>
              

              </div>


            </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="ad in getAdRequests" :key="ad.id">

          <td class="table-warning">Ad Id : {{ ad.id }} <br>


            campaign_id : {{ ad.campaign_id }} <br>
            Ad name :{{ ad.name }}<br>
            influencer_id : {{ ad.influencer_id }} <br>
            requirements : {{ ad.requirements }} <br>
            Ad Amount :{{ ad.amount }}<br>
            Ad status : <button disabled class="btn btn-primary">{{ ad.status }}</button><br>
            Req Created by : {{ ad.created_by }} <br>
            Req sent to :{{ ad.sent_to }}
            <br> <button @click="router.push(`/updateAdRequests/AdID/${ad.id}`)">Update</button> <button
              @click="deleteAd(ad.id)">Delete</button>
          </td>
          <td>
            <div class="card-body">
              <h5 class="card-title">Negotiation</h5>
              <br>

              {{ ad.messages }}


            </div>
            <br>
            <form @submit.prevent="sendMessage(ad.id)">
              <div class="row mb-3">
                <label for="campaignName" class="col-sm-2 col-form-label">Write Message</label>
                <div class="col-sm-10">
                  <input type="text" v-model="message" class="form-control" id="campaignName"
                    placeholder="Type message here"><br> <button type="submit" class="btn btn-primary"> Send </button>
                </div>
              </div>

            </form>


          </td>


        </tr>
      </tbody>
    </table>

  </div>

  <div v-else>
    <div>

      <div v-if="store.getters.getRoles == 'sponsor'">
        <button @click='router.push({ name: "sponsorDashboard" })'>Dashboard</button>
        Currently no ad requests for this campaign
      </div>
      <div v-else>
        <button @click='router.push({ name: "influencerDashboard" })'>Dashboard</button>

        Currently no ad requests for this campaign


      </div>

    </div>
  </div>

</template>
<script>

export default {
  props: {
    id: {
      id: { required: true }
    }
  },
  data() {
    return {
      getAdRequests: null,
      message: ''


    }
  },
  methods: {

    getAds() {


      const campId = this.id;
      fetch(import.meta.env.VITE_BASEURL + `/viewAdRequests/campaign_id/${campId}`,
        {
          method: 'GET',
          headers: {
            "Content-Type": "application/json",
            "Authentication-Token": store.getters.getToken

          },

        }).then((x => {
          return x.json()
        })).then(data => {


          this.getAdRequests = data;

        })
    },
    deleteAd(id) {
      fetch(import.meta.env.VITE_BASEURL + `/get_update_delete_Ad/${id}`,
        {
          method: "DELETE",
          headers: {
            "Authentication-Token": store.getters.getToken
          }
        }).then(x => {
          if (this.$store.getters.getRoles == 'influencer') {
            router.push({ "name": "CampaignsPublic" })
          } else {
            router.push({ "name": "ViewCampaign" })
          }
        })
    },
    sendMessage(id) {

      fetch(import.meta.env.VITE_BASEURL + `/get_update_delete_Ad/${id}`, {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
          'Authentication-Token': store.getters.getToken
        },
        body: JSON.stringify({
          messages: this.message
        })
      }).then(

        x => {
          if (this.$store.getters.getRoles == 'influencer') {
            router.push({ "name": "CampaignsPublic" })
          } else {
            router.push({ "name": "ViewCampaign" })
          }
        }
      )


    }

  },
  mounted() {
   
    this.getAds();
  }

}


</script>

<style scoped>
.message-container {
  height: 300px;
  overflow-y: auto;
  padding: 10px;
  background-color: grey;
 
}
</style>