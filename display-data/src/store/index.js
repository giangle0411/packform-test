import Vue from 'vue'
import Vuex from 'vuex'
import * as order from '@/store/modules/order.js'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: { order }
})
