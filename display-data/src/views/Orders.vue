<template>
  <div class="container">
    <div class="form-inline">
      <div class="col-md-12 form-group">
        <label class="col-sm-2 col-form-label" for="searchbar"
          ><h2>Search:</h2></label
        >
        <input
          id="searchbar"
          class="form-control col-sm-10"
          v-model="filters.name.value"
        />
      </div>
    </div>

    <form class="form-inline date-range">
      <datepicker
        class="start-date"
        v-model="startDate"
        placeholder="Start date"
      />
      -
      <datepicker class="end-date" v-model="endDate" placeholder="End date" />
    </form>

    <v-table
      :data="filteredDate"
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
import _ from 'lodash'

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
      startDate: null,
      endDate: new Date()
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
    filteredDate() {
      let startDate = new Date(this.startDate).getTime()
      let endDate = this.endDate.getTime()
      let data = this.$store.state.order.orders

      return _.filter(data, function(val) {
        let currDate = new Date(val.created_at).getTime()

        if (_.isNull(startDate) && _.isNull(endDate)) {
          return true
        } else if (currDate <= endDate && currDate >= startDate) {
          return val
        }
      })
    }
  }
}
</script>

<style>
.form-label {
  margin-right: 10px;
}

.date-range {
  margin-bottom: 20px;
  margin-top: 10px;
}

.start-date {
  margin-right: 10px;
}

.end-date {
  margin-left: 10px;
  margin-right: 10px;
}
</style>
