<template>
  <div>
    <router-view></router-view>   
  </div>
</template>

<script>
export default {
  name: 'App'
};
</script>

<style>
nav {
  padding: 10px;
  background-color: #f0f0f0;
}

router-link {
  margin: 0 10px;
  text-decoration: none;
  color: #42b983;
}
</style>
