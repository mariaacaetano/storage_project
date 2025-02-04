<template>
    <div class="funcionario-page">
      <!-- Sidebar -->
      <Sidebar />
  
      <main class="main-content">
        <h1 style="font-size:50px; margin: 0;">Categorias</h1>
        <div class="search-bar">
          <input type="text" v-model="searchQuery" placeholder="Pesquisar" />
          <button @click="searchFuncionarios">🔍</button>
        </div>
  
        <section class="edit-section">
          <h2>Criar categoria</h2>
          <form @submit.prevent="salvar">
            <label>Nome da Categoria</label>
            <input type="text" v-model="categoria.nome" />
  
            <label>Descrição</label>
            <input type="text" v-model="categoria.descricao_categoria" />
  
            <label>Localização</label>
            <input type="text" v-model="categoria.localizacao" />
  
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
  import { ref } from 'vue';
  import { useRouter } from 'vue-router';
  import axios from 'axios';
  import Sidebar from "@/components/Sidebar.vue";
  
  export default {
    components: { Sidebar },
    setup() {
      const router = useRouter();
      const searchQuery = ref("");
      const categoria = ref({
        nome: '',
        descricao_categoria: '',
        localizacao: '',
      });
  
      // Função para salvar a categoria
      const salvar = async () => {
        try {
          const token = localStorage.getItem('authToken');
          if (!token) {
            console.error('Usuário não autenticado.');
            return;
          }
  
          // Faz a requisição para criar a categoria
          const response = await axios.post(
            `http://127.0.0.1:8000/storage_management/create_categoria/`,
            {
                nome: categoria.value.nome,
                descricao_categoria: categoria.value.descricao_categoria,
                localizacao: categoria.value.localizacao,
            },
            {
                headers: { Authorization: `Bearer ${token}` },
            }
            );

  
          if (response.status === 201) {
            alert('Categoria criada com sucesso!');
            router.push('/categorias');
          }
        } catch (error) {
          console.error('Erro ao salvar categoria:', error);
          alert('Erro ao salvar categoria. Verifique o console para mais detalhes.');
        }
      };
  
      // Função para voltar à lista de categorias
      const voltar = () => {
        router.push('/categorias');
      };
  
      return { categoria, searchQuery, salvar, voltar };
    },
  };
  </script>
  
  <style scoped>
  @import url('https://fonts.googleapis.com/css2?family=Afacad&display=swap');
  
  .funcionario-page {
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
    justify-content: flex-start;
    width: 100%;
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
    background-color: #ffd1a300;
    border: 1px solid rgba(0, 0, 0, 0);
    border-radius: 10px;
    color: black;
    font-size: 16px;
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
  
  .voltar,
  .editar {
    padding: 10px 15px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  
  .voltar {
    background-color: #ddd;
  }
  
  .editar {
    background-color: #f7e0b5;
  }
  </style>
  