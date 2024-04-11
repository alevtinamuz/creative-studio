<template>
  <div class="bg-gray-100 min-h-screen">
    <nav class="bg-white shadow">
    </nav>
    <div class="container mx-auto mt-8">
      <div class="flex items-start">
        <div class="w-1/4">
          <div class="bg-white shadow-lg p-4 rounded-lg">
            <img :src="avatar" alt="Avatar" class="w-full h-auto rounded-lg">
            <div class="mt-4">
              <input ref="avatarInput" type="file" @change="handleAvatarChange" class="hidden">
              <button @click="$refs.avatarInput.click()" class="bg-blue-500 text-white font-medium py-2 px-4 rounded hover:bg-blue-600 transition-colors">Change Avatar</button>
              <button @click="applyAvatar" class="mt-2 bg-blue-500 text-white font-medium py-2 px-4 rounded hover:bg-blue-600 transition-colors">Apply Avatar</button>
            </div>
            <h2 class="text-xl font-bold mt-4">{{ name }}</h2>
            <p class="text-gray-600">{{ email }}</p>
          </div>
        </div>
        <div class="w-3/4 ml-8">
          <div class="bg-white shadow-lg p-4 rounded-lg">
            <h2 class="text-xl font-bold mb-4">Owned Canvases</h2>
            <div v-for="canvas in canvases" v-bind:key="canvas.id" class="mb-4">
              <h3 class="text-lg font-semibold">{{ canvas.name }}</h3>
              <p class="text-gray-800">{{ canvas.avatar }}</p>
              <p class="text-gray-600">{{ canvas.created_by.name }}</p>
			  <p class="text-gray-600">{{ canvas.created_at_formatted }} ago</p>
            </div>
            <div class="mt-4">
              <button @click="createCanvas" class="bg-blue-500 text-white font-medium py-2 px-4 rounded hover:bg-blue-600 transition-colors">Create Canvas</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
    data() {
		return {
			avatar: 'https://example.com/avatar.jpg',
			name: 'John Doe',
			email: 'johndoe@example.com',
			password: '',
			selectedAvatar: null,
			canvases: []
		};
    },

	mounted() {
		this.getCanvases()
	},
    
    methods: {
		getCanvases() {
			axios
				.get('/api/canvases/')
				.then(response => {
					console.log('data', response.data)

					this.canvases = response.data
				})
				.catch(error => {
					console.log('error', error)
				})
		},

		handleAvatarChange(event) {
			this.selectedAvatar = event.target.files[0];
		},

		applyAvatar() {
			// You can upload the file to a storage service and store the URL for later use
			// Add logic here to upload the file and store the URL
			// For this example, we'll just update the avatar with the selected file
			if (this.selectedAvatar) {
			this.avatar = URL.createObjectURL(this.selectedAvatar);
			}
		},

		createCanvas() {
			// Добавьте логику для создания холста
		}
    },
};
</script>