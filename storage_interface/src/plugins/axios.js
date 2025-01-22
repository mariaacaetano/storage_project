import axios from 'axios';

// Função para obter o CSRF token dos cookies
import axios from 'axios';

// Pegue o token CSRF do cookie
const getCsrfToken = () => {
  const csrfToken = document.cookie.split(';').find(cookie => cookie.trim().startsWith('csrftoken='));
  return csrfToken ? csrfToken.split('=')[1] : '';
};

// Configuração global do Axios para incluir o CSRF no cabeçalho
axios.defaults.headers.common['X-CSRFToken'] = getCsrfToken();


// Configuração global do Axios
const axiosInstance = axios.create({
  baseURL: "http://127.0.0.1:8000/", // Substitua pelo endpoint base da sua API
  headers: {
    "X-CSRFToken": getCsrfToken(),
    "Content-Type": "application/json",
  },
});

export default axiosInstance;
