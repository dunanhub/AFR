<template>
    <section>
        <slot />
    </section>
</template>

<script setup>
    definePageMeta({
      middleware: 'auth',  // Подключаем middleware для этой страницы
    });
</script>