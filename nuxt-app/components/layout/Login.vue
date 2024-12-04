<template>
    <div class="relative">
      <div
        @click="toggleMenu"
        class="flex justify-center items-center cursor-pointer profile-button text-[var(--nav-text-color)] hover:text-[var(--hover-nav-color)]"
      >
        <Icon name="line-md:account" class="mr-2 text-[24px]" />
        <span v-if="loading" class="text-lg underline tracking-wider">Загрузка...</span>
        <span v-else-if="error" class="text-lg underline tracking-wider text-red-500">{{ error }}</span>
        <span v-else class="text-lg underline tracking-wider">
          {{ username }} (Уровень: {{ level || 'нет данных' }})
        </span>
      </div>
  
      <transition name="fade">
        <div
          v-if="menuVisible"
          ref="menu"
          class="absolute -right-7 top-full mt-2 bg-[var(--bg-nav-color)] border-2 border-[var(--bg-color)] rounded-xl shadow-2xl shadow-white z-50 w-52"
        >
          <div class="flex flex-col space-y-2 pb-2">
            <button
              class="flex justify-center items-center w-auto space-x-2 mx-2 py-2 px-4 text-[var(--nav-text-color)] hover:text-[var(--hover-nav-color)]"
            >
              <NuxtImg src="/avatar.png" width="100px" class="rounded-full border-[3px]" alt="avatar" />
            </button>
            <button
              @click="openProfile"
              class="flex justify-left items-center space-x-2 mx-2 pt-4 px-4 text-[var(--nav-text-color)] border-t-2 border-[var(--bg-color)] hover:text-[var(--hover-nav-color)] transition"
            >
              <Icon name="line-md:person" size="1.2em" />
              <span>Профиль</span>
            </button>
            <button
              @click="openSettings"
              class="flex justify-left items-center space-x-2 mx-2 pb-4 px-4 text-[var(--nav-text-color)] border-b-2 border-[var(--bg-color)] hover:text-[var(--hover-nav-color)] transition"
            >
              <Icon name="line-md:cog-loop" size="1.2em" />
              <span>Настройки</span>
            </button>
            <button
              @click="logout"
              class="flex justify-center items-center space-x-2 m-4 py-2 px-4 rounded-lg bg-red-500 text-[var(--nav-text-color)] hover:bg-red-700 transition"
            >
                <span>Выход</span>
                <Icon name="line-md:log-in" size="1.2em" />
            </button>
          </div>
        </div>
      </transition>
    </div>
</template>
  
<script setup>
import { ref, onBeforeUnmount, onMounted } from 'vue';
import { useRouter } from '#app';

const menuVisible = ref(false);

const username = ref(''); // Имя пользователя
const loading = ref(true); // Состояние загрузки
const error = ref(null); // Ошибки

const level = ref(null); // Новый state для уровня пользователя

const router = useRouter();

const fetchUserProfile = async () => {
  const token = localStorage.getItem('access_token');
  if (!token) {
    error.value = 'Токен отсутствует';
    router.push('/');
    return;
  }

  try {
    // console.log('Токен:', token);

    const response = await fetch('http://127.0.0.1:8000/api/api/user/', {
      method: 'GET',
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });

    // Проверяем только один раз
    if (response.ok) {
      const data = await response.json(); // Читаем тело только один раз
      console.log('Ответ сервера:', data);
      username.value = data.username;
      level.value = data.level; // Устанавливаем уровень пользователя
    } else {
      const errorData = await response.json();
      error.value = errorData.detail || 'Ошибка загрузки профиля';
      router.push('/');
    }
  } catch (err) {
    error.value = 'Ошибка соединения с сервером';
    console.error('Ошибка соединения:', err);
  } finally {
    loading.value = false; // Завершаем загрузку
  }
};

const toggleMenu = () => {
  menuVisible.value = !menuVisible.value;
  if (menuVisible.value) {
    document.addEventListener("click", handleClickOutside);
  } else {
    document.removeEventListener("click", handleClickOutside);
  }
};

const handleClickOutside = (event) => {
  if (
    !event.target.closest(".profile-button") &&
    !event.target.closest(".menu")
  ) {
    menuVisible.value = false;
    document.removeEventListener("click", handleClickOutside);
  }
};

const openProfile = () => {
  menuVisible.value = false;
  alert("Opening profile");
};

const openSettings = () => {
  menuVisible.value = false;
  alert("Opening settings");
};

const logout = () => {
  // Удаляем токены из localStorage
  localStorage.removeItem('access_token');
  localStorage.removeItem('refresh_token');
  
  // Перенаправляем пользователя на страницу логина
  router.push('/');
};

onBeforeUnmount(() => {
  document.removeEventListener("click", handleClickOutside);
});

onMounted(fetchUserProfile);
</script>

  
<style scoped>
  .fade-enter-active,
  .fade-leave-active {
    transition: opacity 0.5s ease, transform 0.5s ease;
  }
  .fade-enter {
    opacity: 0;
    transform: translateY(20px);
  }
  .fade-enter-to {
    opacity: 1;
    transform: translateY(0);
  }
  .fade-leave {
    opacity: 1;
    transform: translateY(0);
  }
  .fade-leave-to {
    opacity: 0;
    transform: translateY(20px);
  }
</style>
  