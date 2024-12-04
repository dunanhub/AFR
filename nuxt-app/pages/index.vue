<template>
    <div>
      <SignIn />
    </div>
</template>


<script>
import SignIn from '~/auth/components/SignIn.vue'; // Импортируем компонент

export default {
  components: {
    SignIn, // Регистрируем компонент в `components`
  },
};
</script>