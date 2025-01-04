<template>
    <LayoutHeader />
          <br>
    <div class="analytics-page">
      <h1>Аналитика</h1>
  
      <!-- Фильтры -->
      <div class="filters">
        <label>
          Дата:
          <input type="date" v-model="filters.startDate" />
          -
          <input type="date" v-model="filters.endDate" />
        </label>
        <button @click="fetchAnalytics">Применить фильтры</button>
  
      </div>
  
      <!-- Аналитические блоки -->
      <div class="analytics-blocks">
        <!-- Посещения -->
        <div class="block">
          <h2>Посещения</h2>
          <line-chart v-if="trends.length" :data="trends" />
          <p v-else>Нет данных для отображения.</p>
        </div>
  
        <!-- Количество пользователей -->
        <div class="block">
          <h2>Количество пользователей</h2>
          <bar-chart v-if="regions.datasets && regions.datasets[0].data.length" :data="regions" />
          <p v-else>Нет данных для отображения.</p>
        </div>
  
        <!-- Аномалии -->
        <div class="block">
          <h2>Аномалии</h2>
          <ul v-if="anomalies.length">
            <li v-for="anomaly in anomalies" :key="anomaly.day">
              {{ anomaly.day }}: {{ anomaly.count }} запросов
            </li>
          </ul>
          <p v-else>Нет аномалий.</p>
        </div>
  
        <!-- Активность по дням недели -->
        <div class="block">
          <h2>Активность по дням недели</h2>
          <bar-chart v-if="weekdayActivity.datasets.length" :data="weekdayActivity" />
        </div>
  
  
        <!-- Сегментация по полу -->
        <div class="block">
          <h2>Сегментация по полу</h2>
          <pie-chart
              v-if="genderDistribution.length"
              :data="{
                  labels: genderDistribution.map((g) => g.gender),
                  datasets: [
                    {
                      data: genderDistribution.map((g) => g.total),
                      backgroundColor: ['#36A2EB', '#FF6384'],
                    },
                  ],
              }"
          />
  
          <p v-else>Нет данных для отображения.</p>
        </div>
  
        <!-- Сегментация по возрасту -->
        <div class="block">
          <h2>Сегментация по возрасту</h2>
          <bar-chart v-if="ageGroups.datasets.length" :data="ageGroups" />
          <p v-else>Нет данных для отображения.</p>
        </div>
      </div>
    </div>
</template>
  
<script>
  import LineChart from '~/components/LineChart.vue';
  import BarChart from '~/components/BarChart.vue';
  import PieChart from '~/components/PieChart.vue';
  import axios from 'axios';
  
  axios.defaults.baseURL = 'http://127.0.0.1:8000';
  
  export default {
    components: {
      LineChart,
      BarChart,
      PieChart,
    },
    data() {
      return {
        filters: {
          startDate: null,
          endDate: null,
        },
        trends: [],
        regions: [],
        anomalies: [],
        weekdayActivity: { labels: [], datasets: [] },
        genderDistribution: [],
        ageGroups: { labels: [], datasets: [] },
      };
    },
    methods: {
      formatDate(date) {
        if (!date) return null;
        const d = new Date(date);
        return `${d.getFullYear()}-${(d.getMonth() + 1).toString().padStart(2, '0')}-${d.getDate().toString().padStart(2, '0')}`;
      },
      async fetchAnalytics() {
        const startDate = this.formatDate(this.filters.startDate);
        const endDate = this.formatDate(this.filters.endDate);
        console.log('Фильтры:', { startDate, endDate });
  
        try {
          const [trendsResponse, regionsResponse, anomaliesResponse, ageResponse, weekdayResponse] = await Promise.all([
            axios.get('/api/analytics/trends', { params: { start_date: startDate, end_date: endDate } }),
            axios.get('/api/analytics/regions', { params: { start_date: startDate, end_date: endDate } }),
            axios.get('/api/analytics/anomalies', { params: { start_date: startDate, end_date: endDate } }),
            axios.get('/api/analytics/age'),
            axios.get('/api/analytics/weekday-activity'),
          ]);
  
          this.trends = trendsResponse.data.trends.map((item) => ({
            x: new Date(item.day).toLocaleDateString('ru-RU', {
              day: '2-digit',
              month: '2-digit',
              year: 'numeric',
            }),
            y: item.count,
          }));
  
  
          this.regions = {
            labels: regionsResponse.data.regions.map((region) => region.region),
            datasets: [
              {
                label: 'Количество пользователей',
                data: regionsResponse.data.regions.map((region) => region.total_users),
                backgroundColor: '#36A2EB',
              },
            ],
          };
  
          this.anomalies = anomaliesResponse.data.anomalies.map((anomaly) => ({
            day: new Date(anomaly.day).toLocaleDateString('ru-RU', {
              day: '2-digit',
              month: '2-digit',
              year: 'numeric',
            }),
            count: anomaly.count,
          }));
  
          this.genderDistribution = ageResponse.data.gender || [];
          this.ageGroups = {
            labels: Object.keys(ageResponse.data.age_groups),
            datasets: [
              {
                label: 'Возрастные группы',
                data: Object.values(ageResponse.data.age_groups),
                backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF'],
              },
            ],
          };
  
          this.weekdayActivity = {
            labels: weekdayResponse.data.weekdays.map((item) => item.day),
            datasets: [
              {
                label: 'Количество пользователей',
                data: weekdayResponse.data.weekdays.map((item) => item.total),
                backgroundColor: '#36A2EB',
              },
            ],
          };
        } catch (error) {
          console.error('Ошибка загрузки данных:', error);
        }
      },
    },
      mounted() {
      console.log('Компонент загружен, вызываем fetchAnalytics');
      this.fetchAnalytics();
    },
  };

  definePageMeta({
      middleware: 'auth',  // Подключаем middleware для этой страницы
  });
</script>
  
<style>
    .analytics-page {
        padding: 20px;
    }

    .filters {
        margin-bottom: 20px;
    }

    .analytics-blocks {
        display: grid;
        grid-template-columns: 1fr 1fr 1fr;
        gap: 20px;
    }

    .block {
        padding: 20px;
        background: #f4f4f4;
        border-radius: 10px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }

    canvas {
        height: 300px;
        width: 400px;
    }
</style>