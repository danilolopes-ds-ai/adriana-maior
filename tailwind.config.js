/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./index.html'],
  theme: {
    extend: {
      colors: {
        bgBase: '#FBF9F6',
        bgAlt: '#F2EFE9',
        textMain: '#1A1817',
        textMuted: '#5C544D',
        borderLight: '#DCD7D0',
        brandBlue: '#2A8A96',
        earthTone: '#8A6F5A',
        terracotta: '#C97A56',
      },
      fontFamily: {
        display: ['Cinzel', 'serif'],
        sans: ['Montserrat', 'sans-serif'],
      },
      letterSpacing: {
        lux: '0.2em',
        ui: '0.1em',
      },
    },
  },
  plugins: [],
};
