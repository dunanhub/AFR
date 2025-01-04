<template>
    <canvas ref="chart" id="line"></canvas>
  </template>
  
  <script>
  import {
    Chart,
    LineController,
    LineElement,
    PointElement,
    LinearScale,
    Title,
    Tooltip,
    Legend,
    CategoryScale,
  } from 'chart.js';
  
  // Регистрируем компоненты
  Chart.register(LineController, LineElement, PointElement, LinearScale, Title, Tooltip, Legend, CategoryScale);
  
  export default {
    props: ['data'],
    mounted() {
      new Chart(this.$refs.chart, {
        type: 'line',
        data: {
          labels: this.data.map((d) => d.x), // Метки оси X
          datasets: [
            {
              label: 'Посещения',
              data: this.data.map((d) => d.y), // Значения оси Y
              borderColor: 'blue',
              fill: false,
            },
          ],
        },
      });
    },
  };
  </script>
  
  <style>
  
  </style>