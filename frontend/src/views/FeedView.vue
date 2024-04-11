<template>
	<div class="bg-gray-100 min-h-screen">
		<nav class="bg-white shadow"></nav>
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
						<h2 class="text-xl font-bold mt-4">{{ userStore.user.name }}</h2>
						<p class="text-gray-600">{{ userStore.user.email }}</p>
					</div>
				</div>
				<div class="w-3/4 ml-8">
					<div class="bg-white shadow-lg p-4 rounded-lg">
						<h2 class="text-xl font-bold mb-4">Create new canvas</h2>
						<div class="mt-4">
							<form v-on:submit.prevent="submitForm" method="createCanvas">
								<div>
									<label for="name-canvas" class="text-gray-700 font-medium">Name</label>
									<input v-model="name_canvas" type="name-canvas" id="name-canvas" class="w-full border border-gray-300 rounded p-2 mt-1" />
								</div>
								<button class="mt-4 mb-8 bg-blue-500 text-white font-medium py-2 px-4 rounded hover:bg-blue-600 transition-colors">Create Canvas</button>
							</form>
						</div>
						<h2 class="text-xl font-bold mb-4">Owned Canvases</h2>
						<div v-for="canvas in canvases" v-bind:key="canvas.id" class="mb-6">
							<h3 class="text-lg font-semibold">{{ canvas.name }}</h3>
							<p class="text-gray-800">{{ canvas.avatar }}</p>
							<p class="text-gray-600">{{ canvas.created_by.name }}</p>
							<p class="text-gray-600">{{ canvas.created_at_formatted }} ago</p>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import axios from 'axios'
import { useUserStore } from '@/stores/user'

export default {
    data() {
		return {
			avatar: 'https://example.com/avatar.jpg',
			name: 'John',
			email: 'j',
			password: '',
			selectedAvatar: null,
			canvases: [],
			name_canvas: '',
		};
    },

	setup() {
		const userStore = useUserStore()

		return {
			userStore
		}
	},

	mounted() {
		this.getCanvases()
	},
    
    methods: {
		getCanvases() {
			axios
				.get(`/api/canvases/feed/${this.$route.params.id}/`)
				.then(response => {
					console.log('data', response.data)

					this.canvases = response.data
				})
				.catch(error => {
					console.log('error', error)
				})
		},

		submitForm() {
			axios
				.post('/api/canvases/create/', {
					'name': this.name_canvas
				})
				.then(response => {
					console.log('data', response.data)

					this.canvases.unshift(response.data)
					this.name_canvas = ''
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
		}
    },
};
</script>