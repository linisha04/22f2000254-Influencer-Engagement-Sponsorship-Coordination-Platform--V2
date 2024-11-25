<script setup>
import store from '@/store';
import router from "@/router";
import { RouterView } from "vue-router";

</script>

<template>
  <br>
  <br>
  <h1> <b>Update the Campaign</b></h1>
  <div class="container mt-5">
    <div class="card mx-auto" style="width: 45rem;">
      <div class="card-body">
        <h5 class="card-title">Create Campaign</h5>
        <form @submit.prevent="updateCampaign">
          <div class="row mb-3">
            <label for="campaignName" class="col-sm-2 col-form-label">Name</label>
            <div class="col-sm-10">
              <input type="text" class="form-control" id="campaignName" v-model="campaignInfo.campaignName"
                placeholder="Campaign Name" disabled>
            </div>
          </div>
          <div class="row mb-3">
            <label for="budget" class="col-sm-2 col-form-label">Budget</label>
            <div class="col-sm-10">
              <input type="number" class="form-control" id="budget" v-model="campaignInfo.budget"
                placeholder="Budget in Numbers">
            </div>
          </div>

          <div class="row mb-3">
            <label for="goals" class="col-sm-2 col-form-label">Goals</label>
            <div class="col-sm-10">
              <textarea v-model="campaignInfo.goals" id="goals" placeholder="Enter your goals here..."></textarea>
            </div>
          </div>

          <button type="submit" class="btn btn-primary"> Update  </button>
        </form>


      </div>
    </div>
  </div>


</template>






<script>


export default {
  props: { id: { required: true } }
  ,

  data() {
    return {
      campaignInfo: {
        campaignName: '',
        goals: '',
        budget: 0


      },
      new_goals: null,
      new_budget: null
    }
  },
  methods: {
  
    campInfo() {
      console.log(this.id)
      fetch(import.meta.env.VITE_BASEURL + `/updateCampaign/${this.id}`, {
        method: 'GET',
        headers: {
          "Content-Type": "application/json",
          "Authentication-Token": store.getters.getToken

        },

      }).then((x => {
        return x.json()
      })).then(data => {
        console.log("Fetched campInfo:", data);

        this.campaignInfo = data;

      })
    },
    updateCampaign() {
          fetch(import.meta.env.VITE_BASEURL + `/updateCampaign/${this.id}`, {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
          'Authentication-Token': store.getters.getToken
        },
        body: JSON.stringify({
          budget: this.campaignInfo.budget, goals: this.campaignInfo.goals
        })
      }).then(

        x => {
          return router.push({ name: "ViewCampaign" })
        }
      )
     

    }

  },
  mounted() {

    this.campInfo();
  }



}



</script>

<style></style>