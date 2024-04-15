<template>
    <div class="bg-gray-100 min-h-screen">
      <div class="container mx-auto mt-8">
        <div class="bg-white shadow-lg p-4 rounded-lg">
          <h1 class="text-2xl font-bold mb-4">Search Friends</h1>
          <div class="flex items-center mt-4">
            <input v-model="searchName" type="text" placeholder="Search by Name" class="w-full border border-gray-300 rounded p-2 mr-2">
            <button @click="searchByName" class="bg-blue-500 text-white font-medium py-2 px-4 rounded hover:bg-blue-600 transition-colors">Search</button>
          </div>
          <div class="flex items-center mt-4">
            <input v-model="searchEmail" type="text" placeholder="Search by Email" class="w-full border border-gray-300 rounded p-2 mr-2">
            <button @click="searchByEmail" class="bg-blue-500 text-white font-medium py-2 px-4 rounded hover:bg-blue-600 transition-colors">Search</button>
          </div>
          <h2 class="text-xl mt-6 font-bold">Search Results</h2>
          <ul class="mt-4">
            <li v-for="user in searchResults" :key="user.id" class="bg-white shadow p-4 rounded-lg mb-4">
              <h3 class="text-lg font-semibold">{{ user.name }}</h3>
              <p class="text-gray-600">{{ user.email }}</p>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  export default {
    data() {
      return {
        searchName: '',
        searchEmail: '',
        searchResults: [],
      };
    },

    mounted() {
      this.getUsers()
    },

    methods: {
      searchByName() {
          axios.get('/api/search_by_name/?searchTerm=' + this.searchName)
              .then(response => {
                  this.searchResults = response.data;
              })
              .catch(error => {
                  console.log(error);
              });
      },
      searchByEmail() {
          axios.get('/api/search_by_email/?searchTerm=' + this.searchEmail)
              .then(response => {
                  this.searchResults = response.data;
              })
              .catch(error => {
                  console.log(error);
              });
      },

      getUsers() {
        axios
          .get(`/api/users/`)
          .then(response => {
          console.log('data', response.data)

          this.searchResults = response.data
          })
          .catch(error => {
          console.log('error', error)
          })
      }
    },
  };
  </script>
  