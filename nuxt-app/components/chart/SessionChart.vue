<template>
    <div>
      <canvas ref="sessionChart"></canvas>
    </div>
  </template>
  
  <script>
import { Chart } from 'chart.js/auto';

export default {
  props: {
    data: {
      type: Array,
      required: true,
    },
  },
  mounted() {
    this.renderChart();
  },
  methods: {
    renderChart() {
      new Chart(this.$refs.sessionChart, {
        type: 'line',
        data: {
          labels: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
          datasets: [
            {
              label: 'Sessions',
              data: this.data,
              borderColor: 'rgb(230, 140, 58)',
              backgroundColor: 'rgba(230, 140, 58, 0.2)',
              pointHoverBackgroundColor: 'rgb(230, 140, 58)',
              pointHoverBorderColor: 'rgb(230, 140, 58)',
              fill: true,
              tension: 0, // Set to 0 to create straight lines between points
            },
          ],
        },
        options: {
          responsive: true,
          plugins: {
            legend: {
              display: false, // Hide the legend
            },
            tooltip: {
              enabled: true,
              callbacks: {
                title: (tooltipItems) => {
                  // Display the day name
                  const days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье'];
                  return days[tooltipItems[0].dataIndex];
                },
                label: function (tooltipItem) {
                  // Display the session count
                  return `Количество сеансов: ${tooltipItem.raw}`;
                },
              },
            },
          },
          scales: {
            x: {
              display: false, // Hide x-axis labels
              grid: {
                display: false, // Hide x-axis grid lines
              },
            },
            y: {
              display: false, // Hide y-axis labels
              grid: {
                display: false, // Hide y-axis grid lines
              },
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
  