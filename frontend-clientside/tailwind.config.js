/** @type {import('tailwindcss').Config} */
export default {
  content: ["public/index.html",
    "./src/**/*.{js,ts,jsx,tsx}",],
  theme: {
    extend: {
      fontSize:{
        '12px': '12px',
        '10px': '10px',
        
      },
      translate: {
        
        '-4': '-1rem', // Customize as needed
        '0': '0',
        '2': '0.5rem', // Adding custom translate value for x and y
        '-2': '-0.5rem', // Adding custom negative translate value for x and y
      },
      boxShadow: {
        'custom-red': '3px 3px 0px red', // Customize as needed
        'custom-blue': '3px 3px 0px blue'
      },
      borderWidth:{
        '1': '1px'
      },
      height:{
        '0.7':'2.5px'
      },
      margin:{
        '38' : '150px'
      }
    },
  },
  variants: {
    extend: {
      translate: ['hover'], // Enable hover variants for translate
    },
  },
  plugins: [],
  plugins: [],
}