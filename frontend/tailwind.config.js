const withMT = require("@material-tailwind/html/utils/withMT");

module.exports = withMT({
    content: ['../core/templates/**/*.html'],
    safelist: ["textinput", "bg-white", "px-4", "leading-normal", "rounded-lg", "border-gray-300", "text-gray-700", "block", "border", "appearance-none", "w-full", "focus:outline-none", "py-2"],
    theme: {
        extend: {},
    },
    plugins: [],
});