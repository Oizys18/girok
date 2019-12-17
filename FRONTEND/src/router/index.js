import Vue from 'vue'
import VueRouter from 'vue-router'
import Today from '../views/Today.vue'
import Authentication from '../views/Authentication.vue'
import PageNotFound from '../views/PageNotFound.vue'
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
  },
  {
    path: '/authentication',
    name: 'authentication',
    component: Authentication
  },
  {
    path: '*',
    name: 'PageNotFound',
    component: PageNotFound
  },
]

const router = new VueRouter({
  mode: 'history',
  routes
})

export default router
