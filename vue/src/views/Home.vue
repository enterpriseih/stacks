<template>
  <div class="homeWrap" v-loading="loading">
  </div>
</template>

<script>
  import {user} from "../api";
  import {mapGetters, mapMutations} from "vuex";
  export default {
    name: "Home",
    components: {
    },
    data() {
      return {
        loading: false,
      }
    },
    computed:{
    },
    watch: {
    },
    methods: {
      ...mapMutations(["SAVEUSER"]),
      getUser() {
        user.getUser().then(res => {
        }).catch(err => {
        })
      },
    created() {
      this.getUser()
    },
    updated() {
    },
    mounted() {
    },
    activated() {
    },
  };
</script>

<style lang="scss" type="text/scss" scoped>
  @import "../assets/styles/common.scss";
  .homeWrap {
    height: 100%;
  }
</style>
