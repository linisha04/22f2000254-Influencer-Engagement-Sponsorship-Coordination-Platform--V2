<script setup>
import Navbar from "@/components/Navbar.vue";
import store from "@/store";
import { RouterLink } from "vue-router";
import router from '@/router';

</script>

<template>
    <Navbar />
    <div  >

<div class="container mt-5">
    <div class="card mx-auto" style="width: 45rem ; ">
        <div class="card-body">
            <h5 class="card-title">Login</h5>
            <form @submit.prevent="login()">
                <div class="row mb-3">
                    <label for="name" class="col-sm-2 col-form-label"> Name</label>
                    <div class="col-sm-10">
                        <input type="text" class="form-control" id="name" v-model="username"  autocomplete="username">
                    </div>
                </div>
                <div class="row mb-3">
                    <label for="password" class="col-sm-2 col-form-label">Password</label>
                    <div class="col-sm-10">
                        <input type="password" class="form-control" id="password" v-model="password"  autocomplete="password">
                    </div>
                </div>
                <!-- <fieldset class="row mb-3">
                    <legend class="col-form-label col-sm-2 pt-0">Role</legend>
                    <div class="col-sm-10">
                        <div class="form-check">
                            <input class="form-check-input" type="radio" name="role" id="sponsor"  value="sponsor" v-model="role">
                            <label class="form-check-label" for="sponsor">Sponsor </label>
                        </div>
                        <div class="form-check">
                            <input class="form-check-input" type="radio" name="role" id="influencer" value="influencer" v-model="role">
                               <label class="form-check-label" for="influencer">  Influencer </label> 
                        </div>
                        <div class="form-check ">
                            <input class="form-check-input" type="radio" name="role" id="admin"  value="admin" v-model="role">   
                            <label class="form-check-label" for="admin">   Admin </label>
                        </div>
                    </div>
                </fieldset> -->

                <button type="submit" class="btn btn-primary"> SignIn </button>
            </form>


        </div>
    </div>
</div>
</div>
</template>

<script>
    export default {
        data(){
        return {
            username:null,
            password:null,
           
        }
    },
    methods:{
        validate(){

            let valid=true;
            if (!this.username || !this.password ){
                valid=false;
                alert("Please enter valid username, password");
            }
            
            console.log(this.username , this.password)

            return valid


        },
        login(){
            if(!this.validate()){
                return;
            }

            fetch(import.meta.env.VITE_BASEURL+"/signin"  ,
                 {method : "POST" , headers:{"Content-Type" : "application/json"},
                 body: JSON.stringify({username: this.username, password: this.password})
                }).then(resp => {
                    return [resp.json() , resp.status]
                }).then(x=>{
                    if(x[1] == 200){
                        return x[0]
                    }else if(x[1] == 404 || x==400){
                        return alert("Invalid username  or password");
                    }
                    return {}
                }).then(
                    x =>{

                        store.commit("setUser" , x);

                       


                        if(x["roles"].includes("sponsor")){
                            router.push({name:"sponsorDashboard"})
                        }else if(x["roles"].includes("influencer")){
                        
                            router.push({name:"influencerDashboard"})
                        }else{
                            
                            router.push({name:"AdminDashboard"})
                        }
                    })
            
        }
    }
       
    }
</script>
<style scoped></style>