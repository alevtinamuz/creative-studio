<template>
    <div class="bg-gray-100 min-h-screen flex flex-col">
        <nav class="bg-white shadow-lg">
            <div class="container px-4 mx-auto">
                <div class="flex justify-between items-center h-16">
                    <div>
                        <router-link :to="{'name': 'home'}" class="font-bold text-lg">Home</router-link>
                    </div>
                    <div class="flex" v-if="userStore.user.isAuthenticated">
                        <router-link :to="{name: 'feed', params:{'id': userStore.user.id}}" class="mr-4">My account</router-link>
                        <router-link :to="{'name': 'search_canvases'}" class="mr-4">My canvases</router-link>
                    </div>
                    <div class="flex" v-else>
                        <router-link :to="{'name': 'signup'}" class="mr-4">Sign up</router-link>
                        <router-link :to="{'name': 'login'}" class="mr-4">Log in</router-link>
                    </div>
                </div>
            </div>
            <RouterView/>
        </nav>
    </div>
</template>

<script>
import axios from 'axios';
import { useUserStore } from '@/stores/user'

export default {
    setup() {
        const userStore = useUserStore()

        return {
            userStore
        }
    },

    beforeCreate() {
        this.userStore.initStore()

        const token = this.userStore.user.access
        if (token) {
            axios.defaults.headers.common["Authorization"] = "Bearer " + token;
        } else {
            axios.defaults.headers.common["Authorization"] = "";
        }
    }
}
</script>

