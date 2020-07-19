<template>
  <div class="form-inline">
    <div class="col-md-12 form-group">
      <label class="col-sm-2 col-form-label" for="searchbar"
        ><h2>Search:</h2></label
      >
      <input
        id="searchbar"
        class="form-control col-sm-10"
        @input="$emit('input', $event.target.value)"
      />
    </div>
  </div>
</template>

<script>
export default {}
</script>

<style lang="scss" scoped></style>
