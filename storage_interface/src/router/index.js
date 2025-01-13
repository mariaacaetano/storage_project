import { createRouter, createWebHistory } from 'vue-router';

// Importando os componentes das páginas
import LoginPage from '../views/LoginPage.vue';
import RegisterPage from '../views/RegisterPage.vue';
import HomePage from '../views/HomePage.vue'; // Página inicial
import AboutPage from '../views/AboutPage.vue'; // Página sobre

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomePage, // Página inicial
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginPage, // Página de login
  },
  {
    path: '/register',
    name: 'Register',
    component: RegisterPage, // Página de registro
  },
  {
    path: '/about',
    name: 'About',
    component: AboutPage, // Página sobre
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes, // Definindo as rotas
});

export default router;
