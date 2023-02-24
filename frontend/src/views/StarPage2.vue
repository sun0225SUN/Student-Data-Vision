/* eslint-disable vue/valid-template-root */
// 针对/starpage路由显示
// 在这个组件中，通过子组件注册的方式显示Seller.vue组件

<template>
    <div class="com-page">
        <star2></star2>
    </div>
</template>

<script>
import Star2 from '@/components/Star2'

export default {
  data () {
    return {}
  },
  methods: {},
  components: {
    star2: Star2
  }
}
</script>

<style lang="less" scoped>

</style>
