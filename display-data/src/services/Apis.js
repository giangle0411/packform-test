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
  }
}
