/* eslint-disable vue/valid-template-root */
// 针对/starpage路由显示
// 在这个组件中，通过子组件注册的方式显示Seller.vue组件

<template>
    <div class="com-page">
        <province2></province2>
    </div>
</template>

<script>
import Province2 from '@/components/Province2'

export default {
  data () {
    return {}
  },
  methods: {},
  components: {
    province2: Province2
  }
}
</script>

<style lang="less" scoped>

</style>
