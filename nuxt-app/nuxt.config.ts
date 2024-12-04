export default defineNuxtConfig({
  devtools: { enabled: true },
  css: ['~/assets/css/main.css'],
  postcss: {
    plugins: {
      tailwindcss: {},
      autoprefixer: {},
    },
  },
  compatibilityDate: "2024-11-08",
  modules: [
    "@nuxt/image",
    "@nuxt/icon",
  ],
  runtimeConfig: {
    public: {
      apiBase: 'http://127.0.0.1:8000/api', // Настройка API
    },
  },
})
