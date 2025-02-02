<template>
  <div class="home">
    <Sidebar />
    <main class="main-content">
      <h1 class="title">Produtos</h1>

      <div class="search-bar">
        <input type="text" v-model="searchQuery" placeholder="Pesquisar" />
        <button @click="searchProdutos">
          <img src="@/assets/icones/icone-lupa.png" alt="Logo" class="logo" height="20px" />
        </button>
        <div class="new-product">
          <button @click="newProduto">Criar novo</button>
        </div>
      </div>

      <!-- Lista de Produtos -->
      <div v-for="(produto, index) in filteredProdutos" :key="index" class="card">
        <div class="card-content">
          <div class="info">
            <p style="font-size: 25px"><strong>{{ produto.nome }}</strong></p>
            <p style="font-size: 15px"><strong>Descrição:</strong> {{ produto.descricao_produto }}</p>
            <p style="font-size: 15px"><strong>Preço:</strong> {{ produto.preco | currency }}</p>
          </div>
          <div class="button-group">
            <button class="edit-button" @click="editarProduto(produto.id_produto)">Editar</button>
            <button class="delete-button" @click="deletarProduto(produto.id_produto)">Deletar</button>
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
      produtos: [],
      searchQuery: '',
    };
  },
  computed: {
    filteredProdutos() {
      return this.produtos.filter(produto => {
        return produto.nome.toLowerCase().includes(this.searchQuery.toLowerCase());
      });
    }
  },
  methods: {
    async carregarProdutos() {
      try {
        const token = localStorage.getItem('authToken');
        if (!token) {
          console.error('Usuário não autenticado.');
          return;
        }

        const response = await axios.get('http://localhost:8000/storage_management/produtos/', {
          headers: { Authorization: `Bearer ${token}` }
        });

        this.produtos = response.data;
      } catch (error) {
        console.error('Erro ao carregar produtos:', error);
      }
    },

    editarProduto(produtoId) {
      this.$router.push({ name: 'edit-produtos', params: { id: produtoId } });
    },

    async deletarProduto(produtoId) {
      try {
        const token = localStorage.getItem('authToken');
        if (!token) {
          console.error('Usuário não autenticado.');
          return;
        }

        const confirmDelete = confirm('Tem certeza que deseja deletar este produto?');
        if (confirmDelete) {
          await axios.delete(`http://localhost:8000/storage_management/produtos/${produtoId}/`, {
            headers: { Authorization: `Bearer ${token}` }
          });
          this.produtos = this.produtos.filter(produto => produto.id_produto !== produtoId);
          console.log('Produto excluído com sucesso!');
        }
      } catch (error) {
        console.error('Erro ao excluir produto:', error);
      }
    },

    newProduto() {
      // Redireciona para a página de criação de novo produto
      this.$router.push({ name: 'create-produtos' });
    },

    searchProdutos() {
      console.log('Buscando por: ', this.searchQuery);
    }
  },
  mounted() {
    this.carregarProdutos();
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

.new-product {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-left: 20px;
}

.new-product button {
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

.new-product button:hover {
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
