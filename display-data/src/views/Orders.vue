<template>
  <div class="container">
    <search-bar v-model="searchValue" />

    <date-range
      @emitStartDate="updateStartDate($event)"
      @emitEndDate="updateEndDate($event)"
    />

    <order-table
      :orders="$store.state.order.orders"
      :startDate="startDate"
      :endDate="endDate"
      :searchValue="searchValue"
    />
  </div>
</template>

<script>
import store from '@/store'
import { mapState } from 'vuex'
import OrderTable from '@/components/OrderTable.vue'
import SearchBar from '@/components/SearchBar.vue'
import DateRange from '@/components/DateRange.vue'

export default {
  name: 'Orders',
  components: {
    'order-table': OrderTable,
    'search-bar': SearchBar,
    'date-range': DateRange
  },
  data() {
    return {
      searchValue: '',
      startDate: null,
      endDate: new Date()
    }
  },
  created() {
    store.dispatch('order/fetchOrders')
  },
  methods: {
    updateStartDate(value) {
      this.startDate = value
    },
    updateEndDate(value) {
      this.endDate = value
    }
  },
  computed: {
    ...mapState(['order'])
  }
}
</script>

<style></style>
