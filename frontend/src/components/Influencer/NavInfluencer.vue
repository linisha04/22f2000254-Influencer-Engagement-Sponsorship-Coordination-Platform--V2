<script setup>
import { RouterLink } from 'vue-router'
import router from '@/router';
import store from '@/store';

</script>

<template>
    <nav class="navbar navbar-expand-lg  fixed-top" style="background-color:burlywood;">
        <div class="container-fluid">
            <a class="navbar-brand">Influencer Dashboard</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
                data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false"
                aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                    <li class="nav-item">
                        <RouterLink class="nav-link active" aria-current="page"
                            to="/influencerView/dashboardInfluencer">Home</RouterLink>
                    </li>

                    <li class="nav-item">
                        <RouterLink class="nav-link active" to="/influencerView/campaignsPublic"> Public Campaigns
                        </RouterLink>


                    </li>
                    <li class="nav-item">
                        <button class="nav-link active" @click="logout"> Logout</button>
                    </li>
                </ul>
                <form class="d-flex" role="search" @submit.prevent="search">

                    <input class="form-control me-2" type="search" placeholder="Search public Campaign"
                        aria-label="Search" v-model="keyword">

                    <button class="btn btn-outline-success" type="submit">Search</button>

                </form>

            </div>
        </div>
    </nav>
</template>


<script>

export default {
    data() {
        return {
            keyword: null
        }
    }
    ,
    methods: {
        logout() {
            fetch(import.meta.env.VITE_BASEURL + "/logout", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    'Authentication-Token': store.getters.getToken
                }
            }).then(

                x => {
                    store.dispatch('logout')
                    router.push('/signin')
                }
            )
        },
        search() {
            if (this.keyword) {
                router.push(`/search/keyword/${this.keyword}`)
            }
        }
    }
}

</script>
