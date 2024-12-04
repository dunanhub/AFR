<template>
    <div class="flex justify-center items-center">
        <NuxtLink to="main" class="text-[var(--nav-text-color)] text-lg hover:text-[var(--hover-nav-color)] transition hover:scale-110 mx-5">
            <span>Домашняя страница</span>
        </NuxtLink>
        <NuxtLink to="statistics" class="text-[var(--nav-text-color)] text-lg hover:text-[var(--hover-nav-color)] transition hover:scale-110 mx-5">
            <span>Статистика</span>
        </NuxtLink>
        <NuxtLink to="analytics" class="text-[var(--nav-text-color)] text-lg hover:text-[var(--hover-nav-color)] transition hover:scale-110 mx-5">
            <span>Аналитика</span>
        </NuxtLink>
    </div>
</template>