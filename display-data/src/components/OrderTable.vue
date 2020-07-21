<template>
  <div>
    <v-table
      :data="filteredData"
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
        </tr>
      </thead>
      <tbody slot="body" slot-scope="{ displayData }">
        <tr v-for="row in displayData" :key="row.id">
          <td>{{ row.order_name }}</td>
          <td>{{ row.customer.name }}</td>
          <td>{{ row.customer.company.company_name }}</td>
          <td>{{ row.created_at | date }}</td>
          <td>{{ deliveried_amount(row) | currency }}</td>
          <td>{{ total_amount(row) | currency }}</td>
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
import _ from 'lodash'
export default {
  props: {
    orders: Array,
    startDate: Date,
    endDate: Date,
    searchValue: String
  },
  data() {
    return {
      filters: {
        search: {
          value: this.searchValue,
          keys: [
            'customer.name',
            'order_name',
            'customer.company.company_name',
            'created_at'
          ]
        }
      },
      currentPage: 1,
      totalPages: 0
    }
  },
  methods: {
    dateSort(a, b) {
      let date1 = new Date(a.created_at).getTime()
      let date2 = new Date(b.created_at).getTime()

      return date1 - date2
    },
    deliveried_amount(order) {
      let total = 0
      let order_items = order.order_items
      for (var i = 0; i < order_items.length; i++) {
        let deliveried = order_items[i].deliveries
        for (var j = 0; j < deliveried.length; j++) {
          total +=
            deliveried[j].delivered_quantity * order_items[i].price_per_unit
        }
      }
      if (total) {
        return total
      }
      return '-'
    },
    total_amount(order) {
      let total = 0
      let order_items = order.order_items
      for (var i = 0; i < order_items.length; i++) {
        total += order_items[i].quantity * order_items[i].price_per_unit
      }
      if (total) {
        return total
      }
      return '-'
    }
  },
  computed: {
    filteredData() {
      let startDate = new Date(this.startDate).getTime()
      let endDate = new Date(this.endDate).getTime()
      let data = this.orders

      return _.filter(data, function(val) {
        let currDate = new Date(val.created_at).getTime()

        if (_.isNull(startDate) && _.isNull(endDate)) {
          return true
        } else if (currDate <= endDate && currDate >= startDate) {
          return val
        }
      })
    }
  },
  watch: {
    searchValue: function(value) {
      this.filters.search.value = value
    }
  }
}
</script>

<style lang="scss" scoped></style>
