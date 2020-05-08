require("dotenv").config();

const webpack = require("webpack");
const withImages = require("next-images");
const path = require("path");
const withSass = require('@zeit/next-sass');
const Dotenv = require("dotenv-webpack");
const CompressionPlugin = require('compression-webpack-plugin');

let config = {
  webpack: config => {
  config.plugins = config.plugins || [];
  config.node = {
    fs: "empty"
  };

  config.plugins = [
    ...config.plugins,
    new Dotenv({
      path: path.join(__dirname, ".env"),
      systemvars: true
    }),
    new CompressionPlugin({
      test: /\.js$|\.css$|\.html$/,
      filename: 'bundle.gz',
      algorithm: 'gzip',
      test: /\.js$|\.css$|\.html$/,
      threshold: 10240,
      minRatio: 0.8,
    }),
  ];

  return config;
  }
};

config = withImages(config);
config = withSass(config);

module.exports = config;
