require("dotenv").config();

const withImages = require("next-images");
const path = require("path");
const withSass = require('@zeit/next-sass');
const Dotenv = require("dotenv-webpack");

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
    })
  ];

  return config;
  }
};

config = withImages(config);
config = withSass(config);

module.exports = config;
