<template>
  <div class="bg-gray-100 min-h-screen flex flex-col">
      <div class="flex-grow bg-gray-100 flex items-center justify-center">
          <div class="max-w-lg p-6 bg-white rounded shadow-lg">
          <h1 class="text-2xl font-bold mb-6">Draw with Friends!</h1>
          <p class="text-gray-600 mb-8">
              Welcome to our website where you can draw with friends in real-time.
              Just share the link with your friends and start chatting and drawing together!
          </p>
          <div class="flex justify-center">
              <div class="border-2 border-gray-300 rounded-lg p-4">
              <canvas ref="canvas" @mousedown="startDrawing" @mousemove="draw" @mouseup="stopDrawing"></canvas>
              </div>
          </div>
          <div class="mt-8">
              <p class="text-center text-gray-600">Share Link:</p>
              <input v-model="shareLink" type="text" class="w-full border border-gray-300 rounded p-2 mt-2" readonly />
          </div>
          </div>
      </div>
  </div>
  
</template>

<script>
export default {
    data() {
    return {
        shareLink: 'https://example.com', // Замените это на реальную ссылку на ваш сайт
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