<template>
	<div class="bg-gray-100 min-h-screen">
		<div v-for="canvas in canvases" v-bind:key="canvas.id" class="mb-6 bg-white shadow-lg p-4 rounded-lg">
			<h3 class="text-lg font-semibold">{{ canvas.name }}</h3>
			<p class="text-gray-800">{{ canvas.avatar }}</p>
			<p class="text-gray-600">{{ canvas.created_by.name }}</p>
			<p class="text-gray-600">{{ canvas.created_at_formatted }} ago</p>
			<button class="w-full bg-blue-500 text-white font-medium py-2 rounded hover:bg-blue-600 transition-colors">Edit</button>
		</div>
		
	</div>
</template>
  
<script>
import axios from 'axios'
import { useUserStore } from '@/stores/user'

export default {
	data() {
		return {
			canvases: []
		};
	},

	setup() {
		const userStore = useUserStore()

		return {
		userStore
		}
	},

	mounted() {
		this.getCanvasesByUser()
	},
		
	methods: {
		getCanvases() {
			axios
				.get(`/api/canvases/`)
				.then(response => {
				console.log('data', response.data)

				this.canvases = response.data
				})
				.catch(error => {
				console.log('error', error)
				})
		},

		getCanvasesByUser() {
			axios.get('/api/canvases/search_canvas_by_user/?searchTerm=' + this.userStore.user.name)
              .then(response => {
                  this.canvases = response.data;
              })
              .catch(error => {
                  console.log(error);
              });
		}
	},
};
</script>