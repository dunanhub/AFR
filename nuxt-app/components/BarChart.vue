<template>
    <div>
      <canvas ref="chartCanvas"></canvas>
    </div>
  </template>
  
  <script>
  import {
    Chart,
    BarController,
    BarElement,
    CategoryScale,
    LinearScale,
    Title,
    Tooltip,
  } from 'chart.js';
  
  // Регистрируем компоненты для графика
  Chart.register(BarController, BarElement, CategoryScale, LinearScale, Title, Tooltip);
  
  export default {
    props: {
      data: {
        type: Object,
        required: true,
      },
    },
    mounted() {
      if (this.data.labels && this.data.datasets) {
        this.createChart();
      } else {
        console.error('Неверный формат данных для BarChart:', this.data);
      }
    },
    methods: {
      createChart() {
        const ctx = this.$refs.chartCanvas.getContext('2d');
        new Chart(ctx, {
          type: 'bar',
          data: this.data,
          options: {
            responsive: true,
            plugins: {
              title: {
                display: true,
  
              },
            },
          },
        });
      },
    },
  };
  </script>
  
  <style scoped>
  canvas {
    max-width: 100%;
  }
  </style>