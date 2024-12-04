<template>
    <div>
        <LayoutHeader />
    </div>
</template>

<script>
    export default {
        middleware: 'auth',
    };
</script>