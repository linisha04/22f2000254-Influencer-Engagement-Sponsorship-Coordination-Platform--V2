<script setup>
import store from '@/store';
import router from "@/router";
</script>
<template>

    <table class="table  table-striped-columns fixed-top ">
        <thead>
            <tr>
                <th scope="col" class="table-light">AD Info</th>
                <th scope="col" class="table-light"><button>
                        <RouterLink class="nav-link active" aria-current="page" to="/adminView/adminDashboard">Dashboard
                        </RouterLink>
                    </button>
                </th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="ad in allAdReq" :key="ad.id">

                <td class="table-warning">Ad Id : {{ ad.id }} <br>


                    campaign_id : {{ ad.campaign_id }} <br>
                    Ad name :{{ ad.name }}<br>
                    influencer_id : {{ ad.influencer_id }} <br>
                    requirements : {{ ad.requirements }} <br>
                    Ad Amount :{{ ad.amount }}<br>
                    Ad status : <button disabled class="btn btn-primary">{{ ad.status }}</button><br>
                    Req Created by : {{ ad.created_by }} <br>
                    Req sent to :{{ ad.sent_to }}

                </td>
                <td>
                    <div class="card-body">
                        <h5 class="card-title">Negotiation</h5>
                        <br>

                        {{ ad.messages }}


                    </div>




                </td>


            </tr>
        </tbody>
    </table>

</template>

<script>
export default {

    data() {
        return {
            allAdReq: []
        }
    },
    methods: {

        getAllAdReq() {
            fetch(import.meta.env.VITE_BASEURL + "/allAds", {
                method: 'GET',
                headers: {
                    "Content-Type": "application/json",
                    "Authentication-Token": store.getters.getToken

                },

            }).then((x => {
                return x.json()
            })).then(data => {

                this.allAdReq = data;

            })
        }
    },
    mounted() {

        this.getAllAdReq();
    }

}

</script>
