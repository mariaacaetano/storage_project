import axios from "axios";

const instance = axios.create({
  baseURL: "http://127.0.0.1:8000", // URL base da API
  headers: {
    "Content-Type": "application/json",
  },
});

// Adiciona o CSRF token automaticamente
instance.interceptors.request.use(config => {
  const csrfCookie = document.cookie
    .split(";")
    .find(cookie => cookie.trim().startsWith("csrftoken="));
  const csrfToken = csrfCookie ? csrfCookie.split("=")[1] : null;

  if (csrfToken) {
    config.headers["X-CSRFToken"] = csrfToken;
  }

  return config;
});

export default instance;
