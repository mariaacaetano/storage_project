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

      <!-- Lista de funcionários -->
      <div v-for="(funcionario, index) in filteredFuncionarios" :key="index" class="card">
        <div class="card-content">
          <div class="info">
            <p style="font-size:25px"><strong>{{ funcionario.first_name }} {{ funcionario.last_name }}</strong></p>
            <p style="font-size:15px"><strong>Cargo:</strong> {{ funcionario.role }}</p>
            <p style="font-size:15px"><strong>Matrícula:</strong> {{ funcionario.registration }}</p>
            <p style="font-size:15px"><strong>CPF:</strong> {{ funcionario.cpf }}</p>
            <p style="font-size:15px"><strong>Situação:</strong> {{ funcionario.situation }}</p>
            <p style="font-size:15px"><strong>Permissão:</strong> {{ funcionario.permission }}</p>
            <p style="font-size:15px"><strong>Telefone:</strong> {{ funcionario.phone_number }}</p>
          </div>
          <div class="button-group">
            <button class="view-button" @click="verFuncionario(funcionario)">Ver</button>
            <button class="edit-button" @click="editarFuncionario(funcionario.id)">Editar</button>
            <button class="delete-button" @click="deletarFuncionario(funcionario.id)">Deletar</button>
          </div>
        </div>
      </div>
    </main>

    <!-- Modal de Foto de Perfil -->
    <div v-if="showModal" class="modal">
      <div class="modal-content">
        <span class="close" @click="fecharModal">&times;</span>
        <img :src="selectedProfilePhoto" alt="Foto de Perfil" class="modal-image"/>
        <p>{{ selectedFuncionario.first_name }} {{ selectedFuncionario.last_name }}</p> <!-- Nome do funcionário -->
      </div>
    </div>
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
      funcionarios: [],
      searchQuery: '',
      erro: null,
      showModal: false,
      selectedProfilePhoto: '',  // Para armazenar a foto de perfil selecionada
      selectedFuncionario: {}    // Para armazenar o funcionário selecionado
    };
  },
  computed: {
    filteredFuncionarios() {
      return this.funcionarios.filter(funcionario => {
        const fullName = `${funcionario.first_name} ${funcionario.last_name}`.toLowerCase();
        return (
          fullName.includes(this.searchQuery.toLowerCase()) ||
          funcionario.position?.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
          funcionario.registration?.includes(this.searchQuery)
        );
      });
    }
  },
  methods: {
    async carregarFuncionarios() {
      try {
        const token = localStorage.getItem('authToken'); // Pegando o token salvo no login
        if (!token) {
          console.error('Usuário não autenticado.');
          return;
        }

        const response = await axios.get('http://localhost:8000/customuser/employees/', {
          headers: { Authorization: `Bearer ${token}` }
        });

        this.funcionarios = response.data;
      } catch (error) {
        console.error("Erro ao carregar funcionários:", error);
      }
    },
    verFuncionario(funcionario) {
      // Exibe a foto de perfil do funcionário ao apertar o botão "Ver"
      if (funcionario.profile_photo) {
        this.selectedFuncionario = funcionario; // Armazena o funcionário selecionado
        this.selectedProfilePhoto = `http://127.0.0.1:8000/media/${funcionario.profile_photo}`;
        this.showModal = true;  // Abre o modal
      } else {
        alert('Este funcionário não possui foto de perfil.');
      }
    },
    editarFuncionario(id) {
      // Redireciona para a página de edição com o ID do funcionário
      this.$router.push({ name: 'edit-funcionarios', params: { id } });
    },
    deletarFuncionario(id) {
      // Redireciona para a página de exclusão com o ID do funcionário
      this.$router.push({ name: 'delete-funcionarios', params: { id } });

    },
    fecharModal() {
      this.showModal = false;  // Fecha o modal
      this.selectedProfilePhoto = '';  // Limpa a foto selecionada
      this.selectedFuncionario = {};  // Limpa o funcionário selecionado
    }
  },
  mounted() {
    this.carregarFuncionarios();
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

.card {
  display: flex;
  flex-direction: column; /* Torna o layout do card vertical */
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

.card .card-content {
  display: flex;
  flex-direction: column; /* Mantém o conteúdo do card organizado em uma coluna */
  flex-grow: 1; /* Faz o conteúdo crescer para ocupar o espaço restante */
}

.card p {
  margin: 0;
}

.button-group {
  display: flex;
  justify-content: flex-end; /* Alinha os botões à direita */
  gap: 7px;
}

.general-button,
.view-button,
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

.general-button:hover,
.view-button:hover,
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

/* Estilos do Modal */
.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal-content {
  padding: 20px;
  border-radius: 8px;
  text-align: center;
  position: relative;
}

.modal-content p{
  color: #fff;
  font-size: 20px;
}

.modal-image {
  max-width: 60%;
  max-height: 80vh;
  border-radius: 200px;
}

.close {
  position: absolute;
  top: 10px;
  right: 10px;
  font-size: 30px;
  color: #ffffff;
  cursor: pointer;
}

.close:hover {
  color: #000;
}
</style>
