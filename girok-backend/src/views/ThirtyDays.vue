<template>
  <div>
    <h1>Last Thirty Days</h1>
    <CalendarHeatmap :lastdays="lastdays"/>
    <div>
      <h4>recent top3 #tag</h4>
      <p>{{ sortedTags[0][2]}} ({{ sortedTags[0][1] }}/{{ totalTagCnt }})</p>
      <p>{{ sortedTags[1][2]}} ({{ sortedTags[1][1] }}/{{ totalTagCnt }})</p>
      <p>{{ sortedTags[2][2]}} ({{ sortedTags[2][1] }}/{{ totalTagCnt }})</p>
    </div>
  </div>
</template>

<script>
// @ is an apas to /src
import CalendarHeatmap from '@/components/CalendarHeatmap.vue'

export default {
  name: 'thirtydays',
  components: {
    CalendarHeatmap
  },
  data: function () {
    return {
      lastdays : [
        {id: 1, rate:100, hashtags:[1, 2, 3]},
        {id: 2, rate:66, hashtags: [5, 6, 7]},
        {id: 3, rate:33, hashtags: [3]},
        {id: 4, rate:22, hashtags: [2]},
        {id: 5, rate:50, hashtags: [3]},
        {id: 6, rate:70, hashtags: [1, 3]},
        {id: 7, rate:80, hashtags: [1, 3]},
        {id: 8, rate:90, hashtags: [1, 3]},
        {id: 9, rate:50, hashtags: [5, 6, 7]},
        {id: 10, rate:35, hashtags: [5, 6, 7]},
        {id: 11, rate:100, hashtags: [5, 6, 7]},
        {id: 12, rate:66, hashtags: [6]},
        {id: 13, rate:33, hashtags: [6]},
        {id: 14, rate:22, hashtags: [6]},
        {id: 15, rate:50, hashtags: [6]},
        {id: 16, rate:70, hashtags: [6]},
        {id: 17, rate:80, hashtags: [7]},
        {id: 18, rate:90, hashtags: [7]},
        {id: 19, rate:50, hashtags: [11]},
        {id: 20, rate:35, hashtags: [13]},
        {id: 21, rate:33, hashtags: [15]},
        {id: 22, rate:22, hashtags: [3]},
        {id: 23, rate:50, hashtags: [3]},
        {id: 24, rate:70, hashtags: [3]},
        {id: 25, rate:80, hashtags: [1]},
        {id: 26, rate:90, hashtags: [1]},
        {id: 27, rate:50, hashtags: [1]},
        {id: 28, rate:35, hashtags: [1]}
      ],
      hashtags: [
        {id:1, content:'dinner'},
        {id:2, content:'roomescape'},
        {id:3, content:'Girok'},
        {id:4, content:'YD'},
        {id:5, content:'ML'},
        {id:6, content:'HYBus'},
        {id:7, content:'party'},
        {id:11, content:'drinking'},
        {id:13, content:'happy'},
        {id:15, content:'newyear'}
      ],
      totalTagCnt: 0,
      sortedTags: []
    }
  },
  methods: {
    getTopTags() {
      const tagRank = {}
      this.lastdays.forEach(day => {
        day.hashtags.forEach(t => {
          this.totalTagCnt += 1
          if (t in tagRank) {
            tagRank[`${t}`] += 1
          } else {
            tagRank[`${t}`] = 1
          }
        })
      })
      let entries = Object.entries(tagRank)
      this.sortedTags = entries.sort((a, b) => b[1] - a[1])
      this.sortedTags.forEach( tArray => {
        tArray.push(this.hashtags.find(t => t.id == tArray[0]).content)
      })
    }
  },
  mounted() {
    this.getTopTags()
  }
}
</script>