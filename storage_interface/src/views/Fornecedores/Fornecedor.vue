<template>
  <div class="home">
    <Sidebar />
    <main class="main-content">
      <h1 class="title">Fornecedores</h1>

      <div class="search-bar">
        <input type="text" v-model="searchQuery" placeholder="Pesquisar" />
        <button @click="searchFornecedores">
          <img src="@/assets/icones/icone-lupa.png" alt="Logo" class="logo" height="20px" />
        </button>
        <div class="new-employee">
          <button @click="newFornecedor">Criar novo</button>
        </div>
      </div>

      <div v-for="(fornecedor, index) in filteredFornecedores" :key="index" class="card">
        <div class="card-content">
          <div class="info">
            <p style="font-size: 25px"><strong>{{ fornecedor.nome_fantasia }}</strong></p>
            <p style="font-size: 15px"><strong>Razão Social:</strong> {{ fornecedor.razao_social }}</p>
            <p style="font-size: 15px"><strong>Endereço:</strong> {{ fornecedor.endereco }}</p>
            <p style="font-size: 15px"><strong>Telefone:</strong> {{ fornecedor.telefone }}</p>
          </div>
          <div class="button-group">
            <button class="edit-button" @click="editarFornecedor(fornecedor.id_fornecedor)">Editar</button>
            <button class="delete-button" @click="deletarFornecedor(fornecedor.id_fornecedor)">Deletar</button>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
import Sidebar from '@/components/Sidebar.vue';
import axios from 'axios';

export default {
  components: {
    Sidebar
  },
  data() {
    return {
      fornecedores: [],
      searchQuery: '',
    };
  },
  computed: {
    filteredFornecedores() {
      return this.fornecedores.filter(fornecedor => 
        fornecedor.nome_fantasia.toLowerCase().includes(this.searchQuery.toLowerCase())
      );
    }
  },
  methods: {
    async carregarFornecedores() {
      try {
        const token = localStorage.getItem('authToken');
        if (!token) {
          console.error('Usuário não autenticado.');
          return;
        }
        const response = await axios.get('http://localhost:8000/storage_management/fornecedores/', {
          headers: { Authorization: `Bearer ${token}` }
        });
        this.fornecedores = response.data;
      } catch (error) {
        console.error('Erro ao carregar fornecedores:', error);
      }
    },

    editarFornecedor(fornecedorId) {
      this.$router.push({ name: 'edit-fornecedor', params: { id: fornecedorId } });
    },

    deletarFornecedor(fornecedorId) {
      this.$router.push({ name: 'delete-fornecedor', params: { id: fornecedorId } });
    },


    newFornecedor() {
      this.$router.push({ name: 'create-fornecedor' });
    },

    searchFornecedores() {
      console.log('Buscando por: ', this.searchQuery);
    }
  },
  mounted() {
    this.carregarFornecedores();
  }
};
</script>


<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Afacad&display=swap');

.home {
  display: flex;
  font-family: 'Afacad', sans-serif;
}

.main-content {
  flex: 1;
  padding-left: 16px;
  background-color: #ffffff;
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

.new-employee {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-left: 20px;
}

.new-employee button {
  padding: 10px 16px;
  border: 1px solid rgb(0, 0, 0);
  border-radius: 20px;
  color: black;
  font-size: 16px;
  cursor: pointer;
  background-color: #FFD1A3;
  transition: background-color 0.3s;
  box-shadow: 2px 2px 5px #a7a7a7;
}

.new-employee button:hover {
  background-color: #ffebb2;
}

.card {
  padding: 16px;
  background-color: #fff5db;
  border: 1px solid #ccc;
  border-radius: 8px;
  margin: 8px 0;
  box-shadow: 2px 2px 5px #a7a7a7;
}

.card:hover {
  background-color: #fddeb8;
}

.card p {
  margin: 0;
}

.button-group {
  display: flex;
  justify-content: flex-end;
  gap: 7px;
}

.edit-button,
.delete-button {
  padding: 10px;
  background-color: #f0aa54;
  color: rgb(0, 0, 0);
  border-radius: 20px;
  width: 70px;
  cursor: pointer;
  margin-right: 5px;
  box-shadow: 2px 2px 5px #a7a7a7;
  border: 1px solid rgb(0, 0, 0);
}

.edit-button:hover,
.delete-button:hover {
  background-color: #c88a3d;
}

.delete-button {
  background-color: #cf0e00;
  color: white;
}

.delete-button:hover {
  background-color: #a20a08;
}
</style>
