<template>

	<div class="bg-gray-100 min-h-screen">
		<div class="container mx-auto mt-8">
        <div class="bg-white shadow-lg p-4 rounded-lg">
            <div class="flex justify-center items-center">
          <button @click="setColor('white')" :class="{ 'border-black border-2': color == 'white' }" class="w-10 h-10 rounded-full bg-white mr-2 hover:border-black hover:border-2 text-xs">eraser</button>
          <button @click="setColor('black')" :class="{ 'border-white border-2': color == 'black' }" class="w-10 h-10 rounded-full bg-black mr-2 hover:border-white hover:border-2"></button>
          <button @click="setColor('red')" :class="{ 'border-black border-2': color == 'red' }" class="w-10 h-10 rounded-full bg-red-500 mr-2 hover:border-black hover:border-2" ></button>
          <button @click="setColor('blue')" :class="{ 'border-black border-2': color == 'blue' }" class="w-10 h-10 rounded-full bg-blue-500 mr-2 hover:border-black hover:border-2"></button>
          <button @click="setColor('green')" :class="{ 'border-black border-2': color == 'green' }" class="w-10 h-10 rounded-full bg-green-500 mr-2 hover:border-black hover:border-2"></button>
          <button @click="setColor('purple')" :class="{ 'border-black border-2': color == 'purple' }" class="w-10 h-10 rounded-full bg-purple-500 mr-2 hover:border-black hover:border-2"></button>
          <button @click="setColor('orange')" :class="{ 'border-black border-2': color == 'orange' }" class="w-10 h-10 rounded-full bg-amber-500 mr-2 hover:border-black hover:border-2"></button>
          <button @click="setColor('yellow')" :class="{ 'border-black border-2': color == 'yellow' }" class="w-10 h-10 rounded-full bg-yellow-300 mr-2 hover:border-black hover:border-2"></button>
          <button @click="setColor('pink')" :class="{ 'border-black border-2': color == 'pink' }" class="w-10 h-10 rounded-full bg-pink-300 mr-2 hover:border-black hover:border-2"></button>
          <button @click="setColor('deepPink')" :class="{ 'border-black border-2': color == 'deepPink' }" class="w-10 h-10 rounded-full bg-pink-500 mr-2 hover:border-black hover:border-2"></button>
          <button @click="setColor('cyan')" :class="{ 'border-black border-2': color == 'cyan' }" class="w-10 h-10 rounded-full bg-cyan-300 mr-2 hover:border-black hover:border-2"></button>
          <button @click="setColor('teal')" :class="{ 'border-black border-2': color == 'teal' }" class="w-10 h-10 rounded-full bg-teal-600 mr-2 hover:border-black hover:border-2"></button>
          <button @click="setColor('LawnGreen')" :class="{ 'border-black border-2': color == 'LawnGreen' }" class="w-10 h-10 rounded-full bg-lime-400 mr-2 hover:border-black hover:border-2"></button>
          <button @click="setColor('MediumSlateBlue')" :class="{ 'border-black border-2': color == 'MediumSlateBlue' }" class="w-10 h-10 rounded-full bg-indigo-500 mr-2 hover:border-black hover:border-2"></button>
          <button @click="setColor('violet')" :class="{ 'border-black border-2': color == 'violet' }" class="w-10 h-10 rounded-full bg-fuchsia-400 mr-2 hover:border-black hover:border-2"></button>
          <button @click="setColor('DodgerBlue')" :class="{ 'border-black border-2': color == 'DodgerBlue' }" class="w-10 h-10 rounded-full bg-sky-500 mr-2 hover:border-black hover:border-2"></button>
          <button @click="setColor('MediumAquamarine')" :class="{ 'border-black border-2': color == 'MediumAquamarine' }" class="w-10 h-10 rounded-full bg-emerald-500 mr-2 hover:border-black hover:border-2"></button>
          <button @click="setColor('gray')" :class="{ 'border-black border-2': color == 'gray' }" class="w-10 h-10 rounded-full bg-gray-500 mr-2 hover:border-black hover:border-2"></button>
        </div>
        <div class="flex justify-center items-center mb-5">
          <button @click="setLineWidth(1)" :class="{ 'border-black border-2': lineWidth == 1 }" class="w-10 h-10 rounded-full bg-gray-400 mr-2 hover:border-black hover:border-2 " title="Thin"><div style="height: 2px; background-color: black; margin-top: -2px; width: calc(100%); margin-left: 0px;">
  </div></button>
          <button @click="setLineWidth(3)" :class="{ 'border-black border-2': lineWidth == 3 }" class="w-10 h-10 rounded-full bg-gray-400 mr-2 hover:border-black hover:border-2" title="Medium"><div style="height: 4px; background-color: black; margin-top: -2px; width: calc(100%); margin-left: 0px;">
  </div></button>
          <button @click="setLineWidth(5)" :class="{ 'border-black border-2': lineWidth == 5 }" class="w-10 h-10 rounded-full bg-gray-400 mr-2 hover:border-black hover:border-2" title="Thick"><div style="height: 6px; background-color: black; margin-top: -2px; width: calc(100%); margin-left: 0px;">
  </div></button>
        </div>
            <div class="flex justify-center">
                <canvas :ref="'canvas'" @mousedown="startDrawing" @mousemove="draw" @mouseup="stopDrawing" @mouseleave="stopDrawing" class="rounded border border-gray-300"></canvas>
            </div>
            </div>
            <div class="bg-white shadow-lg p-4 rounded-lg">
                <div class="flex flex-col items-center justify-center">
                <h1 class="text-xl my-6 font-bold">Collaborators</h1>
                <ul class="grid grid-cols-4 gap-4">
                    <li v-for="user in collaborators" :key="user" class="bg-white shadow p-4 rounded-lg mb-4">
                        <h3 class="text-center text-lg font-semibold">{{ user.name }}</h3>
                        <p class="text-center text-gray-600">{{ user.email }}</p>
                        <p v-if="onlineUsersId.includes(user.id)" class="text-center text-green-400">online</p>
                        <p v-if="!onlineUsersId.includes(user.id)" class="text-center text-gray-600">offline</p>
                    </li>
                </ul>
                </div>
            
                <div class="flex flex-row items-center justify-center">

                    <button v-if="!search" @click="searchTrue" class="m-5 bg-blue-500 text-white font-medium py-2 px-4 rounded hover:bg-blue-600 transition-colors">Add collaborators</button>
                    
                    <button @click="deleteCanvas" class="m-5 bg-red-500 text-white font-medium py-2 px-4 rounded hover:bg-red-600 transition-colors">Delete this canvas</button>
                
                </div>
            </div>
            

            <div v-if="search">
                <div class="bg-white shadow-lg p-4 rounded-lg">
                    <div class="flex items-center justify-center">
                        <button @click="saveCollaborators" class=" m-5 bg-blue-500 text-white font-medium py-2 px-4 rounded hover:bg-blue-600 transition-colors text-center">Save collaborators</button>
                    </div>
                
                <h1 class="text-2xl font-bold mb-4 text-center">Search collaborators</h1>
                <div class="flex items-center mt-4">
                    <input v-model="searchName" type="text" placeholder="Search by Name" class="w-full border border-gray-300 rounded p-2 mr-2">
                    <button @click="searchByName" class="bg-blue-500 text-white font-medium py-2 px-4 rounded hover:bg-blue-600 transition-colors">Search</button>
                </div>
                <div class="flex items-center mt-4">
                    <input v-model="searchEmail" type="text" placeholder="Search by Email" class="w-full border border-gray-300 rounded p-2 mr-2">
                    <button @click="searchByEmail" class="bg-blue-500 text-white font-medium py-2 px-4 rounded hover:bg-blue-600 transition-colors">Search</button>
                </div>
                <h2 class="text-xl mt-6 font-bold text-center">Search Results</h2>
                <ul class="mt-4">
                    <div class="grid grid-cols-4 gap-4">
                        <li v-for="user in searchResults" :key="user.id" class="bg-white shadow p-4 rounded-lg mb-4">
                        <h3 class="text-lg font-semibold text-center">{{ user.name }}</h3>
                        <p class="text-gray-600 text-center">{{ user.email }}</p>
                        <button v-if="!collaborators_id.includes(user.id) && !saved_collaborators_id.includes(user.id)" @click="addCollaborator(user.id) && !saved_collaborators_id.includes(user.id)" class=" w-full my-5 bg-blue-500 text-white font-medium py-2 px-4 rounded hover:bg-blue-600 transition-colors">Add</button>
                        <button v-if="collaborators_id.includes(user.id) && !saved_collaborators_id.includes(user.id)" @click="deleteCollaborator(user.id)" class="w-full my-5 bg-white border-2 border-blue-500 focus:outline-none focus:ring-1 focus:ring-blue-500 text-blue-500 font-medium py-2 px-4 rounded transition-colors">Added</button>
                        </li>
                    </div>
                    
                </ul>
                </div>
            </div>

        </div>
	</div>
