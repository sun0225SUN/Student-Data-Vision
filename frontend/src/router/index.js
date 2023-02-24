import Vue from 'vue'
import VueRouter from 'vue-router'

import StarPage from '@/views/StarPage1'
import StarPage2 from '@/views/StarPage2'
import SexPage from '@/views/SexPage'
import GeoPage from '@/views/GeoPage1'
import GeoPage2 from '@/views/GeoPage2'
import ProvincePage1 from '@/views/ProvincePage1'
import ProvincePage2 from '@/views/ProvincePage2'

import StarGroup from '@/views/StarGroup'
import ProvinceGroup from '@/views/ProvinceGroup'

Vue.use(VueRouter)

const routes = [
  {
    path: '/star1',
    component: StarPage
  },
  {
    path: '/star2',
    component: StarPage2
  },
  {
    path: '/sex',
    component: SexPage
  },
  {
    path: '/map1',
    component: GeoPage
  },
  {
    path: '/map2',
    component: GeoPage2
  },
  {
    path: '/province1',
    component: ProvincePage1
  },
  {
    path: '/province2',
    component: ProvincePage2
  },
  {
    path: '/stargroup',
    component: StarGroup
  },
  {
    path: '/provincegroup',
    component: ProvinceGroup
  }
]

const router = new VueRouter({
  routes
})

export default router
