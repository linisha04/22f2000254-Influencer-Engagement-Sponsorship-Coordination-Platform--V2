<script setup>
import { RouterLink } from 'vue-router'
</script>

<template>
    <nav class="navbar navbar-expand-lg fixed-top" style="background-color:brown;">
        <div class="container-fluid">
            <a class="navbar-brand" >Admin Dashboard</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
                data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false"
                aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                    <li class="nav-item">
                        <RouterLink class="nav-link active" aria-current="page"  to="/adminView/adminDashboard" >Home</RouterLink>
                    </li>
                   
                    <li class="nav-item">
                        <RouterLink class="nav-link active" to="/adminView/allCampaigns"> All Campaigns</RouterLink>

                        
                    </li>
                    <li class="nav-item">
                        <RouterLink class="nav-link active" to="/adminView/flagUsers"> Flag Users</RouterLink>

                        
                    </li>
                    <li class="nav-item">
                        <RouterLink class="nav-link active" to="/adminView/allAds"> All Ads</RouterLink>

                        
                    </li>
                    <li class="nav-item">
                        <RouterLink class="nav-link active" to="/"> Logout</RouterLink>
                    </li>
                </ul>
                
            </div>
        </div>
    </nav>
</template>




<style scoped>

body {
    padding-top: 56px; 
}
</style>