<script setup>
import { RouterView } from "vue-router";
import store from '@/store';
import router from "@/router";
</script>

<template>

    <div class="container mt-5">
        <div class="card mx-auto" style="width: 45rem;">
            <div class="card-body">
                <h5 class="card-title">Create Campaign</h5>
                <form @submit.prevent="createCampaign">
                    <div class="row mb-3">
                        <label for="campaignName" class="col-sm-2 col-form-label">Name</label>
                        <div class="col-sm-10">
                            <input type="text" class="form-control" id="campaignName" v-model="campaignName"
                                placeholder="Campaign Name">
                        </div>
                    </div>
                    <div class="row mb-3">
                        <label for="budget" class="col-sm-2 col-form-label">Budget</label>
                        <div class="col-sm-10">
                            <input type="number" class="form-control" id="budget" v-model="budget"
                                placeholder="Budget in Numbers">
                        </div>
                    </div>
                    <fieldset class="row mb-3">
                        <legend class="col-form-label col-sm-2 pt-0">Visibility</legend>
                        <div class="col-sm-10">


                            <div class="form-check">
                                <input class="form-check-input" type="radio" name="visibility" id="public"
                                    value="public" v-model="visibility">
                                <label class="form-check-label" for="public">
                                    Public
                                </label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input" type="radio" name="visibility" id="private"
                                    value="private" v-model="visibility">
                                <label class="form-check-label" for="private">
                                    Private
                                </label>
                            </div>
                        </div>

                    </fieldset>



                    <fieldset class="row mb-3">
                        <legend class="col-form-label col-sm-2 pt-0">Niche</legend>
                        <div class="col-sm-10">
                            <div class="form-check">
                                <input class="form-check-input" type="radio" name="niche" id="Fashion&Beauty&Lifestyle"
                                    value="Fashion&Beauty&Lifestyle" v-model="niche">
                                <label class="form-check-label" for="Fashion&Beauty&Lifestyle">
                                    Fashion & Beauty & Lifestyle
                                </label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input" type="radio" name="niche" id="Health&Wellness"
                                    value="Health&Wellness" v-model="niche">
                                <label class="form-check-label" for="Health&Wellness">
                                    Health & Wellness
                                </label>
                            </div>
                            <div class="form-check ">
                                <input class="form-check-input" type="radio" name="niche" id="Travel&Adventure"
                                    value="Travel&Adventure" v-model="niche">
                                <label class="form-check-label" for="Travel&Adventure">
                                    Travel & Adventure
                                </label>
                            </div>
                            <div class="form-check ">
                                <input class="form-check-input" type="radio" name="niche" id="Tech&Gaming"
                                    value="Tech&Gaming" v-model="niche">
                                <label class="form-check-label" for="Tech&Gaming">
                                    Tech & Gaming
                                </label>
                            </div>

                            <div class="form-check ">
                                <input class="form-check-input" type="radio" name="niche" id="Food&Cooking&Lifestyle"
                                    value="Food&Cooking&Lifestyle" v-model="niche">
                                <label class="form-check-label" for="Food&Cooking&Lifestyle">
                                    Food & Cooking & Lifestyle
                                </label>
                            </div>

                            <div class="form-check ">
                                <input class="form-check-input" type="radio" name="niche" id="Education&Learning"
                                    value="Education&Learning" v-model="niche">
                                <label class="form-check-label" for="Education&Learning">
                                    Education & Learning
                                </label>
                            </div>
                        </div>
                    </fieldset>


                    <div class="row mb-3">
                        <label for="goals" class="col-sm-2 col-form-label">Goals</label>
                        <div class="col-sm-10">
                            <textarea v-model="goals" id="goals" placeholder="Enter your goals here..."></textarea>
                        </div>
                    </div>

                    <button type="submit" class="btn btn-primary"> createCampaign </button>
                </form>


            </div>
        </div>
    </div>
</template>


<script>
export default {
    data() {
        return {
         
            campaignName: null,
            budget: null,
            visibility: null,
            niche: null,
            goals: null

        }
    },
    methods: {
        validate() {

            let valid = true;
            if (!this.campaignName || !this.campaignName || !this.budget || !this.niche || !this.goals) {
                valid = false;
                alert("Please enter valid form details");
            }

            console.log(this.campaignName, this.campaignName, this.niche, this.budget)
            const token = this.$store.getters.getToken;
            console.log(token);
            console.log("anove is token");
            console.log(import.meta.env.VITE_BASEURL); // Should log the base URL
            console.log(this.$store.getters.getToken);
            return valid



        },

        createCampaign() {
            if (!this.validate()) {
                return;
            } else {
                fetch(import.meta.env.VITE_BASEURL + "/createCampaign", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                        'Authentication-Token': store.getters.getToken
                    },
                    body: JSON.stringify({
                        campaignName: this.campaignName,
                        niche: this.niche,
                        budget: this.budget,
                        visibility: this.visibility,
                        goals: this.goals
                    })
                }).then(

                    x => {
                        return router.push({ name: "sponsorDashboard" })
                    }
                )
            };

            // fetch(import.meta.env.VITE_BASEURL+"/createCampaign"  ,
            //      {method : "POST" , headers:{"Content-Type" : "application/json" ,"Authorization": `Bearer ${store.getters.getToken}`},
            //      body: JSON.stringify({campaignName: this.campaignName, niche: this.niche , budget:this.budget ,visibility:this.visibility , goals:this.goals})
            //    })

        }
    }

}
</script>
<style scoped></style>