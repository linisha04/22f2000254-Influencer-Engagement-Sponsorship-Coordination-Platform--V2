<script setup>
import store from '@/store';
import router from "@/router";
import { RouterView } from "vue-router";

</script>
<template>


<br>
<br>

<table class="table  table-striped-columns  ">
    <thead>
      <tr>
        <th scope="col" class="table-light"> Campaign Id</th>
        <th scope="col" class="table-light">Created by</th>

        <th scope="col" class="table-light">Campaign Name</th>
        <th scope="col" class="table-light">Visibility</th>
        <th scope="col" class="table-light">Budget In Rupees</th>
        <th scope="col" class="table-light">Niche</th>
        <th scope="col" class="table-light">Goals</th>
          <th scope="col" class="table-light">
       
        

         </th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="camp in allCampaigns" :key="camp.id">
       
        <td class="table-warning">{{ camp['id'] }}</td>
        <td class="table-warning">{{ camp['sponsorName'] }}</td>

        <td class="table-warning">{{ camp['campaignName'] }}</td>
        <td class="table-warning"> {{ camp['visibility'] }}</td>
        <td class="table-warning">{{ camp['budget'] }}</td>
        <td class="table-warning">{{ camp['niche'] }}</td>
        <td class="table-warning">{{ camp['goals'] }}</td>
           

      </tr>
    </tbody>
  </table>


</template>

<script>
export default {

    data(){
        return{
            allCampaigns:[]
        }
    },
    methods:{
       

        getAllCamps(){
            fetch(import.meta.env.VITE_BASEURL+"/viewCampaign",{
                method:'GET',
                headers:{
                    "Content-Type": "application/json",
                    "Authentication-Token": store.getters.getToken

                },

            }).then((x=>{
                return x.json()
            })) .then(data => {
               
        this.allCampaigns = data;
       
      })
        }
    },
    mounted() {

this.getAllCamps();
}

}

</script>
