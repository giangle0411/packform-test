<template>
  <div class="container">
    <div class="search">
      <div class="search-label"><h2>Search:</h2></div>
      <span><input class="form-control" v-model="filters.name.value"/></span>
    </div>

    <div>
      <datepicker v-model="filters.date.value.min" placeholder="Start date" />
      <datepicker v-model="filters.date.value.max" placeholder="End date" />
    </div>

    <v-table
      :data="this.$store.state.order.orders"
      :filters="filters"
      :currentPage.sync="currentPage"
      :pageSize="5"
      @totalPagesChanged="totalPages = $event"
      class="table table-striped table-borderes"
    >
      <thead slot="head">
        <tr>
          <th>Order Name</th>
          <th>Customer Name</th>
          <th>Customer Company</th>
          <v-th :customSort="dateSort">Order date</v-th>
          <th>Delivered Amount</th>
          <th>Total Amount</th>
          <th></th>
        </tr>
      </thead>
      <tbody slot="body" slot-scope="{ displayData }">
        <tr v-for="row in displayData" :key="row.id">
          <td>{{ row.order_name }}</td>
          <td>{{ row.customer.name }}</td>
          <td>{{ row.customer.company.company_name }}</td>
          <td>{{ row.created_at | date }}</td>
          <td></td>
          <td></td>
        </tr>
      </tbody>
    </v-table>
    <smart-pagination
      :currentPage.sync="currentPage"
      :totalPages="totalPages"
    />
  </div>
</template>

<script>
import store from '@/store'
import { mapState } from 'vuex'
import Datepicker from 'vuejs-datepicker'
export default {
  components: {
    Datepicker
  },
  data() {
    return {
      filters: {
        name: {
          value: '',
          keys: [
            'customer.name',
            'order_name',
            'customer.company.company_name',
            'created_at'
          ]
        },
        date: { value: { min: '', max: '' }, custom: this.dateFilter }
      },
      currentPage: 1,
      totalPages: 0,
      startDate: '',
      endDate: ''
    }
  },
  created() {
    store.dispatch('order/fetchOrders')
  },
  methods: {
    dateSort(a, b) {
      let date1 = new Date(a.created_at).getTime()
      let date2 = new Date(b.created_at).getTime()

      return date1 - date2
    }
    // dateFilter(filterValue, row) {
    //   let date = new Date(row.created_at).getTime()
    //   let minDate = new Date(filterValue.min).getTime()
    //   let maxDate = new Date(filterValue.max).getTime()
    //   return date >= minDate && date <= maxDate
    // }
  },
  computed: {
    ...mapState(['order']),
    filteredEntries() {
      return this.$store.state.order.orders.filter(order => {
        if (this.startDate <= order.created_at <= this.endDate) {
          return order.created_at
        }
        return
        //check if the entry is between the selected dated
      })
    }
  }
}
</script>

<style>
.search-label {
  float: left;
}

.search {
  white-space: nowrap;
  margin-bottom: 10px;
}
</style>
