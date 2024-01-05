/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  theme: {
    fontFamily: {
      display: ['Gupter', 'Times New Roman', 'serif'],
      sans: ['Inter', 'sans-serif']
    },
    extend: {},
  },
  plugins: [require("daisyui")],
  daisyui: {
    themes: [
      {
        dzogchen: {
          "primary": "#080067",   // dark blue from the image's background
          "secondary": "#dc2626", // similar to primary but slightly different
          "accent": "#00d1ff",    // another dark blue variant
          "neutral": "#ff00ff",   // a more vibrant dark blue
          "base-100": "#dcedf3",  // darkest blue identified
          "base-200": "#c4e3ee",  // darkest blue identified
          "base-300": "#87cfe9",  // darkest blue identified
          "info": "#67e8f9",
          "success": "#41d888",
          "warning": "#ffcc00",
          "error": "#ff0000",
          "text-base-content": "#a9dbf9", // white text

          "--rounded-box": "1rem",          // border radius rounded-box utility class, used in card and other large boxes
          "--rounded-btn": "0.5rem",        // border radius rounded-btn utility class, used in buttons and similar elements
          "--rounded-badge": "1.9rem",      // border radius rounded-badge utility class, used in badges and similar
          "--animation-btn": "0.25s",       // duration of animation when you click on a button
          "--animation-input": "0.2s",      // duration of animation for inputs like checkbox, toggle, radio, etc
          "--btn-focus-scale": "0.95",      // scale transform of a button when you focus on it
          "--border-btn": "1px",            // border width of buttons
          "--tab-border": "1px",            // border width of tabs
          "--tab-radius": "0.5rem"          // border radius of tabs
        }
      },
      "light",
      "dark",
      "cupcake",
      "bumblebee",
      "emerald",
      "corporate",
      "synthwave",
      "retro",
      "cyberpunk",
      "valentine",
      "halloween",
      "garden",
      "forest",
      "aqua",
      "lofi",
      "pastel",
      "fantasy",
      "wireframe",
      "black",
      "luxury",
      "dracula",
      "cmyk",
      "autumn",
      "business",
      "acid",
      "lemonade",
      "night",
      "coffee",
      "winter",
      "dim",
      "nord",
      "sunset",
    ],
  },
}

