<template>
    <div class="bg-gray-100 min-h-screen">
      <nav class="bg-white shadow">
        <!-- Навигационное меню -->
      </nav>
      <div class="container mx-auto mt-8">
        <div class="bg-white shadow-lg p-4 rounded-lg">
          <h1 class="text-2xl font-bold mb-4">Search Canvases</h1>
          <div class="flex items-center mt-2">
            <input v-model="searchId" type="text" placeholder="Search by ID" class="w-full border border-gray-300 rounded p-2 mr-2">
            <button @click="searchById" class="bg-blue-500 text-white font-medium py-2 px-4 rounded hover:bg-blue-600 transition-colors">Search</button>
          </div>
          <div class="flex items-center mt-4">
            <input v-model="searchName" type="text" placeholder="Search by Name" class="w-full border border-gray-300 rounded p-2 mr-2">
            <button @click="searchByName" class="bg-blue-500 text-white font-medium py-2 px-4 rounded hover:bg-blue-600 transition-colors">Search</button>
          </div>
          <h2 class="text-xl mt-6 font-bold">Search Results</h2>
          <ul class="mt-4">
            <li v-for="canvas in searchResults" :key="canvas.id" class="bg-white shadow p-4 rounded-lg mb-4">
              <h3 class="text-lg font-semibold">{{ canvas.name }}</h3>
              <p class="text-gray-600">{{ canvas.description }}</p>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        searchId: '',
        searchName: '',
        searchResults: [],
      };
    },
    methods: {
      searchById() {
        // Добавьте логику для поиска холста по ID
        // Выполните запрос к серверу и обновите массив searchResults
      },
      searchByName() {
        // Добавьте логику для поиска холста по названию
        // Выполните запрос к серверу и обновите массив searchResults
      },
    },
  };
  </script>