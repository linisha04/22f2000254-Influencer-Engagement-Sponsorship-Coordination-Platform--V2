<script setup>
import store from '@/store';
import router from "@/router";
import NavSponsor from '@/components/Sponsor/NavSponsor.vue';</script>
<template>

  <div v-if="getAdRequests && getAdRequests.length > 0">

    <table class="table  table-striped-columns fixed-top ">
      <thead>
        <tr>
          <th scope="col" class="table-light">AD Info</th>
          <!-- <th scope="col" class="table-light">campaign_id</th>
        <th scope="col" class="table-light">name</th>
        <th scope="col" class="table-light">influencer_id</th>
        <th scope="col" class="table-light">requirements</th>
        <th scope="col" class="table-light">amount</th>
        <th scope="col" class="table-light">status</th>
        <th scope="col" class="table-light">created_by</th>
        <th scope="col" class="table-light">sent_to</th> -->
          <!-- <th scope="col" class="table-light">Update</th>
        <th scope="col" class="table-light">Delete</th> -->

          <th scope="col" class="table-light"><button>
              <RouterLink class="nav-link active" aria-current="page" to="/sponsorView/dashboardSponsor">Dashboard
              </RouterLink>
            </button></th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="ad in getAdRequests" :key="ad.id">

          <td class="table-warning">Ad Id : {{ ad.id }} <br> campaign_id : {{ ad.campaign_id }} <br> Ad name :
            {{ ad.name }}
            <br> influencer_id : {{ ad.influencer_id }} <br> requirements : {{ ad.requirements }} <br> Ad Amount :
            {{ ad.amount }}
            <br> Ad status : {{ ad.status }} <br> Req Created by : {{ ad.created_by }} <br> Req sent to :
            {{ ad.sent_to }}
            <br> <button @click="updateCampaign(camp.id)">Update</button> <button
              @click="deleteAd(ad.id)">Delete</button>
          </td>
          <!-- <td class="table-warning">{{ ad.campaign_id }}</td>
        <td class="table-warning">{{ ad.name }}</td>
        <td class="table-warning">{{ ad.influencer_id }}</td>
        <td class="table-warning">{{ ad.requirements }}</td>
        <td class="table-warning">{{ ad.amount }}</td>
        <td class="table-warning">{{ ad.status }}</td>
        <td class="table-warning">{{ ad.created_by }}</td>
        <td class="table-warning">{{ ad.sent_to }}</td> -->
          <!-- <td class="table-warning"><button @click="updateCampaign(camp.id)">Update</button></td>
        <td class="table-danger"><button @click="deleteCampaign(camp.id)">Delete</button></td> -->
          <td>
            <div class="card-body">
              <h5 class="card-title">Messages</h5>
              <div class="message-container" style="height: 300px; overflow-y: auto;">
                <div>
                  <h4>Sponsor</h4>
                  <p>{{ ad.messages }}</p>
                </div>
                <!-- <div>
            <h4>Second Message</h4>
            <p>Donec elementum ligula eu sapien consequat eleifend...</p>
        </div>
        <div>
            <h4>Third Message</h4>
            <p>Aenean faucibus nibh et justo cursus id rutrum lorem imperdiet...</p>
        </div>
        <div>
            <h4>Third Message</h4>
            <p>Aenean faucibus nibh et justo cursus id rutrum lorem imperdiet...</p>
        </div>
        <div>
            <h4>Third Message</h4>
            <p>Aenean faucibus nibh et justo cursus id rutrum lorem imperdiet...</p>
        </div>
        <div>
            <h4>Third Message</h4>
            <p>Aenean faucibus nibh et justo cursus id rutrum lorem imperdiet...</p>
        </div> -->

              </div>
            </div>
            <form>
              <div class="row mb-3">
                <label for="campaignName" class="col-sm-2 col-form-label">Write Message</label>
                <div class="col-sm-10">
                  <input type="text" class="form-control" id="campaignName" v-model="newMessage"
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
    <RouterLink class="nav-link active" aria-current="page" to="/sponsorView/dashboardSponsor">Dashboard</RouterLink>

    Currently no ad requests for this campaign

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


    }
  },
  methods: {

    getAds() {
      console.log("Fetched step")
      console.log(this.id)
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
          console.log("Fetched ads:", data);

          this.getAdRequests = data;

        })
    },
    deleteAd(id) {
      fetch(import.meta.env.VITE_BASEURL + `/deleteAd/${id}`,
        {
          method: "DELETE",
          headers: {
            "Authentication-Token": store.getters.getToken
          }
        }).then(x => {
          return router.push({ name: "ViewCampaign" })
        })
    },
    
  },
  mounted() {
      console.log("mounted")
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
  /* Optional: background color */
}
</style>