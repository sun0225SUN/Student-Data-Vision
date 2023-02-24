// vue配置
const webpack = require('webpack')
module.exports = {
  devServer: {
    port: 8999, // 端口号
    open: true // 自动打开
  },
  configureWebpack: {
    plugins: [
      new webpack.ProvidePlugin({
        $: 'jquery',
        jQuery: 'jquery',
        'window.jQuery': 'jquery'
      })
    ]
  }

}
