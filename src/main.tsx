import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import App from './App'
import { ProgressoProvider } from './state'
import './styles.css'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <ProgressoProvider>
      <App />
    </ProgressoProvider>
  </StrictMode>,
)
