/** @type {import('tailwindcss').Config} */
module.exports = {
  mode: 'jit',
  content: [
  './**/templates/**/*.html',
  './**/*.html',
  './static/**/*.js',
  './media/**/*.{jpg,jpeg,png,svg,gif}',

  ],
  theme: {
    extend: {
		colors:{
		  lightblue: '#ADD8E6',
		},
	},
  },
  plugins: [],
}

