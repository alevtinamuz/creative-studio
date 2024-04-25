<template>
	<div class="bg-gray-100 min-h-screen">
		<h1></h1>
		<div class="grid grid-cols-4 gap-4">
			<div class="mb-6 bg-white shadow-lg p-4 rounded-lg flex items-center justify-center content-center">
				<router-link :to="{'name': 'create_canvas'}" class="flex items-center justify-center content-center text-9xl bg-blue-500 text-white px-10 pb-8 rounded leading-none">
					+
				</router-link>
			</div>
			<div v-for="canvas in canvases" v-bind:key="canvas.id" class="mb-6 bg-white shadow-lg p-4 rounded-lg flex flex-col items-center justify-center">
				<img :src="canvas.canvas_data" alt="canvas">
				<h3 class="text-lg font-semibold">{{ canvas.name }}</h3>
				<p class="text-gray-600">Created by {{ canvas.created_by.name }}</p>
				<p class="text-gray-600">{{ canvas.created_at_formatted }} ago</p>
				<button @click="getCanvas(canvas.id)" class="w-full bg-blue-500 text-white font-medium py-2 rounded hover:bg-blue-600 transition-colors">Edit</button>
				
			</div>
		</div>
		
		
	</div>
</template>
  
<script>
import axios from 'axios'
import { useUserStore } from '@/stores/user'
// import router from '@/router';

export default {
	data() {
		return {
			canvases: [],
			canvases_id: [],
		};
	},

	setup() {
		const userStore = useUserStore()

		return {
		userStore
		}
	},

	mounted() {
		this.getCanvasesIdByUser()
		this.getCanvasesByUser()
	},
		
	methods: {

		getCanvas(id) {
			sessionStorage.setItem('canvas_id', id)
			this.$router.push({name: 'edit_canvas', params:{'id': id}})
		},

		getCanvasesByUser() {
			// console.log(this.canvases_id)
			this.canvases_id.forEach(canvas_id => {
				console.log(555)
				axios.get('/api/canvases/' + canvas_id + '/')
					.then(response => {
						
						this.canvases.push(response.data)
						// console.log(response.data.canv.split(',').filter(id => id != ''))
						console.log(response.data)
					})
					.catch((error) => {
						console.error(error);
					});
			});
		},

		getCanvasesIdByUser() {
			axios.get('/api/' + sessionStorage.getItem('user.id') + '/get_canv/')
                .then(response => {
					if (response.data != null)
						this.canvases_id = response.data.canv.split(',').filter(id => id != '')
						this.canvases_id.forEach(canvas_id => {
							console.log(555)
							axios.get('/api/canvases/' + canvas_id + '/')
								.then(response => {
									
									this.canvases.push(response.data)
									// console.log(response.data.canv.split(',').filter(id => id != ''))
									console.log(response.data)
								})
								.catch((error) => {
									console.error(error);
								});
						});
                })
                .catch((error) => {
                    console.error(error);
                });

		}
	},
};
</script>