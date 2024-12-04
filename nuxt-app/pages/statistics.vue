<template>
    <div>
        <LayoutHeader />
        <br>
        <MapComponent />
    </div>
</template>

<script>
    import MapComponent from "~/components/layout/MapComponent.vue";

    export default {
        components: {
            MapComponent,
        },
    };


    
    definePageMeta({
        middleware: 'auth',  // Подключаем middleware для этой страницы
    });
</script>