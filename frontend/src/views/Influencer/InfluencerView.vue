<script setup>
import { RouterView } from "vue-router";
import NavInfluencer from '@/components/Influencer/NavInfluencer.vue';

import router from '@/router';
import { RouterLink } from 'vue-router';
import store from '@/store';
</script>
<template>
   
<NavInfluencer/>
<RouterView/>

</template>

<script>
 
</script>

<style scoped>

</style>