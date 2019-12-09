import Vue from 'vue'
import VueRouter from 'vue-router'
import Today from '../views/Today.vue'
import ThirtyDays from '../views/ThirtyDays.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/today',
    name: 'today',
    component: Today
  },
  {
    path: '/thirtydays',
    name: 'thirtydays',
    component: ThirtyDays
  }
]

const router = new VueRouter({
  routes
})

export default router
