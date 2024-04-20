<template>
  <div class="bg-gray-100 min-h-screen flex flex-col">
      <div class="flex-grow bg-gray-100 flex items-center justify-center">
          <div class="max-w-lg p-6 bg-white rounded shadow-lg">
            <h1 class="text-2xl font-bold mb-6">Draw with Friends!</h1>
            <p class="text-gray-600 mb-8">
                Welcome to our website where you can create!
            </p>
            <div class="flex justify-center">
                <div class="border-2 border-gray-300 rounded-lg p-4">
                    <canvas ref="canvas" @mousedown="startDrawing" @mousemove="draw" @mouseup="stopDrawing"></canvas>
                </div>
            </div>
          </div>
      </div>
  </div>
  
</template>

<script>
export default {
    data() {
    return {
        isDrawing: false,
    };
    },
    methods: {
        startDrawing(event) {
            this.isDrawing = true;
            const canvas = this.$refs.canvas;
            const ctx = canvas.getContext('2d');
            ctx.beginPath();
            ctx.moveTo(event.offsetX, event.offsetY);
        },
        draw(event) {
            if (!this.isDrawing) return;
            const canvas = this.$refs.canvas;
            const ctx = canvas.getContext('2d');
            ctx.lineTo(event.offsetX, event.offsetY);
            ctx.stroke();
        },
        stopDrawing() {
            this.isDrawing = false;
        },
    },
};
</script>