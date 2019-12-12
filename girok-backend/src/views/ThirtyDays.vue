<template>
  <div>
    <h1>Last Thirty Days</h1>
    <CalendarHeatmap :lastdays="lastdays"/>
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
  },
  data: function () {
    return {
      lastdays : [
        {id: 1, rate:100},
        {id: 2, rate:66},
        {id: 3, rate:33},
        {id: 4, rate:22},
        {id: 5, rate:50},
        {id: 6, rate:70},
        {id: 7, rate:80},
        {id: 8, rate:90},
        {id: 9, rate:50},
        {id: 10, rate:35},
        {id: 11, rate:100},
        {id: 12, rate:66},
        {id: 13, rate:33},
        {id: 14, rate:22},
        {id: 15, rate:50},
        {id: 16, rate:70},
        {id: 17, rate:80},
        {id: 18, rate:90},
        {id: 19, rate:50},
        {id: 20, rate:35},
        {id: 21, rate:33},
        {id: 22, rate:22},
        {id: 23, rate:50},
        {id: 24, rate:70},
        {id: 25, rate:80},
        {id: 26, rate:90},
        {id: 27, rate:50},
        {id: 28, rate:35},
      ]
    }
  }
}
</script>