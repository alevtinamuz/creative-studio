<template>
	<div class="bg-gray-100 min-h-screen flex flex-col">
		<nav class="bg-white shadow-lg">
		</nav>
		<div class="flex-grow bg-gray-100 flex items-center justify-center">
		<div class="max-w-lg p-6 bg-white rounded shadow-lg">
			<h1 class="text-2xl font-bold mb-6">Registration</h1>
			<form v-on:submit.prevent="submitForm" class="space-y-4">
				<div>
					<label for="name" class="text-gray-700 font-medium">Name</label>
					<input v-model="form.name" type="text" id="name" class="w-full border border-gray-300 rounded p-2 mt-1" />
				</div>
				<div>
					<label for="email" class="text-gray-700 font-medium">Email</label>
					<input v-model="form.email" type="email" id="email" class="w-full border border-gray-300 rounded p-2 mt-1" />
				</div>
				<div>
					<label for="password" class="text-gray-700 font-medium">Password</label>
					<input v-model="form.password1" type="password" id="password" class="w-full border border-gray-300 rounded p-2 mt-1" />
				</div>
				<div>
					<label for="confirmPassword" class="text-gray-700 font-medium">Confirm Password</label>
					<input v-model="form.password2" type="password" id="confirmPassword" class="w-full border border-gray-300 rounded p-2 mt-1" />
				</div>

				<template v-if="errors.length > 0">
					<div class="bg-red-300 text-white rounded-lg p-6">
						<p v-for="error in errors" v-bind:key="error">{{ error }}</p>
					</div>
				</template>

				<div>
					<button type="submit" class="w-full bg-green-500 text-white font-medium py-2 rounded hover:bg-green-600 transition-colors">Register</button>
				</div>
			</form>
			<div class="text-center mt-4">
			<p class="text-gray-600">Already have an account? <router-link :to="{'name': 'login'}" class="underline">Click here</router-link> to log in!</p>
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
            form: {
                email: '',
                name: '',
                password1: '',
                password2: ''
            },
            errors: [],
        }
    },

    methods: {
        submitForm() {
            this.errors = []

            if (this.form.email === '') {
                this.errors.push('Your e-mail is missing')
            }

            if (this.form.name === '') {
                this.errors.push('Your name is missing')
            }

            if (this.form.password1 === '') {
                this.errors.push('Your password is missing')
            }

            if (this.form.password1 !== this.form.password2) {
                this.errors.push('The password does not match')
            }

            if (this.errors.length === 0) {
                axios
                    .post('/api/signup/', this.form)
                    .then(response => {
					
						this.form.email = ''
						this.form.name = ''
						this.form.password1 = ''
						this.form.password2 = ''
                        
                    })
                    .catch(error => {
                        console.log('error', error)
                    })
            }
        }
    }
}
</script>