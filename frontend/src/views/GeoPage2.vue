/* eslint-disable vue/valid-template-root */
// 针对/starpage路由显示
// 在这个组件中，通过子组件注册的方式显示Seller.vue组件

<template>
    <div class="com-page">
        <geo2></geo2>
    </div>
</template>

<script>
import Geo2 from '@/components/Geo2'

export default {
  data () {
    return {}
  },
  methods: {},
  components: {
    geo2: Geo2
  }
}
</script>

<style lang="less" scoped>

</style>
