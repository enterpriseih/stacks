import Vue from 'vue'
import Vuex from 'vuex'
import App from './App'
import router from './router'
import store from './store'
import './directive'

Vue.config.productionTip = false
Vue.use(Vuex)

// import BaiduMap from 'vue-baidu-map'
// Vue.use(BaiduMap, {
//   ak: '',
// })

// import ElementUI from 'element-ui'
// import locale from 'element-ui/lib/locale/lang/en'
// Vue.use(ElementUI, {
//   locale
// })

new Vue({
  el: '#app',
  router,
  store,
  components: {
    App
  },
  template: '<App/>'
})
