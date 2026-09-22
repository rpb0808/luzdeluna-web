import type { Config } from "tailwindcss";

const config: Config = {
  content: ["./app/**/*.{js,ts,jsx,tsx,mdx}"],
  theme: {
    extend: {
      colors: {
        // Paleta tierra/verde con acento dorado, segun el estado del arte
        luna: {
          fondo: "#faf7f2",
          texto: "#241d15",
          verde: "#2f3b2a",
          dorado: "#b8935a",
        },
      },
      fontFamily: {
        serif: ["Georgia", "Cambria", "serif"],
      },
    },
  },
  plugins: [],
};

export default config;
