<template>
  <div class="home">
    <!-- Inclui a Sidebar como um componente -->
    <Sidebar />

    <main class="main-content">
      <div class="search-bar">
        <input v-model="query" type="text" placeholder="Pesquisar" />
        <button @click="search">
          <img src="@/assets/icones/icone-lupa.png" alt="Logo" class="logo" height="20px">
        </button>
      </div>

      <div class="results">
        <div v-if="results.length">
          <div v-for="(result, index) in results" :key="index" class="result-card">
            <h3>{{ result.nome_produto || result.descricao_categoria || result.nome_fantasia || result.primeiro_nome }}</h3>
            <p>{{ result.descricao || result.contato || result.outroCampo || 'Sem descrição' }}</p>
          </div>
        </div>
        <div v-else>
          <p>Nenhum resultado encontrado.</p>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
import Sidebar from "@/components/Sidebar.vue";
import axios from 'axios';

export default {
  name: "Home",
  components: {
    Sidebar,
  },
  data() {
    return {
      query: '',
      results: [],
    };
  },
  methods: {
    async search() {
      if (this.query.trim() === '') {
        this.results = [];
        return;
      }

      try {
        const response = await axios.get('http://localhost:8000/storage_management/search/', {
          params: { query: this.query }
        });

        this.results = [
          ...response.data.Produtos,
          ...response.data.Categorias,
          ...response.data.Fornecedores,
          ...response.data.Funcionários
        ];
      } catch (error) {
        console.error('Erro ao buscar:', error);
      }
    },
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Afacad&display=swap');

.home {
  display: flex;
  background-color: #ffffff;
  font-family: 'Afacad', sans-serif;
}
.main-content {
  flex: 1;
  padding: 16px;
}
.search-bar {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  gap: 10px;
}

.search-bar input {
  width: 70%;
  padding: 8px;
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

.results {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  margin-top: 20px;
}

.result-card {
  background-color: #f9f9f9;
  border-radius: 8px;
  padding: 16px;
  width: 200px;
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
}

.result-card h3 {
  font-size: 18px;
  margin-bottom: 8px;
}

.result-card p {
  font-size: 14px;
  color: #666;
}
</style>
