<script setup>
import store from '@/store';
import router from "@/router";
import NavSponsor from '@/components/Sponsor/NavSponsor.vue';

</script>




<template>

    <div v-if="role == 'sponsor'">

        <div class="container mt-5 ">
            <div class="card mx-auto" style="width: 70rem;">
                <div class="card-body ">
                    <h5 class="card-title ">Create Ad Request</h5>
                    <form @submit.prevent="createAdRequest()">
                        <div class="mb-3">
                            <label for="adname" class="form-label">Advertisement Name</label>
                            <input type="text" class="form-control" id="adname" v-model="name">

                        </div>
                        <div class="mb-3">
                            <label for="amount" class="form-label">amount</label>
                            <input type="number" class="form-control" id="amount" v-model="amount">
                        </div>
                        <div class="mb-3">
                            <label for="requirements" class="form-label">requirements</label>
                            <textarea class="form-control" id="requirements" v-model="requirements"></textarea>
                        </div>
                        <div class="mb-3">
                            <table class="table  table-striped-columns  ">
                                <thead>
                                    <tr>
                                        <th scope="col" class="table-light">id</th>
                                        <th scope="col" class="table-light">username</th>
                                        <th scope="col" class="table-light">niche</th>
                                        <th scope="col" class="table-light">followers</th>
                                        <th scope="col" class="table-light">earnings</th>
                                        <th scope="col" class="table-light">bio</th>
                                        <th scope="col" class="table-light">
                                            Select
                                        </th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr v-for="inf in influencers" :key="inf.id">
                                        <td class="table-warning">{{ inf.id }}</td>
                                        <td class="table-warning">{{ inf.username }}</td>
                                        <td class="table-warning"> {{ inf.niche }}</td>
                                        <td class="table-warning">{{ inf.followers }}</td>
                                        <td class="table-warning">{{ inf.earnings }}</td>
                                        <td class="table-warning">{{ inf.bio }}</td>
                                        <td class="table-warning"><button type="button"
                                                :disabled="influencer_id === inf.id" @click="select(inf.id)">
                                                {{ influencer_id === inf.id ? 'Selected' : 'Select' }}</button></td>


                                    </tr>
                                </tbody>
                            </table>

                        </div>




                        <button type="submit" class="btn btn-primary">Create Request</button>
                    </form>


                </div>
            </div>
        </div>



    </div>

    <div v-else>
        <br>
        <br>
        <h1></h1>
        <h5 class="card-title ">Create Ad Request</h5>
        <form @submit.prevent="createAdRequest()">
            <div class="mb-3">
                <label for="adname" class="form-label">Advertisement Name</label>
                <input type="text" class="form-control" id="adname" v-model="name">

            </div>
            <div class="mb-3">
                <label for="amount" class="form-label">amount</label>
                <input type="number" class="form-control" id="amount" v-model="amount">
            </div>
            <div class="mb-3">
                <label for="requirements" class="form-label">requirements</label>
                <textarea class="form-control" id="requirements" v-model="requirements"></textarea>
            </div>

            <button type="submit" class="btn btn-primary">Create Request</button>
        </form>


    </div>

</template>





<script>

export default {
    props: { id: { required: true } },
    data() {
        return {


            influencers: null,
            name: null,
            amount: null,
            requirements: null,
            influencer_id: null,
            role: store.getters.getRoles
        }
    },
    methods: {

        getInfluencers() {
            fetch(import.meta.env.VITE_BASEURL + "/getInfluencers", {
                method: 'GET',
                headers: {
                    "Content-Type": "application/json",
                    "Authentication-Token": store.getters.getToken

                },

            }).then((x => {
                return x.json()
            })).then(data => {
                console.log("Fetched influencers:", data);

                this.influencers = data;

            })
        },
        select(inf_id) {
            console.log(inf_id);
            this.influencer_id = inf_id
        },
        validate() {
            let valid = true;
            if (!this.name) {
                valid = false
                alert("Please fill the AdRequest name")
            }
            if (!this.amount || this.amount<0) {
                valid = false
                alert("Please fill the AdRequest amount and should be greater than zero")
            }
            if (!this.requirements) {
                valid = false
                alert("Please fill the AdRequest requirements")
            }
            if (store.getters.getRoles == 'sponsor') {
                if (!this.influencer_id) {
                    valid = false
                    alert("Please Choose the influencer_id ")
                }
            }

            return valid
        }
        ,
        createAdRequest() {
            if (!this.validate()) {
                return
            }
            fetch(import.meta.env.VITE_BASEURL + "/createAdrequest", {
                method: 'POST',
                headers: {
                    "Content-Type": "application/json",
                    'Authentication-Token': store.getters.getToken
                },
                body: JSON.stringify({
                    name: this.name, amount: this.amount, requirements: this.requirements, influencer_id: this.influencer_id, campaign_id: this.id
                })
            }).then(x => {
                if (x.status == 201) {

                    if (store.getters.getRoles == 'influencer') {
                        router.push({ "name": "CampaignsPublic" })
                    } else {
                        router.push({ "name": "ViewAdRequests" })
                    }


                }
                if (x.status == 409) {
                    alert("Req already exists for this campaign")

                    if (this.$store.getters.getRoles == 'influencer') {
                        router.push({ "name": "CampaignsPublic" })
                    } else {
                        router.push({ "name": "ViewAdRequests" })
                    }


                }
            })
        }


    },
    mounted() {
        if (this.$store.getters.getRoles == 'sponsor') {
            this.getInfluencers();
        }

    }
}

</script>