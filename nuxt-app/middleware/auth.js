export default defineNuxtRouteMiddleware(async (to, from) => {
  if (process.server) return;  // Не выполняем код на сервере

  if (process.client) {
    let token = localStorage.getItem('access_token');
    if (!token) {
      // Попытка обновить токен, если он отсутствует
      token = await refreshAccessToken();
    }

    if (!token && to.path !== '/auth/SignIn') {
      return navigateTo('/');  // Перенаправление, если токен отсутствует
    }
  }
});
