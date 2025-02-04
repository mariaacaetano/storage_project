<template>
    <div class="fornecedor-page">
      <Sidebar />
      <main class="main-content">
        <h1 style="font-size:50px; margin: 0;">Fornecedores</h1>
        <div class="search-bar">
          <input type="text" v-model="searchQuery" placeholder="Pesquisar" />
          <button @click="searchFornecedores">🔍</button>
        </div>
        <section class="edit-section">
          <h2>Editar fornecedor</h2>
          <form @submit.prevent="salvar">
            <label>Razão Social</label>
            <input type="text" v-model="fornecedor.razao_social" />
            <label>Nome Fantasia</label>
            <input type="text" v-model="fornecedor.nome_fantasia" />
            <label>CNPJ</label>
            <input type="text" v-model="fornecedor.cnpj" />
            <label>Inscrição Estadual</label>
            <input type="text" v-model="fornecedor.inscricao_estadual" />
            <label>Telefone</label>
            <input type="text" v-model="fornecedor.telefone" />
            <label>Endereço</label>
            <input type="text" v-model="fornecedor.endereco" />
            <label>Tipo de Produto</label>
            <input type="text" v-model="fornecedor.tipo_produto" />
            <div class="buttons">
              <button class="voltar" @click="voltar">Voltar</button>
              <button class="editar" type="submit">Salvar</button>
            </div>
          </form>
        </section>
      </main>
    </div>
  </template>
  
  <script>
  import { ref, onMounted } from 'vue';
  import { useRouter, useRoute } from 'vue-router';
  import axios from 'axios';
  import Sidebar from '@/components/Sidebar.vue';
  
  export default {
    components: { Sidebar },
    setup() {
      const router = useRouter();
      const route = useRoute();
      const searchQuery = ref("");
      const fornecedor = ref({
        razao_social: '', nome_fantasia: '', cnpj: '',
        inscricao_estadual: '', telefone: '', endereco: '', tipo_produto: ''
      });
  
      const FornecedorId = route.params.id || null;
  
      const carregarFornecedor = async () => {
        if (!FornecedorId) return console.error('ID do fornecedor não encontrado.');
        try {
          const token = localStorage.getItem('authToken');
          if (!token) return console.error('Usuário não autenticado.');
          const { data } = await axios.get(`http://127.0.0.1:8000/storage_management/fornecedores/${FornecedorId}/`, {
            headers: { Authorization: `Bearer ${token}` }
          });
          fornecedor.value = data;
        } catch (error) {
          console.error('Erro ao carregar fornecedor:', error);
        }
      };
  
      const salvar = async () => {
        if (!FornecedorId) return console.error('ID do fornecedor não encontrado.');
        try {
          const token = localStorage.getItem('authToken');
          if (!token) return console.error('Usuário não autenticado.');
          await axios.put(`http://127.0.0.1:8000/storage_management/fornecedores/${FornecedorId}/update/`, fornecedor.value, {
            headers: { Authorization: `Bearer ${token}` }
          });
          alert('Fornecedor atualizado com sucesso!');
          router.push('/fornecedor');
        } catch (error) {
          console.error('Erro ao salvar fornecedor:', error);
          alert('Erro ao salvar fornecedor.');
        }
      };
  
      const voltar = () => router.push('/fornecedor');
      
      onMounted(() => carregarFornecedor());
      
      return { fornecedor, searchQuery, salvar, voltar };
    }
  };
  </script>
  
  <style scoped>
  .fornecedor-page {
    display: flex;
    font-family: 'Afacad', sans-serif;
    background-color: #ffffff;
  }
  .main-content {
    flex: 1;
    padding: 2rem;
  }
  .search-bar {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 50px;
  }
  .search-bar input {
    width: 70%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-shadow: 2px 2px 5px #a7a7a7;
  }
  .search-bar button {
    padding: 7px;
    background-color: #ffd1a3;
    border-radius: 10px;
    cursor: pointer;
  }
  .search-bar button:hover {
    background-color: #cdf2ff;
  }
  .edit-section {
    background: #fff;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
  }
  form {
    display: flex;
    flex-direction: column;
  }
  label {
    margin-top: 10px;
    font-weight: bold;
  }
  input {
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 5px;
    margin-bottom: 10px;
  }
  .buttons {
    display: flex;
    justify-content: space-between;
    margin-top: 15px;
  }
  .voltar {
    background-color: #ddd;
    padding: 10px;
    border-radius: 5px;
  }
  .editar {
    background-color: #f7e0b5;
    padding: 10px;
    border-radius: 5px;
  }
  </style>