<template>
  <div>
    <h5>Created date</h5>
    <form class="form-inline date-range">
      <datepicker
        class="start-date"
        v-model="startDate"
        placeholder="Start date"
        @input="emitStartDate()"
      />
      -
      <datepicker
        class="end-date"
        v-model="endDate"
        @input="emitEndDate()"
        placeholder="End date"
      />
    </form>
  </div>
</template>

<script>
import Datepicker from 'vuejs-datepicker'

export default {
  components: {
    Datepicker
  },
  data() {
    return {
      startDate: null,
      endDate: new Date()
    }
  },
  methods: {
    emitStartDate() {
      this.$emit('emitStartDate', this.startDate)
    },
    emitEndDate() {
      this.$emit('emitEndDate', this.endDate)
    }
  }
}
</script>

<style>
.date-range {
  margin-bottom: 20px;
}

.start-date {
  margin-right: 10px;
}

.end-date {
  margin-left: 10px;
  margin-right: 10px;
}
h5 {
  text-align: left;
  font-size: 20px;
}
</style>
