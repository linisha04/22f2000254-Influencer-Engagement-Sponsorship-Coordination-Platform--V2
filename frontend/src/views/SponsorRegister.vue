<script setup>
import Navbar from '@/components/Navbar.vue'
</script>

<template>
<Navbar /> 


<div class="container mt-5">
        <div class="card mx-auto" style="width: 45rem;">
            <div class="card-body">
                <h5 class="card-title">Sponsor Register</h5>
                <form>
                    <div class="row mb-3">
                        <label for="name" class="col-sm-2 col-form-label">Name</label>
                        <div class="col-sm-10">
                            <input type="text" class="form-control" id="name">
                        </div>
                    </div>
                    <div class="row mb-3">
                        <label for="email" class="col-sm-2 col-form-label">Email</label>
                        <div class="col-sm-10">
                            <input type="email" class="form-control" id="email">
                        </div>
                    </div>
                    <div class="row mb-3">
                        <label for="password" class="col-sm-2 col-form-label">Password</label>
                        <div class="col-sm-10">
                            <input type="password" class="form-control" id="password">
                        </div>
                    </div>
                    <fieldset class="row mb-3">
                        <legend class="col-form-label col-sm-2 pt-0">Industry</legend>
                        <div class="col-sm-10">
                            <div class="form-check">
                                <input class="form-check-input" type="radio" name="industry" id="Fashion&Beauty&Lifestyle"
                                    value="Fashion&Beauty&Lifestyle" checked>
                                <label class="form-check-label" for="Fashion&Beauty&Lifestyle">
                                    Fashion & Beauty & Lifestyle
                                </label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input" type="radio" name="industry" id="Health&Wellness"
                                    value="Health&Wellness">
                                <label class="form-check-label" for="Health&Wellness">
                                    Health & Wellness
                                </label>
                            </div>
                            <div class="form-check ">
                                <input class="form-check-input" type="radio" name="industry" id="Travel&Adventure"
                                    value="Travel&Adventure">
                                <label class="form-check-label" for="Travel&Adventure">
                                    Travel & Adventure
                                </label>
                            </div>
                            <div class="form-check ">
                                <input class="form-check-input" type="radio" name="industry" id="Tech&Gaming"
                                    value="Tech&Gaming">
                                <label class="form-check-label" for="Tech&Gaming">
                                    Tech & Gaming
                                </label>
                            </div>

                            <div class="form-check ">
                                <input class="form-check-input" type="radio" name="industry" id="Food&Cooking&Lifestyle"
                                    value="Food&Cooking&Lifestyle">
                                <label class="form-check-label" for="Food&Cooking&Lifestyle">
                                    Food & Cooking & Lifestyle
                                </label>
                            </div>

                            <div class="form-check ">
                                <input class="form-check-input" type="radio" name="industry" id="Education&Learning"
                                    value="Education&Learning">
                                <label class="form-check-label" for="Education&Learning">
                                    Education & Learning
                                </label>
                            </div>
                        </div>
                    </fieldset>

                    <button type="submit" class="btn btn-primary"> Register </button>
                </form>


            </div>
        </div>
    </div>

</template>
