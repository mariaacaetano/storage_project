import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import Login from '../views/Login.vue';
import Register from '../views/Register.vue';

import Profile from '@/views/Profile/Profile.vue';
import EditProfile from '@/views/Profile/editProfile.vue';

import Produtos from '@/views/Produtos/Produtos.vue';
import CreateProdutos from '@/views/Produtos/createProdutos.vue';
import EditProdutos from '@/views/Produtos/editProdutos.vue';
import DeleteProdutos from '@/views/Produtos/deleteProdutos.vue';

import Categorias from '@/views/Categorias/Categorias.vue';
import CreateCategoria from '@/views/Categorias/createCategorias.vue';
import DeleteCategorias from '@/views/Categorias/deleteCategorias.vue';
import EditCategorias from '@/views/Categorias/editCategoria.vue';

import Fornecedor from '@/views/Fornecedores/Fornecedor.vue';

import Funcionarios from '@/views/Funcionarios/Funcionarios.vue';
import EditFuncionarios from '@/views/Funcionarios/editFuncionarios.vue';
import DeleteFuncionarios from '@/views/Funcionarios/deleteFuncionarios.vue';

const routes = [
    { path: '/', name: 'home', component: HomeView },
    { path: '/login', name: 'login', component: Login },
    { path: '/register', name: 'register', component: Register },

    { path: '/produtos', name: 'produtos', component: Produtos },
    { path: '/produtos/create-produtos', name: 'create-produtos', component: CreateProdutos },
    { path: '/produtos/edit-produtos/:id', name: 'edit-produtos', component: EditProdutos, props: true },
    { path: '/produtos/delete-produtos/:id', name: 'delete-produtos', component: DeleteProdutos, props: true },

    { path: '/categorias', name: 'categorias', component: Categorias },
    { path: '/categorias/editar/:id', name: 'edit-categorias', component: EditCategorias, props: true },
    { path: '/categorias/deletar/:id', name: 'delete-categorias', component: DeleteCategorias, props: true },
    { path: '/categorias/novo', name: 'new-categorias', component: CreateCategoria },

    { path: '/fornecedor', name: 'fornecedor', component: Fornecedor },

    { path: '/profile', name: 'profile', component: Profile },
    { path: '/profile/edit-profile', name: 'edit-profile', component: EditProfile },

    { path: '/funcionarios', name: 'funcionarios', component: Funcionarios },
    { path: '/funcionarios/edit-funcionarios/:id', name: 'edit-funcionarios', component: EditFuncionarios, props: true },
    { path: '/funcionarios/delete-funcionarios/:id', name: 'delete-funcionarios', component: DeleteFuncionarios, props: true },
];

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes,
});

export default router;
