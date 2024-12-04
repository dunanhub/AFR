<template>
  <div class="dashboard-container">
    <div class="content">
      <!-- Карта -->
      <div class="card">
        <div class="card-body map-container">
          <svg
              xmlns="http://www.w3.org/2000/svg"
              :viewBox="viewBox"
              class="map-svg"
          >
            <g id="kz">
              <path
                  v-for="region in regions"
                  :key="region.id"
                  :d="region.path"
                  :data-name="region.region"
                  :class="{ active: selectedRegion === region.id }"
                  @click="handleRegionClick(region)"
              />
              <text
                  v-for="region in regions"
                  :key="'text-' + region.id"
                  :x="region.labelPosition.x"
                  :y="region.labelPosition.y"
                  text-anchor="middle"
                  class="region-label"
                  :style="{ fontSize: region.region.length > 10 ? '40px' : '55px' }"
              >
                {{ region.region }}
              </text>
            </g>
          </svg>
        </div>
      </div>


      <!-- Данные -->
      <div class="data-cards">
        <div class="data-card" v-if="analyticsData">
          <h3>Данные для региона: {{ selectedRegionName }}</h3>

          <!-- Круговая диаграмма -->
          <div class="chart">
            <canvas id="genderChart"></canvas>
          </div>

          <!-- Гистограмма возрастов -->
          <div class="chart">
            <canvas id="ageChart"></canvas>
          </div>

          <div class="chart">
            <canvas id="childrenChart"></canvas>
          </div>

          <!-- Круговая диаграмма по пособиям -->
          <div class="chart">
            <canvas id="benefitsChart"></canvas>
          </div>

        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { Chart } from "chart.js";

