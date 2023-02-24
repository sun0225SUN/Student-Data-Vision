/* eslint-disable vue/valid-template-root */
// 针对/starpage路由显示
// 在这个组件中，通过子组件注册的方式显示Seller.vue组件

<template>
    <div class="com-page">
        <star></star>
    </div>
</template>

<script>
import Star from '@/components/Star'

export default {
  data () {
    return {}
  },
  methods: {},
  components: {
    star: Star
  }
}
</script>

<style lang="less" scoped>

</style>
