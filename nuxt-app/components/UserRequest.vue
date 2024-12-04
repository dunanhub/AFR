<template>
    <div class="flex flex-col justify-center items-center bg-[var(--bg-card-color)] text-white rounded-lg">
        <div class="flex flex-col justify-center items-start w-full p-4 text-left text-[20px] tracking-[2px] font-bold relative">
            <span>Запросы из Чата</span>
            <span class="absolute bottom-2 right-2 block text-[8px] font-medim text-[var(--text-card-opacity-color)] opacity-100 p-2 bg-[var(--bg-card-opacity-color)] rounded-xl">Прошлая Неделя</span>
        </div>
        
        <div class="flex items-start w-full p-4 text-left py-2 text-[30px] text-[var(--bg-card-color)] font-medium bg-[var(--bg-color)] border-x-[3px] border-[var(--bg-card-color)]">
            <span class="underline">24.5k</span>
            <div class="flex flex-col justify-start items-left ml-3 w-full">
                <span class="text-[16px] text-green-500">+15.5%</span>
                <span class="text-[16px] text-red-500">-20%</span>
            </div>
        </div>

        <div class="w-full bg-[var(--bg-color)] border-x-[3px] border-b-[3px] border-[var(--bg-card-color)] rounded-b-lg">
            <SessionChart :data="[20, 80, 60, 200, 300, 50, 180]" />
        </div>
    </div>
</template>

<script>
import SessionChart from '~/components/chart/SessionChart.vue';

export default {
  components: {
    SessionChart,
  },
};
</script>