export default {
  data() {
    return {
      regions: [
        { id: 1,
          region: "Астана",
          path: "M2140.64 429.237L2117.5 620.525L1746.47 787.641L1665.49 729.001L1603.42 756.978L1463.78 617.466L1507.93 448.485L1659.76 469.972L1757.55 258.988L1944.66 305.84L2140.64 429.237Z",
          labelPosition: { x: 1800, y: 570 } },
        { id: 2,
          region: "Актобе",
          path: "M775.05 1533.77L758.435 1399.63L640.468 1235.05L629.51 998.848L536.467 931.33L603.045 730.792L756.734 652.381L921.498 650.815L1023.17 724.226L1169.14 622.539L1267.48 812.932L1234.1 959.755L1350.08 1083L1264.48 1228.04L1142.08 1135.6L958.605 1409.85L959.752 1503.11L775.05 1533.77Z",
          labelPosition: { x: 900, y: 1000 } },
        { id: 3,
          region: "Алматы",
          path: "M2288.47 1865.54L2247.57 1685.89L2156.07 1576.96L2144.44 1408.13L2204.25 1329.2L2320.6 1313.91L2317.31 1465.65L2409.68 1682.46L2478.04 1722.15L2661.95 1733.34L2682.49 1829.73L2615.39 1941.04L2499.88 1870.69L2288.47 1865.54Z",
          labelPosition: { x: 2400, y: 1800 } },
        { id: 5,
          region: "Атырау",
          path: "M536.467 931.331L629.51 998.849L640.468 1235.05L758.435 1399.63L662.424 1358.74L471.866 1444.76L481.479 1307.04L340.766 1257.65L178.098 1353L135.097 1197.07L21.6804 1145.37L2.9292 1062.79L203.06 1125.45L331.628 1013.69L447.023 1044.13L536.467 931.331Z",
          labelPosition: { x: 400, y: 1200 } },
        { id: 6,
          region: "Семей",
          path: "M2799.66 1476.55L2768.84 1394.26L2557.36 1245.87L2419.02 1234.38L2371.39 927.749L2439.08 777.793L2563.02 557.036L2616.74 678.269L2745.62 698.786L2724.02 816.96L2905.44 1051.59L2871.97 1227.36L2799.66 1476.55Z",
          labelPosition: { x: 2600, y: 1000 } },
        { id: 7,
          region: "Тараз",
          path: "M2144.44 1408.13L2156.07 1576.96L2247.57 1685.89L2288.47 1865.54L2168.85 1823.61L2100.37 1930.22L1975.36 1880.83L1896.87 1957.75L1833.78 1831.74L1751.69 1408.13L1933.03 1408.06L2144.44 1408.13Z",
          labelPosition: { x: 1980, y: 1610 } },
        { id: 8,
          region: "Жезказган",
          path: "M1264.48 1228.04L1350.09 1083L1408.75 969.305L1516.31 955.652L1623.16 825.391L1668.1 934.166L1782.35 1013.62L1957.72 925.362L1993.24 1139.48L1937.19 1160.89L1933.03 1408.06L1751.69 1408.13L1604.18 1408.43L1468.01 1357.18L1264.48 1228.04Z",
          labelPosition: { x: 1650, y: 1200 } },
        { id: 9,
          region: "Костанай",
          path: "M1507.93 448.485L1463.78 617.466L1603.42 756.978L1665.49 729.001L1623.16 825.391L1516.31 955.652L1408.75 969.305L1350.09 1083L1234.1 959.755L1267.49 812.932L1169.14 622.539L1109.05 271.522L1517.38 120.148L1507.93 448.485Z",
          labelPosition: { x: 1300, y: 500 } },
        { id: 10,
          region: "Кызылорда",
          path: "M959.753 1503.1L958.605 1409.85L1142.08 1135.6L1264.48 1228.04L1468.01 1357.18L1604.18 1408.43L1658.97 1829.2L1519.83 1945.07L1433.04 1741.47L1197.11 1783.25L1126.1 1667.83L959.753 1503.1Z",
          labelPosition: { x: 1300, y: 1500 } },
        { id: 11,
          region: "Актау",
          path: "M758.435 1399.63L775.05 1533.77L720.022 1557.34L720.102 2105.92L576.738 1954.17L479.462 1989.68L395.121 1879.56L269.678 1610.46L356.669 1504L471.866 1444.76L662.424 1358.74L758.435 1399.63Z" ,
          labelPosition: { x: 500, y: 1700 } },
        { id: 12,
          region: "Петропавловск",
          path: "M2140.64 429.237L1944.66 305.84L1757.55 258.988L1659.76 469.972L1507.93 448.485L1517.38 120.148L1685.59 71.3557L1745.36 0.629883L1887.74 20.8479L1919.78 199.08L2099.89 297.783L2140.64 429.237Z",
          labelPosition: { x: 1700, y: 200 } },
        { id: 14,
          region: "Павлодар",
          path: "M2117.5 620.525L2140.64 429.237L2099.89 297.782L2274.23 199.527L2450.43 322.85L2563.02 557.036L2439.08 777.793L2248.56 783.985L2145.66 722.212L2117.5 620.525Z",
          labelPosition: { x: 2300, y: 500 } },
        { id: 16,
          region: "Туркестан",
          path: "M1751.69 1408.13L1833.78 1831.74L1896.88 1957.75L1714.59 2175L1559.35 2116.81L1519.83 1945.07L1658.96 1829.2L1604.18 1408.43L1751.69 1408.13Z",
          labelPosition: { x: 1700, y: 2000 } },
        { id: 17,
          region: "Уральск",
          path: "M603.045 730.792L536.467 931.33L447.023 1044.13L331.628 1013.69L203.06 1125.45L2.92931 1062.78L0.160156 831.583L137.352 730.269L285.937 572.255L512.652 585.311L603.045 730.792Z",
          labelPosition: { x: 300, y: 850 } },
        { id: 18,
          region: "Караганда",
          path: "M1665.49 729.001L1746.47 787.641L2117.5 620.525L2145.66 722.212L2248.56 783.985L2439.08 777.793L2371.39 927.75L2419.02 1234.38L2320.6 1313.91L2204.25 1329.2L2144.44 1408.13L1933.03 1408.06L1937.19 1160.89L1993.24 1139.48L1957.72 925.362L1782.35 1013.62L1668.1 934.166L1623.16 825.391L1665.49 729.001Z",
          labelPosition: { x: 2150, y: 1000 } },
        { id: 19,
          region: "Талдыкорган",
          path: "M2661.95 1733.34L2478.04 1722.15L2409.68 1682.46L2317.31 1465.65L2320.6 1313.91L2419.02 1234.38L2557.36 1245.87L2768.84 1394.26L2799.66 1476.55L2651.07 1549.51L2661.95 1733.34Z",
          labelPosition: { x: 2500, y: 1500 } },
        { id: 20,
          region: "Усть-Каменогорск",
          path: "M2871.97 1227.36L2905.44 1051.59L2724.02 816.961L2745.62 698.786L2922.49 680.657L3031.68 866.946L3157 878.734L3140.27 1028.91L3073.06 1054.35L3069.53 1226.39L3001.18 1283.99L2871.97 1227.36Z",
          labelPosition: { x: 2950, y: 900 } }
      ],
      selectedRegion: null,
      selectedRegionName: null,
      originalViewBox: "0 0 3157 2175",
      viewBox: "0 0 3157 2175",
      analyticsData: null,
      genderChartInstance: null,
      ageChartInstance: null,
      childrenChartInstance: null, // Новый график для детей
    };
  },
  methods: {
    resetViewBox() {
      this.viewBox = this.originalViewBox;
      this.selectedRegion = null;
      this.analyticsData = null;

      // Удаляем существующие графики при сбросе
      if (this.genderChartInstance) this.genderChartInstance.destroy();
      if (this.ageChartInstance) this.ageChartInstance.destroy();
      if (this.childrenChartInstance) this.childrenChartInstance.destroy();
    },
    async handleRegionClick(region) {
      const encodedRegionName = encodeURIComponent(region.region);

      if (this.selectedRegion === region.id) {
        return;
      }

      this.selectedRegion = region.id;
      this.selectedRegionName = region.region;

      try {
        const [genderResponse, ageResponse, childrenResponse] = await Promise.all([
          fetch(`http://127.0.0.1:8000/api/analytics/region/${encodedRegionName}/gender/`).then((res) => res.json()),
          fetch(`http://127.0.0.1:8000/api/analytics/region/${encodedRegionName}/age/`).then((res) => res.json()),
          fetch(`http://127.0.0.1:8000/api/analytics/region/${encodedRegionName}/children/`).then((res) => res.json()),
        ]);

        this.analyticsData = {
          gender: genderResponse,
          age: ageResponse,
          children: childrenResponse.children_stats.distribution,

        };

        // Обновляем графики
        this.$nextTick(() => {
          this.renderGenderChart(genderResponse.gender_distribution);
          this.renderAgeChart(ageResponse.age_distribution);
          this.renderChildrenChart(childrenResponse.children_stats.distribution);
        });
      } catch (error) {
        console.error("Ошибка загрузки данных:", error);
      }
    },

    renderGenderChart(data) {
      if (this.genderChartInstance) this.genderChartInstance.destroy();

      const ctx = document.getElementById("genderChart").getContext("2d");
      this.genderChartInstance = new Chart(ctx, {
        type: "pie",
        data: {
          labels: ["Мужчины", "Женщины"],
          datasets: [
            {
              data: [data.male_percentage, data.female_percentage],
              backgroundColor: ["#36A2EB", "#FF6384"],
            },
          ],
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
        },
      });
    },
    renderAgeChart(data) {
      if (this.ageChartInstance) this.ageChartInstance.destroy();

      const ctx = document.getElementById("ageChart").getContext("2d");
      this.ageChartInstance = new Chart(ctx, {
        type: "bar",
        data: {
          labels: Object.keys(data.age_groups),
          datasets: [
            {
              label: "Возрастные группы",
              data: Object.values(data.age_groups),
              backgroundColor: "rgba(54,162,235,0.6)",
              borderColor: "rgb(54,162,235)",
              borderWidth: 1,
            },
          ],
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            x: {
              title: {
                display: true,
                text: "Возрастные группы",
              },
            },
            y: {
              beginAtZero: true,
              title: {
                display: true,
                text: "Количество людей",
              },
            },
          },
        },
      });
    },
    renderChildrenChart(data) {
      // Уничтожаем старый график, если он есть
      if (this.childrenChartInstance) {
        this.childrenChartInstance.destroy();
      }

      const ctx = document.getElementById("childrenChart").getContext("2d");

      // Убедитесь, что данные корректны
      if (!data || typeof data !== "object") {
        console.error("Invalid children data:", data);
        return;
      }

      // Создаем гистограмму
      this.childrenChartInstance = new Chart(ctx, {
        type: "bar",
        data: {
          labels: Object.keys(data).map((key) => key.replace("_children", " детей")),
          datasets: [
            {
              label: "Количество детей",
              data: Object.values(data),
              backgroundColor: "rgba(79,75,192,0.6)",
              borderColor: "rgb(79,75,192)",
              borderWidth: 1,
            },
          ],
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            x: {
              title: {
                display: true,
                text: "Число детей",
              },
            },
            y: {
              beginAtZero: true,
              title: {
                display: true,
                text: "Количество пользователей",
              },
            },
          },
        },
      });
    },
  },
};
</script>


<style>
.content {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 20px;
  align-items: stretch;
}

.map-container {
  display: flex;
  flex: 1;
  height: 100%;
  justify-content: center;
  align-items: center;
  padding: 10px;
  background-color: #ffffff;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}


.map-svg {
  width: 100%; /* Растягиваем на всю ширину родителя */
  height: auto; /* Пропорциональная высота */
  max-height: 600px; /* Установите ограничение по высоте, если нужно */
  display: block;
  margin: auto; /* Центрируем */
}



path {
  fill: #213e60;
  stroke: #ffffff;
  stroke-width: 5px;
  cursor: pointer;
  transition: fill 0.3s ease;
}

path:hover {
  fill: #4071b4;
}

path.active {
  fill: #e14d4d;
}

.region-label {
  font-size: 12px;
  fill: #ffffff;
  pointer-events: none;
}


.data-cards {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.data-card {
  background: white;
  border-radius: 10px;
  padding: 20px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  height: 100%;
}

.card {
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 100%;
  background-color: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  overflow: hidden;
}

.card-body {
  display: flex;
  flex: 1;
  padding: 0;
  justify-content: center;
  align-items: center;
}


</style>