import Apis from '@/services/Apis.js'

export const namespaced = true

export const state = {
  orders: []
}

export const mutations = {
  SET_ORDERS(state, orders) {
    state.orders = orders
  }
}

export const actions = {
  fetchOrders({ commit }) {
    return Apis.getOrders().then(response => {
      commit('SET_ORDERS', response.data)
    })
  }
}
