import react from '@vitejs/plugin-react'
import { defineConfig } from 'vitest/config'
import { VitePWA } from 'vite-plugin-pwa'

// base './' deixa o mesmo build funcionar na raiz do Vercel e em subpasta do GitHub Pages.
export default defineConfig({
  base: './',
  plugins: [
    react(),
    VitePWA({
      registerType: 'autoUpdate',
      includeAssets: ['icon-192.png', 'icon-512.png'],
      manifest: {
        name: 'Estudos ABDI 2026',
        short_name: 'Estudos ABDI',
        description: 'Estudo diário para o processo seletivo da ABDI (API, Comunicação e Marketing).',
        lang: 'pt-BR',
        display: 'standalone',
        start_url: './',
        scope: './',
        background_color: '#f6f4ee',
        theme_color: '#1b6b4a',
        icons: [
          { src: 'icon-192.png', sizes: '192x192', type: 'image/png' },
          { src: 'icon-512.png', sizes: '512x512', type: 'image/png', purpose: 'any maskable' },
        ],
      },
      workbox: { globPatterns: ['**/*.{js,css,html,png,json,svg}'] },
    }),
  ],
  test: { include: ['src/**/*.test.ts'] },
})
