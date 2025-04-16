const withMT = require("@material-tailwind/html/utils/withMT");

module.exports = withMT({
  content: [
    '../core/templates/**/*.html'
  ],
  theme: {
    extend: {},
  },
  plugins: [],
});