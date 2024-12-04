<template>
  <NuxtLayout>
    <NuxtPage />
  </NuxtLayout>
</template>

<script setup>
    definePageMeta({
      middleware: 'auth',  // Подключаем middleware для этой страницы
    });
</script>