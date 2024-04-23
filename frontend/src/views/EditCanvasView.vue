<template>
	<div class="bg-gray-100 min-h-screen">
		<div class="container mx-auto mt-8">
        <div class="bg-white shadow-lg p-4 rounded-lg">
        <div class="flex items-center mt-4">
            <button @click="setColor('black')" class="w-10 h-10 rounded-full bg-black mr-2 hover:border-white hover:border-2"></button>
            <button @click="setColor('red')" class="w-10 h-10 rounded-full bg-red-500 mr-2 hover:border-black hover:border-2" ></button>
            <button @click="setColor('blue')" class="w-10 h-10 rounded-full bg-blue-500 mr-2 hover:border-black hover:border-2"></button>
            <button @click="setColor('green')" class="w-10 h-10 rounded-full bg-green-500 mr-2 hover:border-black hover:border-2"></button>
        </div>
        <div class="flex items-center mt-4">
            <button @click="setLineWidth(1)" class="w-10 h-10 rounded-full bg-gray-400 mr-2 hover:border-black hover:border-2" title="Thin"></button>
            <button @click="setLineWidth(3)" class="w-10 h-10 rounded-full bg-gray-400 mr-2 hover:border-black hover:border-2" title="Medium"></button>
            <button @click="setLineWidth(5)" class="w-10 h-10 rounded-full bg-gray-400 mr-2 hover:border-black hover:border-2" title="Thick"></button>
        </div>
            <div class="flex justify-center">
                <canvas :ref="'canvas'" @mousedown="startDrawing" @mousemove="draw" @mouseup="stopDrawing" @mouseleave="stopDrawing" class="border border-gray-300"></canvas>
            </div>
            
            <div class="flex flex-row items-center justify-center">
                <!-- <button @click="updateCanvas" class="m-5 bg-blue-500 text-white font-medium py-2 px-4 rounded hover:bg-blue-600 transition-colors">Save</button> -->

                <button @click="searchTrue" class="m-5 bg-blue-500 text-white font-medium py-2 px-4 rounded hover:bg-blue-600 transition-colors">Add collaborators</button>
                
                <button @click="deleteCanvas" class="m-5 bg-red-500 text-white font-medium py-2 px-4 rounded hover:bg-red-600 transition-colors">Delete this canvas</button>
            
            </div>

            <div v-if="search">
                <div class="bg-white shadow-lg p-4 rounded-lg">
                <button @click="saveCollaborators" class="m-5 bg-blue-500 text-white font-medium py-2 px-4 rounded hover:bg-blue-600 transition-colors">Save</button>
                <h1 class="text-2xl font-bold mb-4">Search collaborators</h1>
                <div class="flex items-center mt-4">
                    <input v-model="searchName" type="text" placeholder="Search by Name" class="w-full border border-gray-300 rounded p-2 mr-2">
                    <button @click="searchByName" class="bg-blue-500 text-white font-medium py-2 px-4 rounded hover:bg-blue-600 transition-colors">Search</button>
                </div>
                <div class="flex items-center mt-4">
                    <input v-model="searchEmail" type="text" placeholder="Search by Email" class="w-full border border-gray-300 rounded p-2 mr-2">
                    <button @click="searchByEmail" class="bg-blue-500 text-white font-medium py-2 px-4 rounded hover:bg-blue-600 transition-colors">Search</button>
                </div>
                <h2 class="text-xl mt-6 font-bold">Search Results</h2>
                <ul class="mt-4">
                    <li v-for="user in searchResults" :key="user.id" class="bg-white shadow p-4 rounded-lg mb-4">
                    <h3 class="text-lg font-semibold">{{ user.name }}</h3>
                    <p class="text-gray-600">{{ user.email }}</p>
                    <button v-if="!collaborators_id.includes(user.id) && !saved_collaborators_id.includes(user.id)" @click="addCollaborator(user.id) && !saved_collaborators_id.includes(user.id)" class="m-5 bg-blue-500 text-white font-medium py-2 px-4 rounded hover:bg-blue-600 transition-colors">Add</button>
                    <button v-if="collaborators_id.includes(user.id) && !saved_collaborators_id.includes(user.id)" @click="deleteCollaborator(user.id)" class="m-5 bg-white border-2 border-blue-500 focus:outline-none focus:ring-1 focus:ring-blue-500 text-blue-500 font-medium py-2 px-4 rounded transition-colors">Added</button>
                    </li>
                </ul>
                </div>
            </div>

        </div>
		</div>
	</div>
</template>
  
<script>
import axios from 'axios';

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

      };
    },

    mounted() {
      this.canvas = this.$refs.canvas;
      this.canvas.width = 800;
      this.canvas.height = 400;
      this.context = this.canvas.getContext('2d');
      this.getCanvasData();
      this.getUsers();
      this.getCollaborators();
    },

    methods: {

        getCollaborators() {
            axios.get('/api/canvases/' + sessionStorage.getItem('canvas_id') + '/get_users/')
                .then(response => {
                    this.saved_collaborators_id = response.data.users.split(',').filter(id => id != '');
                
                })
                .catch((error) => {
                    console.error(error);
                });
        },

        saveCollaborators() {
            this.collaborators_id.forEach(user_id => {
                // console.log(user_id)
                
                
                axios.put('/api/' + user_id + '/add_canv/', {
                "canv_id": sessionStorage.getItem('canvas_id')
                })
                .then(() => {
                    console.log('canvas was added!')
                    
                })
                .catch((error) => {
                    console.error(error);
                });


                axios.put('/api/canvases/' + sessionStorage.getItem('canvas_id') + '/add_user/', {
                    "user_id": user_id
                })
                .then(response => {
                    console.log('user was added!')
                    console.log(response.data)
                    
                })
                .catch((error) => {
                    console.error(error);
                });
            });
            
        },

        getUsers() {
            axios
            .get(`/api/users/`)
            .then(response => {
            console.log('data', response.data)

            this.searchResults = response.data
            })
            .catch(error => {
            console.log('error', error)
            })
        },

        searchByName() {
          axios.get('/api/search_by_name/?searchTerm=' + this.searchName)
              .then(response => {
                  this.searchResults = response.data;
              })
              .catch(error => {
                  console.log(error);
              });
        },
        searchByEmail() {
            axios.get('/api/search_by_email/?searchTerm=' + this.searchEmail)
                .then(response => {
                    this.searchResults = response.data;
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
                    this.context.drawImage(img, 0, 0, 800, 400);
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
            .then(() => {
                // sessionStorage.setItem('canvas_id', "")
                // this.$router.push('/search_canvases')
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
            
        },

        stopDrawing() {
            this.drawing = false;
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