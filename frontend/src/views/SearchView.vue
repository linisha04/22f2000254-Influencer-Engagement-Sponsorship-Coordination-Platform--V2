<script setup>
import NavSponsor from '@/components/Sponsor/NavSponsor.vue';
import router from '@/router';
import { RouterView } from "vue-router";

import store from '@/store';

</script>

<template>
    <div v-if="store.getters.getRoles.includes('influencer')">
        <div v-if="CampORInf.length>0">

        <table class="table  table-striped-columns fixed-top ">
            <thead>
                <tr class="table-info">
                    <th scope="col">id</th>
                    <th scope="col">campaignName</th>
                    <th scope="col">visibility</th>
                    <th scope="col">budget</th>
                    <th scope="col">niche</th>
                    <th scope="col">goals</th>
                    <th scope="col">Create Ad req <button type="button"
                            @click="router.push({ name: 'influencerDashboard' })">Dashboard</button></th>
                </tr>
            </thead>
           
            <tbody>
                <tr v-for="camp in CampORInf" :key="camp.id" class="table-success">
                    <!-- <th scope="row">1</th> -->
                    <td>{{ camp.id }}</td>
                    <td>{{ camp.campaignName }}</td>
                    <td>{{ camp.visibility }}</td>
                    <td>{{ camp.budget }}</td>
                    <td>{{ camp.niche }}</td>

                    <td>{{ camp.goals }}</td>
                    <td class="table-primary">
                        <button @click="router.push(`/createAdRequest/campaign_id/${camp.id}`)">Create Ad
                            Requests</button>
                        <button @click="router.push(`/viewAdRequests/campaign_id/${camp.id}`)">view Ad Requests</button>

                    </td>

                </tr>
            </tbody>
       
       
        </table>
    </div>

    <div v-else>
            No Public Campaigns for this niche
            <button type="button"
            @click="router.push({ name: 'influencerDashboard' })">Dashboard</button>
        </div>

    </div>
    <div v-if="store.getters.getRoles.includes('sponsor')">
  <div v-if="CampORInf.length>0">

        <table class="table  table-striped-columns  ">
            <thead>
                <tr>
                    <th scope="col" class="table-light">id</th>
                    <th scope="col" class="table-light">username</th>
                    <th scope="col" class="table-light">niche</th>
                    <th scope="col" class="table-light">followers</th>
                    <th scope="col" class="table-light">earnings</th>
                    <th scope="col" class="table-light">bio  <button type="button" @click="router.push({ name: 'sponsorDashboard' })">Dashboard</button></th>
                   
                    <!-- <th scope="col" class="table-light">
                        Select
                    </th> -->
                </tr>
            </thead>
          

           
            <tbody>
                <tr v-for="inf in CampORInf" :key="inf.id">
                    <td class="table-warning">{{ inf.id }}</td>
                    <td class="table-warning">{{ inf.username }}</td>
                    <td class="table-warning"> {{ inf.niche }}</td>
                    <td class="table-warning">{{ inf.followers }}</td>
                    <td class="table-warning">{{ inf.earnings }}</td>
                    <td class="table-warning">{{ inf.bio }}</td>
                    <!-- <td class="table-warning"><button type="button" @click="select(inf.id)">Select</button></td> -->

                </tr>
            </tbody>
      
        </table>
        


    </div>
    
    <div v-else>
            No influencers

            <button type="button" @click="router.push({ name: 'sponsorDashboard' })">Dashboard</button>
        </div>

    </div>


</template>

<script>

export default {
    props: {
        word: {
            word: { type: String,required: true }
        }
    },
    data() {
        return {
            CampORInf:[],

        }
    },
    methods: {

        getCampOrInf() {
            console.log("Fetched step")
            console.log(this.word)

            fetch(import.meta.env.VITE_BASEURL + `/search/${this.word}`,
                {
                    method: 'GET',
                    headers: {
                        "Content-Type": "application/json",
                        "Authentication-Token": store.getters.getToken

                    },

                }).then((x => {
                    return x.json()
                })).then(data => {
                    console.log("Fetched CampORInf:", data);

                    this.CampORInf = data;

                })
        },
    },
    mounted() {

        this.getCampOrInf();
    }

}

</script>
