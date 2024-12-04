<template>
    <div class="login-page">
      <span class="circle top-left"></span>
      <span class="circle bottom-right"></span>
      <form class="login-block" @submit.prevent="handleSubmit">
        <NuxtImg src="/logo/AFR_rus.png" width="200px" class="logo" />
        <div class="form-group">
          <label for="email" class="label">Username:</label>
          <input
            type="text"
            id="username"
            v-model="form.username"
            class="input"
            required
          />
        </div>
        <div class="form-group">
          <label for="password" class="label">Пароль:</label>
          <input
            type="password"
            id="password"
            v-model="form.password"
            class="input"
            required
          />
        </div>
        <button type="submit" class="button">Войти в систему</button>
      </form>
    </div>
</template>

<script setup>
import { reactive } from "vue";
import { useRouter } from "#app";

const router = useRouter();

const form = reactive({
  username: "",
  password: "",
});

const handleSubmit = async () => {
  try {
    const response = await fetch("http://127.0.0.1:8000/api/login/", {
      method: "POST", // Убедитесь, что здесь именно POST
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        username: form.username,
        password: form.password,
      }),
    });

    // Обработка ответа
    if (response.ok) {
      const data = await response.json();
      localStorage.setItem('access_token', data.access); // Сохраняем токен
      localStorage.setItem('refresh_token', data.refresh); // Сохраняем refresh токен
      router.push('/main'); // Перенаправляем на нужную страницу
    } else {
      const errorData = await response.json();
      alert(`Ошибка: ${errorData.error || "Неизвестная ошибка"}`);
    }
  } catch (error) {
    console.error("Ошибка соединения:", error);
    alert("Ошибка соединения с сервером!");
  }
};
</script>

<style scoped>
  /* Wrapper for the entire login page */
  .login-page {
    position: relative;
    width: 100vw;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: #f9f9f9;
    overflow: hidden;
  }
  
  /* Circle decorations */
  .circle {
    position: absolute;
    width: 700px;
    height: 700px;
    border: 10px solid var(--bg-nav-color);
    border-radius: 50%;
    overflow: hidden;
  }
  
  .top-left {
    top: -300px;
    left: -300px;
  }
  
  .bottom-right {
    bottom: -300px;
    right: -300px;
  }
  
  /* Logo */
  .logo {
    display: block;
    /* margin: 0 auto 1.5rem; */
  }
  
  /* Form block */
  .login-block {
    z-index: 2;
    max-width: 400px;
    width: 100%;
    padding: 2rem;
    background: #fff;
    border: 1px solid #ddd;
    border-radius: 8px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    text-align: center;
  }
  
  /* Form group */
  .form-group {
    margin-bottom: 1.5rem;
  }
  
  /* Label */
  .label {
    display: block;
    margin-bottom: 0.5rem;
    font-size: 14px;
    font-weight: 600;
    color: #333;
    text-align: left;
  }
  
  /* Input */
  .input {
    width: 100%;
    padding: 0.75rem;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 14px;
    color: #333;
    background: #f9f9f9;
  }
  
  .input:focus {
    border-color: #007bff;
    outline: none;
    box-shadow: 0 0 0 3px rgba(0, 123, 255, 0.25);
  }
  
  /* Button */
  .button {
    display: inline-block;
    width: 100%;
    padding: 0.75rem;
    font-size: 14px;
    font-weight: bold;
    color: #fff;
    background: var(--bg-nav-color);
    border: none;
    border-radius: 4px;
    cursor: pointer;
    text-align: center;
    transition: background 0.3s;
  }
  
  .button:hover {
    background: var(--btn-hover);
  }
  
  .button:focus {
    outline: none;
    box-shadow: 0 0 0 3px rgba(0, 123, 255, 0.25);
  }
</style>
  