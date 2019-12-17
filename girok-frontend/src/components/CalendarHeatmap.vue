<template>
  <div>
    <h2>calendarHeatmap</h2>
    <div id="container">
      <div class="box" :id="day.id" v-for="day in lastdays" :key="day.id"></div>
    </div>
	</div>
</template>

<script>
import Rainbow from '../rainbowvis'


export default {
  name: 'CalendarHeatmap',
  props: {
    lastdays: {
      type: Array
    }
  },
  methods: {
    giveHeat() {
      let rainbow = new Rainbow()
      rainbow.setSpectrum('grey', 'indianred')
      for (let i=0; i <= 27; i++) {
        let ii = this.lastdays[i].id
        let r = this.lastdays[i].rate
        document.getElementById(`${ii}`).style.backgroundColor  = '#'+rainbow.colourAt(r)
      }
    }
  },
  mounted () {
    this.giveHeat()
  }
}
</script>

<style scoped>
  #container {
    height: 40vh;
    width: 35vw;
    margin: auto;
    display: flex;
    flex-wrap: wrap;
  }

  .box {
    height: 8vh;
    width: 4vw;
    margin: 1vh 0.5vw;
  }

</style>