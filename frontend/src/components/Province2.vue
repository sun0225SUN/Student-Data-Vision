// 星座信息饼图展示页面
<template>
    <div class="com-container">
        <div id="com-chart7" ref="star_ref"></div>
    </div>
</template>

<script>
export default {
  data () {
    return {
      chartInstance: null,
      allData: null // 服务器返回的数据
    }
  },
  mounted () {
    this.initChart()
    this.getData()
  },
  methods: {
    // 初始化echarts实例对象
    initChart () {
      this.chartInstance = this.$echarts.init(document.getElementById('com-chart7'))
    },
    // 获取服务器数据
    async getData () {
      // 地址，http：127.0.0.1/api/seller
      const { data: ret } = await this.$http.get('province')

      this.allData = ret
      // console.log(this.allData)
      this.updateChart()
    },
    // 更新图表
    updateChart () {
      const starNames = this.allData.map((item) => {
        return item.name
      })
      const starValues = this.allData.map((item) => {
        return item.value
      })
      const option = {
        textStyle: {
          fontSize: 18
        },
        title: {
          text: '星座柱状图分析',
          textStyle: {
            fontSize: 25
          }
        },
        tooltip: {},
        legend: {
          data: ['销量']
        },
        xAxis: {
          data: starNames,
          axisLabel: {
            fontSize: 20
          }
        },
        yAxis: {
          interval: 1
        },
        series: [
          {
            name: '',
            type: 'bar',
            data: starValues
          }
        ]
      }
      this.chartInstance.setOption(option)
    }
  }
}
</script>

<style lang="less" scoped>

</style>
