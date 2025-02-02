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
          <p v-if="funcionario">
            Tem certeza que deseja deletar <strong>{{ funcionario.full_name }}</strong>? Esta ação não poderá ser desfeita.
          </p>
          <p v-else>Carregando dados do funcionário...</p>
          <button class="edit-button" @click="voltar">Voltar</button>
          <button class="delete-button" @click="deletarFuncionario(funcionario.id)" v-if="funcionario">Deletar</button>
        </div>
      </main>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  import { useRoute, useRouter } from "vue-router";
  import Sidebar from "@/components/Sidebar.vue";
  
  export default {
    components: {
      Sidebar,
    },
    data() {
      return {
        funcionario: null,
        searchQuery: "",
        funcionarioId: null, // Adicionei a variável funcionarioId aqui
      };
    },
    setup() {
      const route = useRoute();
      const router = useRouter();
      const funcionarioId = route.params.id; // Obtendo o ID da URL
  
      return { funcionarioId, router };
    },
    created() {
      this.funcionarioId = this.$route.params.id; // Atribuindo o id da URL ao data()
      this.fetchFuncionario();
    },
    methods: {
      async fetchFuncionario() {
        if (!this.funcionarioId) {
          console.error("ID do funcionário não encontrado na URL.");
          return;
        }
  
        try {
          const token = localStorage.getItem("authToken");
          const response = await axios.get(
            `http://localhost:8000/customuser/employe_info/${this.funcionarioId}/`,
            {
              headers: { Authorization: `Bearer ${token}` },
            }
          );
          this.funcionario = response.data;
        } catch (error) {
          console.error("Erro ao buscar funcionário:", error);
          alert("Erro ao carregar informações do funcionário.");
        }
      },
      async deletarFuncionario(id) {
        try {
          const token = localStorage.getItem("authToken");
          await axios.delete(
            `http://localhost:8000/customuser/employe_info/${id}/`,
            {
              headers: { Authorization: `Bearer ${token}` },
            }
          );
          alert("Funcionário deletado com sucesso!");
          this.$router.push("/funcionarios"); // Redirecionar após exclusão
        } catch (error) {
          console.error("Erro ao deletar funcionário:", error);
          alert("Erro ao deletar funcionário.");
        }
      },
      voltar() {
        this.$router.go(-1); // Volta para a página anterior
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
  