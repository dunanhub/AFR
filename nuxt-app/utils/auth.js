// utils/auth.js
export async function refreshAccessToken() {
    try {
      const refreshToken = localStorage.getItem('refresh_token');
      if (!refreshToken) throw new Error('Refresh token отсутствует');
  
      const response = await fetch('http://127.0.0.1:8000/api/token/refresh/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ refresh: refreshToken }),
      });
  
      if (response.ok) {
        const data = await response.json();
        localStorage.setItem('access_token', data.access); // Обновляем access токен
        return data.access;
      } else {
        console.error('Ошибка обновления токена');
        return null;
      }
    } catch (error) {
      console.error('Ошибка обновления токена:', error);
      return null;
    }
  }
  