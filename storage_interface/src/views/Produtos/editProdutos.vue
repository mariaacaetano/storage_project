<template>
  <div class="produto-page">
    <!-- Sidebar -->
    <Sidebar />
  
    <main class="main-content">
      <h1 style="font-size:50px; margin: 0;">Editar Produto</h1>
  
      <!-- Barra de pesquisa de produtos -->
      <div class="search-bar">
        <input type="text" v-model="searchQuery" placeholder="Pesquisar" />
        <button @click="searchProdutos">🔍</button>
      </div>
  
      <section class="edit-section">
        <h2>Editar Produto</h2>
        <form @submit.prevent="salvar">
          <!-- Nome do Produto -->
          <label>Nome do Produto</label>
          <input type="text" v-model="produto.nome_produto" required />
  
          <!-- Código do Produto -->
          <label>Código do Produto</label>
          <input type="text" v-model="produto.codigo_produto" required />
  
          <!-- Preço e Moeda -->
          <label>Preço</label>
          <div class="preco-input">
            <select v-model="produto.moeda" class="styled-select">
              <option value="R$">R$</option>
              <option value="USD">USD</option>
              <option value="EUR">EUR</option>
            </select>
            <input type="number" step="0.01" v-model.number="produto.preco_produto" required />
          </div>
  
          <!-- Categoria -->
          <label>Categoria</label>
          <select v-model="produto.categoria" required class="styled-select">
            <option v-for="categoria in categorias" :key="categoria.id_categoria" :value="categoria.id_categoria">{{ categoria.nome }}</option>
          </select>
  
          <!-- Quantidade -->
          <label>Quantidade</label>
          <input type="number" v-model.number="produto.quantidade" required />
  
          <!-- Status -->
          <label>Status</label>
          <select v-model="produto.status" class="styled-select">
            <option :value="true">Ativo</option>
            <option :value="false">Desativo</option>
          </select>

  
          <!-- Fornecedor -->
          <label>Fornecedor</label>
          <select v-model="produto.fornecedor" required class="styled-select">
            <option v-for="fornecedor in fornecedores" :key="fornecedor.id_fornecedor" :value="fornecedor.id_fornecedor">{{ fornecedor.nome_fantasia || fornecedor.nome }}</option>
          </select>
  
          <!-- Botões -->
          <div class="buttons">
            <button class="voltar" @click="voltar">Voltar</button>
            <button class="salvar" type="submit">Salvar</button>
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
import Sidebar from "@/components/Sidebar.vue";

export default {
  components: { Sidebar },
  setup() {
    const router = useRouter();
    const route = useRoute();  // Usando useRoute para pegar o ID da URL
    const searchQuery = ref("");
    const categorias = ref([]);
    const fornecedores = ref([]);
    const produto = ref({
      id_produto: route.params.id, // Pegando o ID diretamente da URL
      nome_produto: '',
      codigo_produto: '',
      preco_produto: 0,
      moeda: 'R$',
      categoria: '',
      quantidade: 0,
      status: 'ativo',
      fornecedor: '',
    });

    // Carregar categorias
    const carregarCategorias = async () => {
      try {
        const token = localStorage.getItem('authToken');
        if (!token) {
          console.error('Usuário não autenticado.');
          return;
        }
        const response = await axios.get(`http://127.0.0.1:8000/storage_management/categorias/`, {
          headers: { Authorization: `Bearer ${token}` },
        });
        categorias.value = response.data;
      } catch (error) {
        console.error('Erro ao carregar categorias:', error);
      }
    };

    // Carregar fornecedores
    const carregarFornecedores = async () => {
      try {
        const token = localStorage.getItem('authToken');
        if (!token) {
          console.error('Usuário não autenticado.');
          return;
        }
        const response = await axios.get(`http://127.0.0.1:8000/storage_management/fornecedores/`, {
          headers: { Authorization: `Bearer ${token}` },
        });
        fornecedores.value = response.data;
      } catch (error) {
        console.error('Erro ao carregar fornecedores:', error);
      }
    };

    // Função para salvar as alterações no produto
    const salvar = async () => {
      if (!produto.value.id_produto) {
        console.error('ID do produto não encontrado.');
        alert('ID do produto não encontrado.');
        return;
      }

      try {
        const token = localStorage.getItem('authToken');
        if (!token) {
          console.error('Usuário não autenticado.');
          return;
        }

        const response = await axios.put(`http://127.0.0.1:8000/storage_management/produtos/${produto.value.id_produto}/update/`, produto.value, {
          headers: { Authorization: `Bearer ${token}` },
        });

        if (response.status === 200) {
          alert('Produto atualizado com sucesso!');
          router.push('/produtos');
        } else {
          alert('Erro ao salvar produto. Tente novamente.');
        }
      } catch (error) {
        console.error('Erro ao salvar produto:', error);
        alert('Erro ao salvar produto. Verifique o console para mais detalhes.');
      }
    };

    // Função para voltar à lista de produtos
    const voltar = () => {
      router.push('/produtos');
    };

    // Função para buscar produtos
    const searchProdutos = () => {
      console.log('Buscando por: ', searchQuery.value);
    };

    onMounted(() => {
      carregarCategorias();
      carregarFornecedores();
    });

    return { produto, categorias, fornecedores, searchQuery, salvar, voltar, searchProdutos };
  },
};
</script>


  <style scoped>
  @import url('https://fonts.googleapis.com/css2?family=Afacad&display=swap');

  .produto-page {
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
    gap: 10px;
    margin-bottom: 30px;
  }

  .search-bar input {
    width: 70%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
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

  .preco-input {
    display: flex;
    align-items: center;
  }

  .styled-select, input {
    width: 100%;
    padding: 10px;
    margin: 10px 0;  
    border: 1px solid #ccc;
    border-radius: 5px;
  }

  .styled-select {
    background-color: white;
    cursor: pointer;
  }

  .buttons {
    display: flex;
    justify-content: space-between;
    margin-top: 15px;
  }

  .voltar, .salvar {
    padding: 10px 15px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }

  .voltar {
    background-color: #ddd;
  }

  .salvar {
    background-color: #f7e0b5;
  }
  </style>
