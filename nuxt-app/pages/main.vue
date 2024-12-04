<template>
  <div>
      <LayoutHeader />
      <div class="pb-10">
        <div class="mx-auto max-w-2xl px-6 lg:max-w-7xl lg:px-8 ">
          <div class="mt-10 grid gap-4 sm:mt-16 lg:grid-cols-3 lg:grid-rows-2">
            <div class="relative lg:row-span-2">
              <div class="absolute inset-px rounded-lg bg-white lg:rounded-l-[2rem]" />
              <div class="relative flex h-full flex-col overflow-hidden rounded-[calc(theme(borderRadius.lg)+1px)] lg:rounded-l-[calc(2rem+1px)]">
                <div class="px-8 pb-3 pt-8 sm:px-10 sm:pb-0 sm:pt-10">
                  <p class="mt-2 text-lg font-medium tracking-tight text-gray-950 max-lg:text-center">Пользователи</p>
                  <p class="mt-2 max-w-lg text-sm/6 text-gray-600 max-lg:text-center">Количество пользователей</p>
                </div>
                <div class="relative min-h-[30rem] w-full grow [container-type:inline-size] max-lg:mx-auto max-lg:max-w-sm">
                  <div class="absolute inset-x-10 bottom-0 top-10 overflow-hidden rounded-t-[12cqw] border-x-[3cqw] border-t-[3cqw] border-gray-700 bg-gray-900 shadow-2xl">
                    <img class="size-full object-cover object-top" src="https://tailwindui.com/plus/img/component-images/bento-03-mobile-friendly.png" alt="" />
                  </div>
                </div>
              </div>
              <div class="pointer-events-none absolute inset-px rounded-lg shadow ring-1 ring-black/5 lg:rounded-l-[2rem]" />
            </div>
            <div class="relative flex w-full  p-6 rounded-lg shadow-lg text-white" style="background-color: rgb(33, 62, 96);">
              <div class="absolute inset-0 rounded-lg bg-opacity-20"></div>
              <div class="relative flex flex-col items-start">
                <p class="text-lg font-semibold">Sessions</p>
                <div class="flex items-baseline mt-4">
                  <p class="text-3xl font-bold">24.5k</p>
                  <p class="ml-2 text-sm text-red-400">-20%</p>
                </div>
                <p class="mt-2 text-sm text-gray-400">Last Week</p>
              </div>

              <!-- Блок для графика -->
              <div class="absolute  left-0 right-0 bottom-0 w-70 h-30">
                <canvas ref="sessionsChart"></canvas>
              </div>
            </div>


            <div class="relative max-lg:row-start-3 lg:col-start-2 lg:row-start-2">
              <div class="absolute inset-px rounded-lg bg-white" />
              <div class="relative flex h-full flex-col overflow-hidden rounded-[calc(theme(borderRadius.lg)+1px)]">
                <div class="px-8 pt-8 sm:px-10 sm:pt-10">
                  <p class="mt-2 text-lg font-medium tracking-tight text-gray-950 max-lg:text-center">Security</p>
                  <p class="mt-2 max-w-lg text-sm/6 text-gray-600 max-lg:text-center">Morbi viverra dui mi arcu sed. Tellus semper adipiscing suspendisse semper morbi.</p>
                </div>
                <div class="flex flex-1 items-center [container-type:inline-size] max-lg:py-6 lg:pb-2">
                  <img class="h-[min(152px,40cqw)] object-cover object-center" src="https://tailwindui.com/plus/img/component-images/bento-03-security.png" alt="" />
                </div>
              </div>
              <div class="pointer-events-none absolute inset-px rounded-lg shadow ring-1 ring-black/5" />
            </div>
            <div class="relative lg:row-span-2">
              <div class="absolute inset-px rounded-lg bg-white max-lg:rounded-b-[2rem] lg:rounded-r-[2rem]" />
              <div class="relative flex h-full flex-col overflow-hidden rounded-[calc(theme(borderRadius.lg)+1px)] max-lg:rounded-b-[calc(2rem+1px)] lg:rounded-r-[calc(2rem+1px)]">
                <div class="px-8 pb-3 pt-8 sm:px-10 sm:pb-0 sm:pt-10">
                  <p class="mt-2 text-lg font-medium tracking-tight text-gray-950 max-lg:text-center">Powerful APIs</p>
                  <p class="mt-2 max-w-lg text-sm/6 text-gray-600 max-lg:text-center">Sit quis amet rutrum tellus ullamcorper ultricies libero dolor eget sem sodales gravida.</p>
                </div>
                <div class="relative min-h-[30rem] w-full grow">
                  <div class="absolute bottom-0 left-10 right-0 top-10 overflow-hidden rounded-tl-xl bg-gray-900 shadow-2xl">
                    <div class="flex bg-gray-800/40 ring-1 ring-white/5">
                      <div class="-mb-px flex text-sm/6 font-medium text-gray-400">
                        <div class="border-b border-r border-b-white/20 border-r-white/10 bg-white/5 px-4 py-2 text-white">NotificationSetting.jsx</div>
                        <div class="border-r border-gray-600/10 px-4 py-2">App.jsx</div>
                      </div>
                    </div>
                    <div class="px-6 pb-14 pt-6">
                      <!-- Your code example -->
                    </div>
                  </div>
                </div>
              </div>
              <div class="pointer-events-none absolute inset-px rounded-lg shadow ring-1 ring-black/5 max-lg:rounded-b-[2rem] lg:rounded-r-[2rem]" />
            </div>
          </div>
        </div>
      </div>
  </div>
</template>

<script>

  import { onMounted, ref } from 'vue';
  import { Chart } from 'chart.js/auto';

  export default {
    setup() {
      const sessionsChart = ref(null);

      onMounted(() => {
        if (sessionsChart.value) {
          new Chart(sessionsChart.value, {
            type: 'line',
            data: {
              labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
              datasets: [{
                label: 'Sessions',
                data: [30, 70, 150, 20, 50, 90, 80],
                borderColor: 'rgb(255,255,255)',
                backgroundColor: 'rgba(204,204,204,0.2)',
                borderWidth: 2,
                fill: true,
              }]
            },
            options: {
              responsive: true,
              maintainAspectRatio: false,
              scales: {
                x: {display: false},
                y: {display: false}
              },
              plugins: {
                legend: {display: false}
              }
            }
          });
        }
      });

      return {
        sessionsChart
      };
    }
  };



  definePageMeta({
    middleware: 'auth',  // Подключаем middleware для этой страницы
  });
</script>