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
                <button @click="updateCanvas" class="m-5 bg-blue-500 text-white font-medium py-2 px-4 rounded hover:bg-blue-600 transition-colors">Save</button>

                
                <button @click="deleteCanvas" class="m-5 bg-red-500 text-white font-medium py-2 px-4 rounded hover:bg-red-600 transition-colors">Delete this canvas</button>
            
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
        drawing: false,
        color: 'black',
        lineWidth: 1,
		name_canvas: '',
        canvas_data: '',
      };
    },

    mounted() {
      this.canvas = this.$refs.canvas;
      this.canvas.width = 800;
      this.canvas.height = 400;
      this.context = this.canvas.getContext('2d');
      this.getCanvasData();
    },

    methods: {

        getCanvasData() {
            const canvasId = localStorage.getItem('canvas_id');

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
            const canvasId = localStorage.getItem('canvas_id');

            axios.put('/api/canvases/' + canvasId + '/update/', {
                "canvas_data": this.canvas.toDataURL()
            })
            .then(() => {
                console.log(555)
                localStorage.setItem('canvas_id', "")
                this.$router.push('/search_canvases')
            })
            .catch((error) => {
                console.error(error);
            });
        },

        async deleteCanvas() {
            const canvasId = localStorage.getItem('canvas_id');
            try {
                const response = await axios.delete(`/api/canvases/${canvasId}/delete/`);
                console.log(response.data);
                localStorage.setItem('canvas_id', "")
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