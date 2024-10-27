<script>
import { RouterLink } from 'vue-router';

</script>


<template>

<nav class="navbar navbar-expand-md bg-primary-subtle  fixed-top">
  <div class="container-fluid">
    <a class="navbar-brand" ISCP>Navbar</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item">
          <RouterLink class="nav-link active" aria-current="page" to="/">Home</RouterLink>
        </li>
        <li class="nav-item">
          <RouterLink class="nav-link" to="/signin">Login</RouterLink>
        </li>
        <li class="nav-item">
          <RouterLink class="nav-link" to="/influencerRegister">Infuencer Register</RouterLink>
        </li>
        <li class="nav-item">
          <RouterLink class="nav-link " to="/sponsorRegister">Sponsor Register</RouterLink>
        </li>
      </ul>
    </div>
  </div>
</nav>

</template>

<style>

</style>


