<script setup >
import { RouterLink, RouterView } from 'vue-router'
import { createRouter, createWebHistory } from 'vue-router';

import store from "@/store";

// import HelloWorld from '@/components/HelloWorld.vue'
// import Navbar from '@/components/Navbar.vue';
</script>

<template>
  <RouterView />
</template>

<script>
export default {
    created(){
      let user = localStorage.getItem("user")
      store.commit("setUser", (user) ? JSON.parse(user) : {token: null,roles: []});
    }
  }
</script>

<style scoped>

</style>
