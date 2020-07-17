import axios from 'axios'

const apiClient = axios.create({
  baseURL: 'http://localhost:5000/',
  withCredentials: false, // default
  headers: {
    Accept: 'application/json',
    'Content-Type': 'application/json'
  }
})

export default {
  getOrders() {
    return apiClient.get('/orders')
  },
  getOrderItems() {
    return apiClient.get('/order_items')
  },
  getDeliveries() {
    return apiClient.get('/deliveries')
  },
  getCustomers() {
    return apiClient.get('/customers')
  },
  getCustomersCompanies() {
    return apiClient.get('/customers-companies')
  },
  getOrder(id) {
    return apiClient.get('/orders/' + id)
  }
}
