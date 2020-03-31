var path = require('path');
const TerserPlugin = require('terser-webpack-plugin'); //minificadornp

module.exports = {
    entry: { 
        main: './src/js/main.js',
        vendor: './src/js/vendor.js'
    },
    output: {
        filename: '[name].bundle.js',
        path: path.resolve(__dirname, 'static/script/js')
    },
    optimization: {
        minimize: true,
        minimizer: [new TerserPlugin({
            test: /\.js(\?.*)?$/i,
          })],
    },
    module: {
        rules: [
            {
                test: /\.css$/,
                use: [
                    'style-loader',
                    'css-loader',
                ],
            },
        ],
    },
}