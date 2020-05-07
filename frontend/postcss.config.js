module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
    ...(process.env.NODE_ENV === 'production'
      ? {
        '@fullhuman/postcss-purgecss': {
          content: [
            './components/**/*.js',
            './pages/**/*.js',
            './styles/_components.scss'
            ],
            defaultExtractor: content => content.match(/[\w-/:]+(?<!:)/g) || []
        }
   }
  : {})
  }
};
