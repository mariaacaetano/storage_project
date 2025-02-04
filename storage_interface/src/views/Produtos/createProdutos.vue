<template>
  <div class="produto-page">
    <!-- Sidebar -->
    <Sidebar />
  
    <main class="main-content">
      <h1 style="font-size:50px; margin: 0;">Produtos</h1>
      <div class="search-bar">
        <input type="text" v-model="searchQuery" placeholder="Pesquisar" />
        <button @click="searchProdutos">🔍</button>
      </div>
  
      <section class="edit-section">
        <h2>Criar Produto</h2>
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
            <option v-for="categoria in categorias" :key="categoria.id_categoria" :value="categoria.id_categoria">{{ categoria.nome }}</option>
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
            <option v-for="fornecedor in fornecedores" :key="fornecedor.id_fornecedor" :value="fornecedor.id_fornecedor">{{ fornecedor.nome_fantasia || fornecedor.nome }}</option>
          </select>
  
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
import { useRouter } from 'vue-router';
import axios from 'axios';
import Sidebar from "@/components/Sidebar.vue";

export default {
  components: { Sidebar },
  setup() {
    const router = useRouter();
    const searchQuery = ref("");
    const categorias = ref([]);
    const fornecedores = ref([]);
    const produto = ref({
      nome_produto: '',
      codigo_produto: '',
      preco_produto: 0,
      moeda: 'R$',
      categoria: '',
      quantidade: 0,
      status: '',
      fornecedor: '',
    });

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

    onMounted(() => {
      carregarCategorias();
      carregarFornecedores();
    });

    const salvar = async () => {
  console.log(produto.value); // Verifique os dados que estão sendo enviados
    try {
      const token = localStorage.getItem('authToken');
      if (!token) {
        console.error('Usuário não autenticado.');
        return;
      }
      const response = await axios.post('http://127.0.0.1:8000/storage_management/create-produto/', produto.value, {
        headers: { Authorization: `Bearer ${token}` },
      });

      if (response.status === 201) {
        alert('Produto criado com sucesso!');
        router.push('/produtos');
      } else {
        alert('Erro ao salvar produto. Tente novamente.');
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