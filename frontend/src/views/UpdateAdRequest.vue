<script setup>
import store from '@/store';
import router from "@/router";
import { RouterView } from "vue-router";

</script>

<template>
    <br>
    <br>
    <h1>Update Adrequest</h1>
    <div class="container mt-5" v-if="adInfo.created_by===adInfo.current_user_id">
        <div class="card mx-auto" style="width: 45rem;">
            <div class="card-body">
                <h5 class="card-title">Update AD</h5>
                <form @submit.prevent="updateAd">
                    <div class="row mb-3">
                        <label for="AdName" class="col-sm-2 col-form-label">Name</label>
                        <div class="col-sm-10">
                            <input type="text" class="form-control" id="AdName" v-model="adInfo.name"
                                placeholder="Ad Name" disabled>
                        </div>
                    </div>
                    <div class="row mb-3">
                        <label for="amount" class="col-sm-2 col-form-label">amount</label>
                        <div class="col-sm-10">
                            <input type="number" class="form-control" id="amount" v-model="adInfo.amount"
                                placeholder="amount in Numbers">
                        </div>
                    </div>

                    <div class="row mb-3">
                        <label for="goals" class="col-sm-2 col-form-label">requirements</label>
                        <div class="col-sm-10">
                            <textarea v-model="adInfo.requirements" id="goals" placeholder="Enter your requirements here..."></textarea>
                        </div>
                    </div>

                    <button type="submit" class="btn btn-primary"> update the ad </button>
                </form>


            </div>
        </div>
    </div>
    <div class="container mt-5" v-else>
        <div class="card mx-auto" style="width: 45rem;">
            <div class="card-body">
                <h5 class="card-title">Update AD</h5>
                <form @submit.prevent="updatedStatus">
                    <div class="row mb-3">
                        <label for="AdName" class="col-sm-2 col-form-label">Name</label>
                        <div class="col-sm-10">
                            <input type="text" class="form-control" id="AdName" v-model="adInfo.name"
                                placeholder="Ad Name" disabled>
                        </div>
                    </div>
                    <div class="row mb-3">
                        <label for="amount" class="col-sm-2 col-form-label">amount</label>
                        <div class="col-sm-10">
                            <input type="number" class="form-control" id="amount" v-model="adInfo.amount"
                                placeholder="amount in Numbers" disabled>
                        </div>
                    </div>

                    <div class="row mb-3">
                        <label for="goals" class="col-sm-2 col-form-label">requirements</label>
                        <div class="col-sm-10">
                            <textarea v-model="adInfo.requirements" id="goals" disabled placeholder="Enter your requirements here..."></textarea>
                        </div>
                    </div>


                    <fieldset class="row mb-3">
                        <legend class="col-form-label col-sm-2 pt-0">status</legend>
                        <div class="col-sm-10">
                            <div class="form-check">
                                <input class="form-check-input" type="radio" name="status" id="pending"
                                    value="pending" v-model="adInfo.status">
                                <label class="form-check-label" for="pending">
                                    Pending
                                </label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input" type="radio" name="status" id="accepted"
                                    value="accepted" v-model="adInfo.status">
                                <label class="form-check-label" for="accept">
                                    Accept
                                </label>
                            </div>
                            <div class="form-check ">
                                <input class="form-check-input" type="radio" name="status" id="rejected"
                                    value="rejected" v-model="adInfo.status">
                                <label class="form-check-label" for="reject">
                                    Reject
                                </label>
                            </div>
                        </div>
                    </fieldset>


                    <button type="submit" class="btn btn-primary"> update the ad </button>
                </form>


            </div>
        </div>
    </div>




</template>




<script>

export default {
    props:{id:{required: true }},
    data(){
        return {
            adInfo:{
                 name:'',
                 amount:'',
                 requirements:'',
                 created_by:'',
                 sent_to:'',
                 status:'',
                 messages:'',
                 influencer_id:'',
                 campaign_id:'',
                 id:this.id,
                 current_user_id:''
            }
        }
    },
    methods:{
        getAdInfo() {
        console.log(this.id)
        fetch(import.meta.env.VITE_BASEURL + `/get_update_delete_Ad/${this.id}`, {
          method: 'GET',
          headers: {
            "Content-Type": "application/json",
            "Authentication-Token": store.getters.getToken
  
          },
  
        }).then((x => {
          return x.json()
        })).then(data => {
          console.log("Fetched adInfo:", data);
  
          this.adInfo = data;
  
        })
      },
      updateAd() {
            
            fetch(import.meta.env.VITE_BASEURL +`/get_update_delete_Ad/${this.id}`, {
                method: "PUT",
                headers: {
                    "Content-Type": "application/json",
                    'Authentication-Token': store.getters.getToken
                },
                body: JSON.stringify({amount: this.adInfo.amount  , requirements: this.adInfo.requirements
                })
            }).then(

                x => {
                    if (this.$store.getters.getRoles == 'influencer') {
                            router.push({ "name": "CampaignsPublic" })
        }else{
            router.push({ "name": "ViewCampaign" })
        }
                }
            )
        

    },
    updatedStatus(){

        fetch(import.meta.env.VITE_BASEURL +`/get_update_delete_Ad/${this.id}`, {
                method: "PUT",
                headers: {
                    "Content-Type": "application/json",
                    'Authentication-Token': store.getters.getToken
                },
                body: JSON.stringify({status: this.adInfo.status
                })
            }).then(

                x => {
                    if (this.$store.getters.getRoles == 'influencer') {
                            router.push({ "name": "CampaignsPublic" })
        }else{
            router.push({ "name": "ViewCampaign" })
        }
                }
            )

    }



    },
    mounted(){
        this.getAdInfo();
    }
}

</script>