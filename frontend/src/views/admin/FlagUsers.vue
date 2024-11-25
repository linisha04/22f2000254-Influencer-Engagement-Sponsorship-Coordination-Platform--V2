<script setup>
import store from '@/store';
import router from "@/router";
</script>
<template>
  
   <br>
   <br>
<table class="table  table-striped-columns " >
       <thead>
       <tr class="table-info">
        <th scope="col">Id</th>
         <th scope="col">Username</th>
         <th scope="col">Email</th>
         <th scope="col">Role</th>
         <th scope="col">Is Active</th>
         <th scope="col">Flagged  </th>
        
         
        
       </tr>
     </thead>
     <tbody>
       <tr v-for="user in allUser" :key="user.id" class="table-success">
         <!-- <th scope="row">1</th> -->
         <td>{{ user.id }}</td>
         <td>{{ user.username }}</td>
         <td>{{ user.email }}</td>
         <td>{{ user.role[0] }}</td>
         <td>{{ user.active }}</td>
  
         <!-- <td>{{ i.flagged }}</td> -->
          <td>
         <button  @click="changeFlag(user)">{{ user.flagged ? ' Unflag' : 'Flagged' }}</button></td>

       </tr>
     </tbody>
   </table>


</template>

<script>
export default {

    data(){
        return{
            allUser:[]
        }
    },
    methods:{

        getAllUsers(){
            fetch(import.meta.env.VITE_BASEURL+"/allUsers",{
                method:'GET',
                headers:{
                    "Content-Type": "application/json",
                    "Authentication-Token": store.getters.getToken

                },

            }).then((x=>{
                return x.json()
            })) .then(data => {
               
        this.allUser = data;
       
      })
        },

        changeFlag(user){
      if (!user) {
    console.error('user is not there');
    return;
  }
      console.log(user)
     const status=!user.flagged;
     fetch(import.meta.env.VITE_BASEURL+`/changeFlag/${user.id}`,
      {method:'POST',
        headers:{
          "Content-Type": "application/json",
          'Authentication-Token': store.getters.getToken
        },
        body:JSON.stringify({
          flagged:status
          
        })
      }).then(
        x => {
          console.log(x)
          return x.json()
          
        }).then(x=>{
         
          user.flagged=status;
          console.log(x)
         
        })
      }
    },
    mounted() {

this.getAllUsers();
}

}

</script>
