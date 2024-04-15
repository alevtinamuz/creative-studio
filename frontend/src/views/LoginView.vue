<template>
    <div class="bg-gray-100 min-h-screen flex flex-col">
        <nav class="bg-white shadow-lg">
            <!-- Navigation Bar -->
        </nav>
        <div class="flex-grow bg-gray-100 flex items-center justify-center">
            <div class="max-w-lg p-6 bg-white rounded shadow-lg">
                <h1 class="text-2xl font-bold mb-6">Login</h1>
                <form v-on:submit.prevent="submitForm" class="space-y-4">
                    <div>
                        <label for="email" class="text-gray-700 font-medium">Email</label>
                        <input v-model="form.email" type="email" class="w-full border-2 border-blue-500 focus:outline-none focus:ring-1 focus:ring-blue-500 rounded p-2 mt-1" />
                    </div>
                    <div>
                        <label for="password" class="text-gray-700 font-medium">Password</label>
                        <input v-model="form.password" type="password" class="w-full border-2 border-blue-500 focus:outline-none focus:ring-1 focus:ring-blue-500 rounded p-2 mt-1" />
                    </div>

                    <template v-if="errors.length > 0">
                        <div class="bg-red-300 text-white rounded-lg p-6">
                            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                        </div>
                    </template>

                    <div>
                        <button type="submit" class="w-full bg-blue-500 text-white font-medium py-2 rounded hover:bg-blue-600 transition-colors">Log in</button>
                    </div>
                </form>
                <div class="text-center mt-4">
                    <p class="text-gray-600">Don't have an account? <router-link :to="{'name': 'signup'}" class="underline">Click here</router-link> to sign up!</p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

import { useUserStore } from '@/stores/user'

export default {
    setup() {
        const userStore = useUserStore()

        return {
            userStore
        }
    },

    data() {
        return {
            form: {
                email: '',
                password: '',
            },
            errors: []
        }
    },
    methods: {
        async submitForm() {
            this.errors = []

            if (this.form.email === '') {
                this.errors.push('Your e-mail is missing')
            }

            if (this.form.password === '') {
                this.errors.push('Your password is missing')
            }

            if (this.errors.length === 0) {
                await axios
                    .post('/api/login/', this.form)
                    .then(response => {
                        this.userStore.setToken(response.data)

                        axios.defaults.headers.common["Authorization"] = "Bearer " + response.data.access;
                    })
                    .catch(error => {
                        console.log('error', error)
                    })
                
                await axios
                    .get('/api/me/')
                    .then(response => {
  
                        this.userStore.setUserInfo(response.data)

                        this.$router.push('/')
                    })
                    .catch(error => {
                        console.log('error', error)
                    })
            }
        }
    }
}
</script>