</template>
  
<script>
import axios from 'axios';
import { ref, onBeforeUnmount } from 'vue'

  export default {

    

    data() {
      return {
        search: false,
        drawing: false,
        color: 'black',
        lineWidth: 1,
		name_canvas: '',
        canvas_data: '',
        collaborators_id: [],
        searchResults: [],
        saved_collaborators_id: [],
        onlineUsersCount: 0,
        messages: [],
        onlineUsers: [],
        collaborators: [],
        onlineUsersId: [],
      };
    },

    mounted() {
        this.canvas = this.$refs.canvas;
        this.canvas.width = 1500;
        this.canvas.height = 400;
        this.context = this.canvas.getContext('2d');
        this.getCanvasData();
        this.getCollaborators();

        this.socket = ref(null) // Создаем реактивный объект для хранения ссылки на WebSocket
  
      // Открываем соединение WebSocket
        this.socket.value = new WebSocket('ws://localhost:8000/ws/');
    
        // Обработчик события открытия соединения
        this.socket.value.onopen = () => {
            const user = { id: sessionStorage.getItem('user.id'), name: sessionStorage.getItem('user.name'), currentCanvas: sessionStorage.getItem('canvas_id') };
            this.socket.value.send(JSON.stringify({ type: 'user_info', user: user }));
        };
    
        // Обработчик события закрытия соединения
        this.socket.value.onclose = () => {
            const user = { id: sessionStorage.getItem('user.id'), name: sessionStorage.getItem('user.name'), currentCanvas: sessionStorage.getItem('canvas_id') };
            this.socket.value.send(JSON.stringify({ type: 'user_out', user: user }));
        };
    
        // Обработчик события получения сообщения
        this.socket.value.onmessage = (event) => {
            const data = JSON.parse(event.data);
            this.onlineUsers = data.users.map((user) => user = JSON.stringify(user));
            this.onlineUsers = Array.from(new Set(this.onlineUsers));
            this.onlineUsers = this.onlineUsers.map((user) => user = JSON.parse(user));
            this.onlineUsers = this.onlineUsers.filter((user) => {
                return user.currentCanvas == sessionStorage.getItem('canvas_id')
            })
            this.onlineUsersCount = this.onlineUsers.length

            this.onlineUsersId = []

            this.onlineUsers.forEach(user => {
                this.onlineUsersId.push(user.id)
            });

            this.getCanvasData()
            console.log(this.onlineUsers)

        };
    
        // Обработчик жизненного цикла beforeUnmount
        onBeforeUnmount(() => {
            if (this.socket.value) {
                this.socket.value.close()
            }
        })
    },

    methods: {

        getCollaborators() {
            axios.get('/api/canvases/' + sessionStorage.getItem('canvas_id') + '/get_users/')
                .then(response => {
                    this.saved_collaborators_id = response.data.users.split(',').filter(id => id != '');

                    this.saved_collaborators_id.forEach(id => {
                        axios.get('/api/' + id + '/')
                            .then(response => {
                                this.collaborators.push(response.data)
                                
                            })
                            .catch(error => {
                                console.log(error);
                            });
                    });
                    axios
                        .get(`/api/users/`)
                        .then(response => {

                            this.searchResults = response.data
                            console.log(this.searchResults.length, this.searchResults)
                            this.searchResults = this.searchResults.filter((user) => {
                                return !this.saved_collaborators_id.includes(user.id)
                            })
                            console.log(this.searchResults.length, this.saved_collaborators_id)
                        })
                        .catch(error => {
                            console.log('error', error)
                        })
                
                })
                .catch((error) => {
                    console.error(error);
                });
        },

        saveCollaborators() {
            this.collaborators_id.forEach(user_id => {
                this.saved_collaborators_id.push(user_id)

                this.searchResults = this.searchResults.filter(user => {
                    return user.id != user_id
                })
                axios.put('/api/' + user_id + '/add_canv/', {
                "canv_id": sessionStorage.getItem('canvas_id')
                })
                .catch((error) => {
                    console.error(error);
                });


                axios.put('/api/canvases/' + sessionStorage.getItem('canvas_id') + '/add_user/', {
                    "user_id": user_id
                })
                .catch((error) => {
                    console.error(error);
                });

                axios.get('/api/' + user_id + '/')
                    .then(response => {
                        this.collaborators.push(response.data)
                        
                    })
                    .catch(error => {
                        console.log(error);
                    });


                // this.saveCollaborators.push(user_id)

                
                this.search = false;
            });

            // this.search = false;
            this.collaborators_id = [];
            
        },

        searchByName() {
          axios.get('/api/search_by_name/?searchTerm=' + this.searchName)
              .then(response => {
                  this.searchResults = response.data;
                  this.searchResults = this.searchResults.filter((user) => {
                    return !this.saved_collaborators_id.includes(user.id)
                })
              })
              .catch(error => {
                  console.log(error);
              });
        },
        searchByEmail() {
            axios.get('/api/search_by_email/?searchTerm=' + this.searchEmail)
                .then(response => {
                    this.searchResults = response.data;
                    this.searchResults = this.searchResults.filter((user) => {
                    return !this.saved_collaborators_id.includes(user.id)
                })
                })
                .catch(error => {
                    console.log(error);
                });
        },

        getCanvasData() {
            const canvasId = sessionStorage.getItem('canvas_id');

            axios.get('/api/canvases/' + canvasId + '/')
            .then(response => {
                this.canvas_data = response.data['canvas_data']
                const img = new Image();
                img.onload = () => {
                    this.context.drawImage(img, 0, 0, 1500, 400);
                }
                img.src = this.canvas_data;
            })
            .catch(error => {
                console.error(error);
            });
        },

        updateCanvas() {
            
            const canvasId = sessionStorage.getItem('canvas_id');

            axios.put('/api/canvases/' + canvasId + '/update/', {
                "canvas_data": this.canvas.toDataURL()
            })
            .catch((error) => {
                console.error(error);
            });
        },

        searchTrue() {
            this.search = true;
        },

        addCollaborator(user_id) {
            this.collaborators_id.push(user_id)

        },

        deleteCollaborator(user_id) {
            this.collaborators_id = this.collaborators_id.filter((id) => id != user_id)
        },

        async deleteCanvas() {
            const canvasId = sessionStorage.getItem('canvas_id');
            try {
                const response = await axios.delete(`/api/canvases/${canvasId}/delete/`);
                console.log(response.data);
                sessionStorage.setItem('canvas_id', "")
                this.$router.push('/search_canvases')
            } catch (error) {
                console.error(error);
            }
        },

        startDrawing(event) {
            this.drawing = true;
            this.context.beginPath();
            this.context.moveTo(event.offsetX, event.offsetY);
            const message = {
                type: 'draw'
            };
            this.socket.value.send(JSON.stringify(message));
        },

        draw(event) {
            if (!this.drawing) return;
            this.context.lineTo(event.offsetX, event.offsetY);
            this.context.strokeStyle = this.color;
            this.context.lineWidth = this.lineWidth;
            this.context.lineCap = 'round';
            this.context.lineJoin = 'round';
            this.context.stroke();
            this.updateCanvas();
            const message = {
                type: 'draw'
            };
            this.socket.value.send(JSON.stringify(message));
            
        },

        stopDrawing() {
            this.drawing = false;
            const message = {
                type: 'draw'
            };
            this.socket.value.send(JSON.stringify(message));
        },

        setColor(color) {
            this.color = color;
        },

        setLineWidth(width) {
            this.lineWidth = width;
        },

        
        },
  };
</script>