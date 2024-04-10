<template>
	<div class="bg-gray-100 min-h-screen">
		<nav class="bg-white shadow">
		</nav>
		<div class="container mx-auto mt-8">
		<div class="bg-white shadow-lg p-4 rounded-lg">
			<h1 class="text-2xl font-bold mb-4">Collaborative Canvas!</h1>
			<div class="flex justify-center">
			<canvas ref="canvas" @mousedown="startDrawing" @mousemove="draw" @mouseup="stopDrawing" @mouseleave="stopDrawing" class="border border-gray-300"></canvas>
			</div>
			<div class="flex items-center mt-4">
			<button @click="setColor('black')" class="w-10 h-10 rounded-full bg-black mr-2"></button>
			<button @click="setColor('red')" class="w-10 h-10 rounded-full bg-red-500 mr-2"></button>
			<button @click="setColor('blue')" class="w-10 h-10 rounded-full bg-blue-500 mr-2"></button>
			<button @click="setColor('green')" class="w-10 h-10 rounded-full bg-green-500 mr-2"></button>
			</div>
			<div class="flex items-center mt-4">
			<button @click="setLineWidth(1)" class="w-10 h-10 rounded-full bg-gray-400 mr-2" title="Thin"></button>
			<button @click="setLineWidth(3)" class="w-10 h-10 rounded-full bg-gray-400 mr-2" title="Medium"></button>
			<button @click="setLineWidth(5)" class="w-10 h-10 rounded-full bg-gray-400 mr-2" title="Thick"></button>
			</div>
		</div>
		</div>
	</div>
</template>
  
  <script>
  export default {
    data() {
      return {
        drawing: false,
        color: 'black',
        lineWidth: 1,
      };
    },
    mounted() {
      this.canvas = this.$refs.canvas;
      this.context = this.canvas.getContext('2d');
    },
    methods: {
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