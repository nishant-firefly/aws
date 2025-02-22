import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react-swc';

export default defineConfig({
  plugins: [react()],
  server: {
    watch: {
      usePolling: true, // Ensures file changes are detected inside Docker
    },
    host: "0.0.0.0",  // Allows access from Docker container
    port: 5173,       // Ensure this matches docker-compose.yml
    strictPort: true,
    hmr: {
      clientPort: 5173, // Fixes HMR inside Docker
    },
  },
});
