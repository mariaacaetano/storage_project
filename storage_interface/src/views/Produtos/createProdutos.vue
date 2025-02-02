<template>
  <div class="produto-page">
    <Sidebar />
    
    <main class="main-content">
      <h1 class="title">Produtos</h1>
      <div class="search-bar">
        <input type="text" v-model="searchQuery" placeholder="Pesquisar" />
        <button @click="searchProdutos">
          <img src="@/assets/icones/icone-lupa.png" alt="Logo" class="logo" height="20px" />
        </button>
      </div>
      
      <section class="edit-section">
        <h2>Editar produto</h2>
        <form @submit.prevent="salvar">
          <label>Nome do Produto</label>
          <input type="text" v-model="produto.nome_produto" required />

          <label>Código do Produto</label>
          <input type="text" v-model="produto.codigo_produto" required />

          <label>Preço</label>
          <div class="preco-input">
            <select v-model="produto.moeda" class="styled-select">
              <option value="R$">R$</option>
              <option value="USD">USD</option>
              <option value="EUR">EUR</option>
            </select>
            <input type="number" step="0.01" v-model.number="produto.preco_produto" required />
          </div>

          <label>Categoria</label>
          <select v-model="produto.categoria" required class="styled-select">
            <option v-for="categoria in categorias" :key="categoria.id" :value="categoria.id">{{ categoria.nome }}</option>
          </select>

          <label>Quantidade</label>
          <input type="number" v-model.number="produto.quantidade" required />

          <label>Status</label>
          <select v-model="produto.status" class="styled-select">
            <option value="ativo">Ativo</option>
            <option value="desativo">Desativo</option>
          </select>

          <label>Fornecedor</label>
          <select v-model="produto.fornecedor" required class="styled-select">
            <option v-for="fornecedor in fornecedores" :key="fornecedor.id" :value="fornecedor.id">{{ fornecedor.nome }}</option>
          </select>
          
          <div class="buttons">
            <button class="voltar" type="button" @click="voltar">Voltar</button>
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
    const route = useRoute();
    const searchQuery = ref("");
    const categorias = ref([]);
    const fornecedores = ref([]);
    const produto = ref({
      id: null,
      nome_produto: '',
      categoria: '',
      quantidade: 0,
      codigo_produto: '',
      preco_produto: 0,
      status: 'ativo',
      fornecedor: '',
      moeda: 'R$',
    });

    const carregarCategorias = async () => {
      try {
        const response = await axios.get(`http://127.0.0.1:8000/categorias/`);
        categorias.value = response.data;
      } catch (error) {
        console.error('Erro ao carregar categorias:', error);
      }
    };

    const carregarFornecedores = async () => {
      try {
        const response = await axios.get(`http://127.0.0.1:8000/fornecedores/`);
        fornecedores.value = response.data;
      } catch (error) {
        console.error('Erro ao carregar fornecedores:', error);
      }
    };

    const carregarProduto = async () => {
      const id = route.params.id;
      if (!id) return;
      try {
        const response = await axios.get(`http://127.0.0.1:8000/storage_management/produtos/${id}/`);
        produto.value = response.data;
      } catch (error) {
        console.error('Erro ao carregar produto:', error);
      }
    };

    onMounted(() => {
      carregarCategorias();
      carregarFornecedores();
      carregarProduto();
    });

    const salvar = async () => {
      try {
        const token = localStorage.getItem('authToken');
        if (!token) {
          alert('Usuário não autenticado. Faça login novamente.');
          return;
        }

        const url = produto.value.id 
          ? `http://127.0.0.1:8000/storage_management/produtos/${produto.value.id}/`
          : `http://127.0.0.1:8000/storage_management/produtos/`;
        
        const method = produto.value.id ? 'put' : 'post';
        
        const response = await axios[method](url, produto.value, {
          headers: { Authorization: `Bearer ${token}` },
        });

        if ([200, 201].includes(response.status)) {
          alert('Produto salvo com sucesso!');
          router.push('/produtos');
        }
      } catch (error) {
        console.error('Erro ao salvar produto:', error);
        alert('Erro ao salvar produto. Verifique o console para mais detalhes.');
      }
    };

    const voltar = () => {
      router.push('/produtos');
    };

    const searchProdutos = () => {
      console.log('Buscando por: ', searchQuery.value);
    };

    return { produto, searchQuery, salvar, voltar, searchProdutos, categorias, fornecedores };
  },
};
</script>

  
<style scoped>
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
.preco-input select {
  margin-right: 10px;
}

.styled-select, input {
  width: 100%;
  padding: 10px;
  margin: 10px 0;  
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 16px;
}

.styled-select {
  background-color: white;
  cursor: pointer;
}

.preco-container {
  display: flex;
  gap: 5px;
}

.imagem-upload button {
  background: none;
  border: none;
  font-size: 20px;
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