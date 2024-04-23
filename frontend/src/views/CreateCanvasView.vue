<template>
	<div class="bg-gray-100 min-h-screen">
		<nav class="bg-white shadow">
		</nav>
		<div class="container mx-auto mt-8">
      <div class="bg-white shadow-lg p-4 rounded-lg">
        <!-- <h1 class="text-2xl font-bold mb-4">Create new canvas</h1> -->
        <div class="flex justify-center items-center">
        </div>
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
          <form v-on:submit.prevent="submitForm">
            <canvas ref="canvas" @mousedown="startDrawing" @mousemove="draw" @mouseup="stopDrawing" @mouseleave="stopDrawing" class="border border-gray-300"></canvas>
            <div class="flex flex-col items-center justify-center">
              <div class="m-4">
                <label for="name-canvas" class="text-gray-700 font-medium">Name</label>
                <input v-model="name_canvas" type="name-canvas" id="name-canvas" class="w-full border border-gray-300 rounded p-2" />
              </div>
              
              <button @click="formSubmit" class="mt-2 mb-8 bg-blue-500 text-white font-medium py-2 px-4 rounded hover:bg-blue-600 transition-colors">Create Canvas</button>
            </div>
					</form>
      </div>
		</div>
	</div>
</template>
  
<script>
import axios from 'axios';

  export default {
    data() {
      return {
        drawing: false,
        color: 'black',
        lineWidth: 1,
        canvases: [],
			  name_canvas: '',
        canvas_id: '',
      };
    },
    mounted() {
      this.canvas = this.$refs.canvas;
      this.canvas.width = 800;
      this.canvas.height = 400;
      this.context = this.canvas.getContext('2d');

    },

    methods: {

      submitForm() {
        axios
          .post('/api/canvases/create/', {
            'canvas_data': this.canvas.toDataURL(),
            'name': this.name_canvas,
          })
          .then(response => {
            this.canvases.unshift(response.data)
            this.name_canvas = ''
            // this.canvas_id = response.data.id
            axios.put('/api/' + localStorage.getItem('user.id') + '/add_canv/', {
                "canv_id": response.data.id
                })
                .then(() => {
                    console.log('canvas was added!')
                    this.$router.push('/search_canvases')
                    
                })
                .catch((error) => {
                    console.error(error);
                });
            // console.log(response.data)
            
          })
          .catch(error => {
            console.log('error', error)
          })

          // axios.put('/api/' + localStorage.getItem('user.id') + '/add_canv/', {
          //       "canv_id": this.canvas_id
          //       })
          //       .then(() => {
          //           console.log('canvas was added!')
          //           // this.$router.push('/search_canvases')
                    
          //       })
          //       .catch((error) => {
          //           console.error(error);
          //       });
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