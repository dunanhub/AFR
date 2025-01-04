<template>
    <div>
      <canvas ref="pieChart"></canvas>
    </div>
  </template>
  
  <script>
  import { Chart } from 'chart.js';
  
  export default {
    props: {
      data: {
        type: Object,
        required: true,
      },
    },
    mounted() {
      if (this.data && this.data.labels && this.data.datasets) {
        new Chart(this.$refs.pieChart, {
          type: 'pie',
          data: this.data,
          options: {
            responsive: true,
            maintainAspectRatio: false,
          },
        });
      } else {
        console.error('Некорректные данные для PieChart:', this.data);
      }
    },
  };
  </script>