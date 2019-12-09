<template>
  <div>
    <h1>Last Thirty Days</h1>
    <CalendarHeatmap/>
    <DropdownList/>
  </div>
</template>

<script>
// @ is an alias to /src
import CalendarHeatmap from '@/components/CalendarHeatmap.vue'
import DropdownList from '@/components/DropdownList.vue'

export default {
  name: 'thirtydays',
  components: {
    CalendarHeatmap,
    DropdownList
  }
}
</script>