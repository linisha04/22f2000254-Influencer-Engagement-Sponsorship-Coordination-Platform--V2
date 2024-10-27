<script setup>
import router from '@/router';
import { RouterLink } from 'vue-router';
import store from '@/store';
</script>
<template>

<div class="container mt-5 ">
        <div class="card mx-auto" style="width: 45rem;">
            <div class="card-body">
                <h5 class="card-title">Sponsor Register</h5>
                <form @submit.prevent="createCampaign()">


                    <div class="row mb-3">
                        <label for="campaignName" class="col-sm-2 col-form-label">Campaign Name</label>
                        <div class="col-sm-10">
                            <input type="text" class="form-control" id="campaignName" v-model="campaignName">
                        </div>
                    </div>



                    <fieldset class="row mb-3">
                        <legend class="col-form-label col-sm-2 pt-0">Campaign Type</legend>
                        <div class="col-sm-10">
                            
                            <div class="form-check ">
                                <input class="form-check-input" type="radio" name="visibility" id="public"
                                    value="public" v-model="visibility">
                                <label class="form-check-label" for="public">
                                    Public
                                </label>
                            </div>

                            <div class="form-check ">
                                <input class="form-check-input" type="radio" name="visibility" id="private"
                                    value="private" v-model="visibility">
                                <label class="form-check-label" for="private">
                                    Private
                                </label>
                            </div>
                        </div>
                    </fieldset>





                    <div class="row mb-3">
                        <label for="budget" class="col-sm-2 col-form-label">Budget</label>
                        <div class="col-sm-10">
                            <input type="number" class="form-control" id="budget" v-model="budget"> 
                        </div>
                    </div>
                    <!-- <div class="row mb-3">
                        <label for="start_date" class="col-sm-2 col-form-label">Start Date</label>
                        <div class="col-sm-10">
                            <input type="date" class="form-control" id="start_date" v-model="start_date">
                        </div>
                    </div>
                    <div class="row mb-3">
                        <label for="end_date" class="col-sm-2 col-form-label">End Date</label>
                        <div class="col-sm-10">
                            <input type="date" class="form-control" id="end_date" v-model="end_date">
                        </div>
                    </div> -->
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
                  <label for="campaignDescription" class="col-sm-2 col-form-label">Campaign Goals</label>
                    <div class="col-sm-10">
                    <textarea class="form-control" id="campaignDescription" rows="4" v-model="goals"></textarea>
                  </div>
                 </div>

                    <button type="submit" class="btn btn-primary">  Create Campaign </button>
                </form>


            </div>
        </div>
    </div>

</template>


<script>
    export default {
        data(){
        return {
            campaignName:null,
            budget:null,
            // start_date:null,
            // end_date:null,
            visibility:null,
            niche:null,
            goals:null
        }},
        methods:{

            validate(){
                let valid=true;
                if(!this.campaignName || !this.budget  || !this.visibility || !this.niche || !this.goals){
                    alert("Please enter full deatails");
                    valid=false;
                    
                }
                console.log('1');
                return valid;
            },
            createCampaign(){
                if(!this.validate()){
                    return ;


                }
                const token = store.getters.getToken;
                if (!token) {
                    alert("You are not logged in.");
                    return;
                }


                fetch(import.meta.env.VITE_BASEURL+"/createCampaign",
                {method : "POST" ,
                 headers:{"Content-Type" : "application/json", "Authentication-Token": store.getters.getToken},
                 body:JSON.stringify({campaignName:this.campaignName ,budget:this.budget  , visibility:this.visibility , niche: this.niche , goals:this.goals  })
                }).then(resp=>{return [resp.json() , resp.status]}).then(x=>{
                    if(x[1]==200){
                        router.push({name:"sponsorDashboard"})
                        console.log('Yes');
                    }else if(x[1]==400 ){
                        alert("Please enter correct deatails");

                    }else if (x[1]==404){
                        alert("No deatails");

                    }
                }
                )
                
            }




        }}
</script>
<style scoped></style>