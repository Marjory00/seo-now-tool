import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// Proxies /api calls to FastAPI so we don't need full URLs in the frontend
export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173,
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,
      },
    },
  },
})