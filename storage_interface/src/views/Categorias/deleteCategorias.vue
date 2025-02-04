<template>
  <div class="home">
    <!-- Sidebar -->
    <Sidebar />

    <!-- Conteúdo principal -->
    <main class="main-content">
      <h1 class="title">Funcionários</h1>

      <div class="search-bar">
        <input type="text" v-model="searchQuery" placeholder="Pesquisar" />
        <button @click="searchFuncionarios">
          <img src="@/assets/icones/icone-lupa.png" alt="Buscar" class="logo" height="20px">
        </button>
      </div>
      <div class="delete-session">
        <p v-if="categoria">
          Tem certeza que deseja deletar <strong>{{ categoria.nome }}</strong>? Esta ação não poderá ser desfeita.
        </p>
        <p v-else>Carregando dados do categoria...</p>
        <button class="edit-button" @click="voltar">Voltar</button>
        <button class="delete-button" @click="deletarFuncionario(categoria.id)" v-if="categoria">Deletar</button>
      </div>
    </main>
  </div>
</template>



<script>
import axios from "axios";
import Sidebar from "@/components/Sidebar.vue";

export default {
  components: {
    Sidebar,
  },
  data() {
    return {
      categoria: null,
      searchQuery: "",
      categoriaId: null, // Corrigido: Adicionando categoriaId ao data()
    };
  },
  created() {
    this.categoriaId = this.$route.params.id; // Obtendo ID da URL corretamente
    this.fetchCategoria();
  },
  methods: {
    async fetchCategoria() {
      if (!this.categoriaId) {
        console.error("ID da categoria não encontrado na URL.");
        return;
      }

      try {
        const token = localStorage.getItem("authToken");
        if (!token) {
          console.error("Usuário não autenticado.");
          return;
        }

        const response = await axios.get(
          `http://127.0.0.1:8000/storage_management/categorias/detail/${this.categoriaId}/`, // Uso de `this.categoriaId`
          {
            headers: { Authorization: `Bearer ${token}` },
          }
        );
        this.categoria = response.data;
      } catch (error) {
        console.error("Erro ao buscar categoria:", error);
        alert("Erro ao carregar informações da categoria.");
      }
    },

    async deletarFuncionario() { // Removi `id` pois já temos `this.categoriaId`
      if (!this.categoriaId) {
        console.error("ID da categoria não encontrado.");
        return;
      }

      try {
        const token = localStorage.getItem("authToken");
        if (!token) {
          console.error("Usuário não autenticado.");
          return;
        }

        await axios.delete(
          `http://127.0.0.1:8000/storage_management/categorias/${this.categoriaId}/delete/`, // Uso de `this.categoriaId`
          {
            headers: { Authorization: `Bearer ${token}` },
          }
        );
        alert("Categoria deletada com sucesso!");
        this.$router.push("/categorias"); // Redirecionar após exclusão
      } catch (error) {
        console.error("Erro ao deletar categoria:", error);
        alert("Erro ao deletar categoria.");
      }
    },

    voltar() {
      this.$router.go(-1);
    },
  },
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

.edit-button,
.delete-button {
  padding: 10px;
  border-radius: 20px;
  width: 100px;
  cursor: pointer;
  margin-right: 10px;
  box-shadow: 2px 2px 5px #a7a7a7;
  border: 1px solid rgb(0, 0, 0);
  font-size: 16px;
  text-align: center;
}

.edit-button {
  background-color: #f0aa54;
  color: rgb(0, 0, 0);
}

.edit-button:hover {
  background-color: #c88a3d;
}

.delete-button {
  background-color: #cf0e00;
  color: white;
}

.delete-button:hover {
  background-color: #a20a08;
}

.delete-session {
  padding: 10px;
}

.delete-session p {
  font-size: 18px;
}
</style>
