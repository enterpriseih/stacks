<template>
  <div class="wrap">
    <el-menu class="menu" default-active="1">
      <el-submenu index="1">
        <template slot="title">
          <i class="el-icon-location"></i>
          <span>定位</span>
        </template>
        <el-menu-item index="1-1">
          <el-input v-model="zoom"><span slot="prepend">全局比例</span></el-input>
        </el-menu-item>
        <el-menu-item index="1-2">
          <el-input v-model="center.lng"><span slot="prepend">中心点经度</span></el-input>
        </el-menu-item>
        <el-menu-item index="1-3">
          <el-input v-model="center.lat"><span slot="prepend">中心点纬度</span></el-input>
        </el-menu-item>
        <el-menu-item index="1-4">
          <el-switch v-model="showCenter" active-color="#000000" inactive-color="#dcdcdc" active-text="显示中心点"></el-switch>
        </el-menu-item>
      </el-submenu>
    </el-menu>
    <!--  -->
    <baidu-map
      class="map"
      :center="center"
      :zoom="zoom"
      :minZoom = "5"
      :maxZoom = "20"
      :scroll-wheel-zoom = "true"
      @ready="handler"
      @moving="syncCenterAndZoom"
      @moveend="syncCenterAndZoom"
      @zoomend="syncCenterAndZoom"
      >
      <bm-marker v-if="showCenter" :position="center" :dragging="false" animation="BMAP_ANIMATION_BOUNCE"></bm-marker>
      <bm-city-list anchor="BMAP_ANCHOR_TOP_LEFT"></bm-city-list>
      <bm-navigation anchor="BMAP_ANCHOR_TOP_RIGHT"></bm-navigation>
      <bm-overview-map anchor="BMAP_ANCHOR_BOTTOM_RIGHT" :isOpen="true"></bm-overview-map>
    </baidu-map>
  </div>
</template>

<script>
export default {
  name: "bmap",
  data() {
    return {
      center: {
        lng: null,
        lat: null
      },
      zoom: null,
      showCenter: false
    };
  },
  methods: {
    handler({ BMap, map }) {
      this.center.lng = 116.404;
      this.center.lat = 39.915;
      this.zoom = 15;
    },
    syncCenterAndZoom(e) {
      const { lng, lat } = e.target.getCenter();
      this.center.lng = lng;
      this.center.lat = lat;
      this.zoom = e.target.getZoom();
    }
  }
};
</script>

<style lang='scss'>
.wrap {
  height: 100%;
  overflow-y: hidden;
  .map {
    height: 100%;
    z-index: 0;
  }
}
</style>
