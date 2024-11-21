<script setup>

import { RouterView } from "vue-router";
import store from '@/store';

</script>


<template>

  <RouterView />
  
  <br>
  
  
  <br>
       
        <div v-if="userInfo && userInfo.sponsors_to_approve">
       
          <table class="table  table-striped-columns  fixed">
            <thead>
              <tr class="table-info">
                <th scope="col">id</th>
                <th scope="col">name</th>
                <th scope="col">industry</th>
                <th scope="col">budget</th>
                <th scope="col">approved</th>
                <th scope="col"></th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="sponsor in userInfo.sponsors_to_approve" :key="sponsor.id" class="table-success">
                
                <td>{{ sponsor.id }}</td>
                <td>{{ sponsor.name }}</td>
                <td>{{ sponsor.industry }}</td>
                <td>{{ sponsor.budget }}</td>
                <td>{{ sponsor.approved }}</td>
                <td><button  @click="changeApproval(sponsor)">{{ sponsor.approved ? 'Revoke Approval' : 'Grant Approval' }}</button></td>
              </tr>
            </tbody>
          </table>
        </div>
        <div v-else>
          no sponsors to approve...
        </div>



        <div class="card" style="width: 80rem ;">
    <div v-if="userInfo">
      <ul class="list-group list-group-flush">


        <li class="list-group-item"><b>Total Number of Campaigns : </b> {{ userInfo.number_of_camp }} </li>
        <li class="list-group-item"><b>Public Campaigns Count : </b> {{ userInfo.number_of_public_camp }} </li>
        <li class="list-group-item"><b>Private Campaigns Count : </b> {{ userInfo.number_of_private_camp }} </li>

      </ul>
    </div>
    <div v-else> Loading... </div>
  </div>
  
  

  
  
     

</template>

<script>
export default {
  data() {
    return {
      userInfo: null,
    
    };
  },

  methods: {
    DashboardInfo() {
      fetch(import.meta.env.VITE_BASEURL + "/adminDashboard", {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
          'Authentication-Token': store.getters.getToken
        },
      })
        .then(x => {
          return x.json()
        })
        .then(data => {
          this.userInfo = data;
        })

    },
    
    changeApproval(sponsor){
      if (!sponsor) {
    console.error('Sponsor is undefined');
    return;
  }
      console.log(sponsor)
     const status=!sponsor.approved;
     fetch(import.meta.env.VITE_BASEURL+`/approve_status/${sponsor.id}`,
      {method:'POST',
        headers:{
          "Content-Type": "application/json",
          'Authentication-Token': store.getters.getToken
        },
        body:JSON.stringify({
          approved:status
          
        })
      }).then(
        x => {
          console.log(x)
          return x.json()
          
        }).then(x=>{
         
          sponsor.approved=status;
          console.log(x)
         
        })
      }
  },
  mounted() {
    this.DashboardInfo();
  },
  
  
  



}

</script>