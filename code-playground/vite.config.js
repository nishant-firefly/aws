import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  server: {
    host: "0.0.0.0",   // Exposes the server outside the container
    port: 5173,        // Keep the default Vite port
    strictPort: true,  // Ensures it doesn't fall back to another port
    watch: {
      usePolling: true // Ensures hot-reloading works inside Docker
    }
  }
});
