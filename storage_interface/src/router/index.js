import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import Login from '../views/Login.vue';
import Register from '../views/Register.vue'
import Produtos from '@/views/Produtos.vue';
import Categorias from '@/views/Categorias.vue';
import Fornecedor from '@/views/Fornecedor.vue';
import Funcionarios from '@/views/Funcionarios.vue';
import Profile from '@/views/Profile.vue';

const routes = [
    { path: '/', name: 'home', component: HomeView },
    { path: '/login', name: 'login', component: Login },
    { path: '/register', name: 'register', component: Register },
    { path: '/produtos', name: 'produtos', component: Produtos },
    { path: '/categorias', name: 'categorias', component: Categorias },
    { path: '/fornecedor', name: 'fornecedor', component: Fornecedor },
    { path: '/funcionarios', name: 'funcionarios', component: Funcionarios },
    { path: '/profile', name: 'profile', component: Profile },
];

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes,
});

export default router;
