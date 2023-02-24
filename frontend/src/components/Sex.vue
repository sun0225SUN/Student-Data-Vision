// 男女比例
<template>
    <div class="com-container">
        <div id="com-chart3"></div>
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
      this.chartInstance = this.$echarts.init(document.getElementById('com-chart3'))
    },
    // 获取服务器数据
    async getData () {
      // 地址，http：127.0.0.1/api/seller
      const { data: ret } = await this.$http.get('sex')

      this.allData = ret
      // console.log(this.allData)
      this.updateChart()
    },
    // 更新图标
    updateChart () {
      const sexValues = this.allData.map((item) => {
        return item.value
      })
      var getxb1 = sexValues[0] // 男生人数
      var getxb2 = sexValues[1] // 女生人数

      const option = {
        title: {
          show: true,
          left: '45%',
          bottom: '25%',
          text: '地信19-1男女比例',
          textAlign: 'center',
          textStyle: {
            fontWeight: '600',
            fontSize: '28',
            color: '#000'
          }
        },
        tooltip: {
          show: true
        },
        // legend: {
        //     orient: 'vertical',
        //     left: 'bottom',
        //     // data: xbzb,
        // },
        series: [
          {
            name: '',
            type: 'pie',
            radius: ['55%', '115%'],
            startAngle: 180,
            center: ['45%', '83%'],
            roseType: 'radius',
            labelLine: {
              show: false
              // normal: {
              //     length: 20,
              //     length2: 0,
              //     lineStyle: {
              //         color: '#C8C8C8'
              //     }
              // }
            },
            label: {
              normal: {
                show: true,
                position: 'center',
                textStyle: {
                  fontSize: '12px',
                  padding: [-20, 0, 0, 0]
                },
                // formatter: ['{c}'].join('\n'),
                // formatter: ['{c}'] + ' : '['{}'],
                formatter: function (params) {
                  var proportion = ''
                  for (var i = 0; i < option.series[0].data.length - 1; i++) {
                    // console.log(option.series[0].data);
                    if (i === 0) {
                      proportion = proportion + option.series[0].data[i].value.toString()
                    } else {
                      proportion = proportion + ' : ' + option.series[0].data[i].value.toString()
                    }
                  }
                  return proportion
                }
              },
              position: 'center',
              show: true
            },
            data: [
              {
                value: getxb1,
                name: '男生',
                itemStyle: {
                  normal: {
                    // eslint-disable-next-line no-undef
                    color: new echarts.graphic.LinearGradient(
                      0,
                      0,
                      0,
                      1,
                      [
                        {
                          offset: 0,
                          color: '#4C8DFA'
                        },
                        {
                          offset: 1,
                          color: '#5CCFFF'
                        }
                      ],
                      false
                    )
                  }
                }
              },
              {
                value: getxb2,
                name: '女生',
                itemStyle: {
                  normal: {
                    // eslint-disable-next-line no-undef
                    color: new echarts.graphic.LinearGradient(
                      0,
                      0,
                      0,
                      1,
                      [
                        {
                          offset: 0,
                          color: '#FFD18B'
                        },
                        {
                          offset: 1,
                          color: '#FDAD59'
                        }
                      ],
                      false
                    )
                  }
                }
              },
              {
                value: getxb1 + getxb2,
                name: '',
                label: {
                  show: false
                },
                labelLine: {
                  show: false
                },
                itemStyle: {
                  normal: {
                    color: 'transparent',
                    borderWidth: 0,
                    shadowBlur: 0
                  }
                }
              }
            ]
          },
          {
            type: 'pie',
            radius: ['55%', '130%'],
            startAngle: 180,
            hoverAnimation: false,
            center: ['45%', '83%'],
            roseType: 'radius',
            labelLine: {
              normal: {
                show: false
              }
            },
            data: [
              {
                value: getxb1,
                itemStyle: {
                  normal: {
                    // eslint-disable-next-line no-undef
                    color: new echarts.graphic.LinearGradient(
                      0,
                      0,
                      0,
                      1,
                      [
                        {
                          offset: 0,
                          color: 'rgba(76,141,250,.3)'
                        },
                        {
                          offset: 1,
                          color: 'rgba(92,207,255,.3)'
                        }
                      ],
                      false
                    )
                  }
                }
              },
              {
                value: getxb2,
                itemStyle: {
                  normal: {
                    // eslint-disable-next-line no-undef
                    color: new echarts.graphic.LinearGradient(
                      0,
                      0,
                      0,
                      1,
                      [
                        {
                          offset: 0,
                          color: 'rgba(255,209,139,.3)'
                        },
                        {
                          offset: 1,
                          color: 'rgba(253,173,89,.3)'
                        }
                      ],
                      false
                    )
                  }
                }
              },
              {
                value: getxb1 + getxb2,
                name: '',
                label: {
                  show: false
                },
                labelLine: {
                  show: false
                },
                itemStyle: {
                  normal: {
                    color: 'transparent',
                    borderWidth: 0,
                    shadowBlur: 0,
                    borderColor: 'transparent',
                    shadowColor: 'transparent'
                  }
                }
              }
            ],
            z: -1
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
