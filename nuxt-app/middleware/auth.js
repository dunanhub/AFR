// middleware/auth.js
import { refreshAccessToken } from '~/utils/auth';

export default defineNuxtRouteMiddleware(async (to, from) => {
  if (process.server) return;

  let token = localStorage.getItem('access_token');

  if (!token) {
    token = await refreshAccessToken(); // Попытка обновления токена
  }

  if (!token && to.path !== '/auth/SignIn') {
    return navigateTo('/');
  }
});
