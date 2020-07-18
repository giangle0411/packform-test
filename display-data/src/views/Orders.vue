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
          v-model="filterValue"
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

    <order-table
      :orders="$store.state.order.orders"
      :startDate="startDate"
      :endDate="endDate"
      :filteredValue="filterValue"
    />
  </div>
</template>

<script>
import store from '@/store'
import { mapState } from 'vuex'
import Datepicker from 'vuejs-datepicker'
import OrderTable from '@/components/OrderTable.vue'
import _ from 'lodash'

export default {
  components: {
    Datepicker,
    OrderTable
  },
  data() {
    return {
      filterValue: '',
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
