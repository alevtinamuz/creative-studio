<template>
	<div class="bg-gray-100 min-h-screen">
		<nav class="bg-white shadow">
		</nav>
		<div class="container mx-auto mt-8">
      <div class="bg-white shadow-lg p-4 rounded-lg">
        <!-- <h1 class="text-2xl font-bold mb-4">Create new canvas</h1> -->
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
        <form v-on:submit.prevent="submitForm">
            <div><canvas ref="canvas" @mousedown="startDrawing" @mousemove="draw" @mouseup="stopDrawing" @mouseleave="stopDrawing" class="border border-gray-300"></canvas></div>

            
            <div class="flex flex-col items-center justify-center">
              <div class="flex flex-col items-center justify-center">
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
        color: 'red',
        lineWidth: 1,
        canvases: [],
			  name_canvas: '',
        canvas_id: '',
      };
    },
    mounted() {
      this.canvas = this.$refs.canvas;
      this.canvas.width = 1500;
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
            axios.put('/api/' + sessionStorage.getItem('user.id') + '/add_canv/', {
                "canv_id": response.data.id
                })
                .then(() => {
                    this.$router.push('/search_canvases')
                    
                })
                .catch((error) => {
                    console.error(error);
                });
            
          })
          .catch(error => {
            console.log('error', error)
          })
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