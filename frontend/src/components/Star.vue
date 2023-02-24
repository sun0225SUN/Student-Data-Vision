// 星座信息饼图展示页面
<template>
    <div class="com-container">
        <div id="com-chart"></div>
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
      this.chartInstance = this.$echarts.init(document.getElementById('com-chart'))
    },
    // 获取服务器数据
    async getData () {
      // 地址，http：127.0.0.1/api/seller
      const { data: ret } = await this.$http.get('star')

      this.allData = ret
      // console.log(this.allData)
      this.updateChart()
    },
    // 更新图标
    updateChart () {
      const option = {
        // backgroundColor: '#000E1A',
        textStyle: {
          fontSize: 20
        },
        title: {
          text: '班级学生星座饼图分析',
          subtext: '安理地信19-1',
          left: 'center',
          textStyle: {
            fontSize: 36
          },
          subtextStyle: {
            fontSize: 25
          }
        },
        color: ['#c23531', '#2f4554', '#61a0a8', '#d48265', '#91c7ae', '#749f83', '#ca8622', '#bda29a', '#6e7074', '#546570', '#c4ccd3', '#ffc1e3'],
        tooltip: {
          trigger: 'item'
          // textStyle: {
          //   fontSize: 20
          // }
        },
        legend: {
          orient: 'vertical',
          left: 'left'
        },
        series: [
          {
            name: '',
            type: 'pie',
            radius: '50%',
            data: this.allData,
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: 'rgba(0, 0, 0, 0.5)'
              }
            }
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
