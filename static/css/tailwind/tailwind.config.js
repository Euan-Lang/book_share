module.exports = {
  content: ["./../../../templates/**/*.html"],
  theme: {
    extend: {
      fontFamily: {
        sans: ["Work Sans", "sans-serif"],
      },
      colors: {
        white: "#ffffff",
        black: "#1E2019",
        gray: "#E5E5E5",
        blue: {
          DEFAULT: "#3379FC",
          900: "#0350DD",
        },
      },
    },
  },
  plugins: [
    require("@tailwindcss/forms")({
      strategy: "base", // only generate global styles
    }),
  ],
};
