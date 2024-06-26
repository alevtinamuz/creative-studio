import { defineStore } from 'pinia'
import axios from 'axios'

export const useUserStore = defineStore({
    id: 'user',
    
    state: () => ({
        user: {
            isAuthenticated: false,
            id: null,
            name: null,
            email: null, 
            access: null, 
            refresh: null,
        }
    }),

    actions: {
        initStore() {
            console.log('initStore', sessionStorage.getItem('user.access'))

            if (sessionStorage.getItem('user.access')) {
                console.log('User has access!')

                this.user.access = sessionStorage.getItem('user.access')
                this.user.refresh = sessionStorage.getItem('user.refresh')
                this.user.id = sessionStorage.getItem('user.id')
                this.user.name = sessionStorage.getItem('user.name')
                this.user.email = sessionStorage.getItem('user.email')
                this.user.isAuthenticated = true

                this.refreshToken()

                console.log('Initialized user:', this.user)
            }
        },

        setToken(data) {
            console.log('setToken', data)

            this.user.access = data.access
            this.user.refresh = data.refresh
            this.user.isAuthenticated = true

            sessionStorage.setItem('user.access', data.access)
            sessionStorage.setItem('user.refresh', data.refresh)

            console.log('user.access: ', sessionStorage.getItem('user.access'))
        },

        removeToken() {
            console.log('removeToken')

            this.user.refresh = null
            this.user.access = null
            this.user.isAuthenticated = false
            this.user.id = false
            this.user.name = false
            this.user.email = false

            sessionStorage.setItem('user.access', '')
            sessionStorage.setItem('user.refresh', '')
            sessionStorage.setItem('user.id', '')
            sessionStorage.setItem('user.name', '')
            sessionStorage.setItem('user.email', '')
        },

        setUserInfo(user) {
            console.log('setUserInfo', user)

            this.user.id = user.id
            this.user.name = user.name
            this.user.email = user.email

            sessionStorage.setItem('user.id', this.user.id)
            sessionStorage.setItem('user.name', this.user.name)
            sessionStorage.setItem('user.email', this.user.email)

            console.log('User', this.user)
        },

        refreshToken() {
            axios.post('/api/refresh/', {
                refresh: this.user.refresh
            })
                .then((response) => {
                    this.user.access = response.data.access

                    sessionStorage.setItem('user.access', response.data.access)

                    axios.defaults.headers.common["Authorization"] = "Bearer " + response.data.access
                })
                .catch((error)=>{
                    console.log(error)

                    this.removeToken()
                })
        },
    }
})