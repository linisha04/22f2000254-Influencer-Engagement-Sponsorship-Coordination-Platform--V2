<script setup>
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



                    <fieldset class="row mb-3">
                        <legend class="col-form-label col-sm-2 pt-0">Visibility</legend>
                        <div class="col-sm-10">


                            <div class="form-check">
                                <input class="form-check-input" type="radio" name="visibility" id="public"
                                    value="public" v-model="campaignInfo.visibility">
                                <label class="form-check-label" for="public">
                                    Public
                                </label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input" type="radio" name="visibility" id="private"
                                    value="private" v-model="campaignInfo.visibility">
                                <label class="form-check-label" for="private">
                                    Private
                                </label>
                            </div>
                        </div>

                    </fieldset>




                    <div class="row mb-3">
                        <label for="goals" class="col-sm-2 col-form-label">Goals</label>
                        <div class="col-sm-10">
                            <textarea v-model="campaignInfo.goals" id="goals" placeholder="Enter your goals here..."></textarea>
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
    props: { id: { required: true } },
    data() {
        return {
            campaignInfo: null,
            newbudget: null,
            newvisibility: null,
        }
    },
    method: {
        getCampaign() {
            fetch(import.meta.env.VITE_BASEURL + `get_update_campaign/${this.id}`,
                {
                    method: 'GET',
                    headers: {
                        "Content-Type": "application/json",
                        "Authentication-Token": store.getters.getToken

                    },

                }).then((x => {
                    return x.json()
                })).then(data => {
                    console.log("Fetched campaignInfo:", data);

                    this.campaignInfo = data;

                })
        },
        
    },
    mounted(){
        this.getCampaign();
    }
}

</script>