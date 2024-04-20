<template>
	<div class="bg-gray-100 min-h-screen flex items-center justify-center">
		<div class="container max-w-lg p-6 bg-white rounded shadow-lg">
			<div class="flex items-center justify-center flex-col">
				<p class="text-gray-600 mt-2">Your name: {{ userStore.user.name }}</p>
				<p class="text-gray-600 mt-2">Your email: {{ userStore.user.email }}</p>
				<button @click="logOut" class="m-2 bg-blue-500 text-white font-medium py-2 px-4 rounded hover:bg-blue-600 transition-colors">Log Out</button>
			</div>
		</div>
	</div>
</template>

<script>
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
    
    methods: {
		
		handleAvatarChange(event) {
			this.selectedAvatar = event.target.files[0];
		},

		applyAvatar() {
			if (this.selectedAvatar) {
				this.avatar = URL.createObjectURL(this.selectedAvatar);
			}
		},

		logOut() {
			this.userStore.removeToken()
			this.$router.push('/')
		}
    },
};
</script>