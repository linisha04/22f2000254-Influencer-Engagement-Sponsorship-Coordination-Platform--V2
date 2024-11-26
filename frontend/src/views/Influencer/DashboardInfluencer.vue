<script setup>

import { RouterView } from "vue-router";
import NavInfluencer from '@/components/Influencer/NavInfluencer.vue';
import store from '@/store';

</script>


    <template>

<RouterView/>

<div class="card" style="width: 56rem ;">
  <img src="/Users/linisha/Documents/PROJECT_MAD2/MAD2/frontend/src/assets/Home Page.png" class="card-img-top" alt="Image">
 
  
  <div v-if="userInfo">
  <ul class="list-group list-group-flush">


    <li class="list-group-item"><b>Name : </b> {{ userInfo.username }}      </li>
    <li class="list-group-item"><b>Your ID : </b>    {{ userInfo.id}}                      </li>
    <li class="list-group-item"><b>Your Email : </b>    {{ userInfo.email}}                      </li>
    <li class="list-group-item"><b>Earnings : </b>   {{ userInfo.earnings }}                  </li>
    <li class="list-group-item"><b>Niche : </b>          {{ userInfo.niche }}                        </li>
    <li class="list-group-item"><b>Your Bio : </b>            {{ userInfo.bio }}                   </li>
    <li class="list-group-item"><b>Your Budget : </b>            {{ userInfo.followers }}                   </li>
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
    InfluencerInfo() {
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
    this.InfluencerInfo();
  }
  

 
 }

</script>