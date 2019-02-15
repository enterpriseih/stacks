<template>
  <div id="app">
    <transition name="fade" mode="out-in">
      <keep-alive include="Home">
        <router-view></router-view>
      </keep-alive>
    </transition>
  </div>
</template>

<script>
  export default {
    name: 'App',
    data() {
      return {}
    },
    methods: {
    },
    computed: {
    },
    created() {
    },
    updated() {
    },
    mounted() {
    },
  }
</script>

<style lang="scss" scoped>
  #app {
    height: 100%;
  }
</style>
