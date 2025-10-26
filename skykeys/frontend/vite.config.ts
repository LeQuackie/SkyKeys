import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import path from 'node:path';

// Vite configuration scoped to the frontend directory while emitting builds
// into the repository-level dist folder expected by Netlify.
export default defineConfig({
  root: path.resolve(__dirname),
  plugins: [react()],
  build: {
    outDir: path.resolve(__dirname, '../dist'),
    emptyOutDir: true
  },
  server: {
    port: 5173
  },
  preview: {
    port: 4173
  }
});
