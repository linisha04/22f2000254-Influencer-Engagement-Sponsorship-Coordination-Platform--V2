<script setup>
import Navbar from '@/components/Navbar.vue'
import router from '@/router';
import { RouterLink } from 'vue-router';
import store from '@/store';

</script>

<template>
<Navbar /> 


<div class="container mt-5">
        <div class="card mx-auto" style="width: 45rem;">
            <div class="card-body">
                <h5 class="card-title">Sponsor Register</h5>
                <form @submit.prevent="sponsorRegister">
                    <div class="row mb-3">
                        <label for="name" class="col-sm-2 col-form-label">Name</label>
                        <div class="col-sm-10">
                            <input type="text" class="form-control" id="name" v-model="username">
                        </div>
                    </div>
                    <div class="row mb-3">
                        <label for="email" class="col-sm-2 col-form-label">Email</label>
                        <div class="col-sm-10">
                            <input type="email" class="form-control" id="email" v-model="email"> 
                        </div>
                    </div>
                    <div class="row mb-3">
                        <label for="password" class="col-sm-2 col-form-label">Password</label>
                        <div class="col-sm-10">
                            <input type="password" class="form-control" id="password" v-model="password">
                        </div>
                    </div>
                    <fieldset class="row mb-3">
                        <legend class="col-form-label col-sm-2 pt-0">Industry</legend>
                        <div class="col-sm-10">
                            <div class="form-check">
                                <input class="form-check-input" type="radio" name="industry" id="Fashion&Beauty&Lifestyle"
                                    value="Fashion&Beauty&Lifestyle" v-model="industry">
                                <label class="form-check-label" for="Fashion&Beauty&Lifestyle">
                                    Fashion & Beauty & Lifestyle
                                </label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input" type="radio" name="industry" id="Health&Wellness"
                                    value="Health&Wellness" v-model="industry">
                                <label class="form-check-label" for="Health&Wellness">
                                    Health & Wellness
                                </label>
                            </div>
                            <div class="form-check ">
                                <input class="form-check-input" type="radio" name="industry" id="Travel&Adventure"
                                    value="Travel&Adventure" v-model="industry">
                                <label class="form-check-label" for="Travel&Adventure">
                                    Travel & Adventure
                                </label>
                            </div>
                            <div class="form-check ">
                                <input class="form-check-input" type="radio" name="industry" id="Tech&Gaming"
                                    value="Tech&Gaming" v-model="industry">
                                <label class="form-check-label" for="Tech&Gaming">
                                    Tech & Gaming
                                </label>
                            </div>

                            <div class="form-check ">
                                <input class="form-check-input" type="radio" name="industry" id="Food&Cooking&Lifestyle"
                                    value="Food&Cooking&Lifestyle" v-model="industry">
                                <label class="form-check-label" for="Food&Cooking&Lifestyle">
                                    Food & Cooking & Lifestyle
                                </label>
                            </div>

                            <div class="form-check ">
                                <input class="form-check-input" type="radio" name="industry" id="Education&Learning"
                                    value="Education&Learning" v-model="industry">
                                <label class="form-check-label" for="Education&Learning">
                                    Education & Learning
                                </label>
                            </div>
                        </div>
                    </fieldset>

                    <button type="submit" class="btn btn-primary"> Sponsor Register </button>
                </form>


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
            email:null,
            industry:null
        }
    },
    methods:{
        validate(){

            let valid=true;
            if (!this.username ){
                valid=false;
                alert("Please enter valid username or length must be greater than 4.");
               
            }
            if (!this.industry){
                valid=false;
                alert("Please enter the industry.");
            }
            // if (!this.password.length>3 ){
            //     valid=false;
            //     alert("Please enter the correct password length.");
            // }
            if (!email){
                valid=false;
                alert("Please enter the email");
            }
            if(!password){
                valid=false;
                alert("Please enter the passord and length should be greater than 4")
            }
            

            
            console.log(this.username , this.password , this.email , this.industry)

            return valid


        },
        sponsorRegister(){
            if(!this.validate()){
                return;
            }

            fetch(import.meta.env.VITE_BASEURL+"/sponsorRegister"  ,
                 {method : "POST" , headers:{"Content-Type" : "application/json"},
                 body: JSON.stringify({username: this.username, password: this.password , email:this.email , industry: this.industry})
                }).then(resp => {
                    return [resp.json() , resp.status]
                }).then(x=>{
                    if(x[1] == 200){
                        return x[0]
                    }else if(x[1] == 409){
                        this.alert(" username exists")
                    }
                    console.log(this.username , this.password )
                    return {}
                }).then(
                    x =>{
                        console.log(this.username , this.password , this.email , this.industry)
                        if (x["message"]=="Check Username"){
                            alert("Check Username");
                        }else if(x["message"]=="Check password"){
                            alert("Check password");
                        }else if(x["message"]=="Check email"){
                            alert("Check email");
                        }else if(x["message"]=="Check industry"){
                            alert("Check industry");
                        }else{
                            router.push({name:"loginView"})
                        }
                    })
            
        }
    }
       
    }
</script>
<style scoped></style>