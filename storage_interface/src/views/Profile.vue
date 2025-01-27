<template>
  <div class="profile-page">
    <!-- Inclui a Sidebar como um componente -->
    <Sidebar />
  
    <!-- Conteúdo principal -->
    <main class="main-content">
      <!-- Barra de Pesquisa -->
      <div class="search-bar">
        <input type="text" placeholder="Pesquisar" />
        <button>🔍</button>
      </div>
  
      <!-- Seção do Perfil -->
      <div class="profile-header">
        <h1 style="margin: 0; font-size: 50px; margin-top: 30px">Meu Perfil</h1>
        <p style="margin: 0; font-size: 20px">Gerencie suas informações e preferências</p>
      </div>
  
      <!-- Detalhes do Perfil -->
      <div class="profile-details">
        <div class="profile-info">
          <img src="@/assets/profile_pattern.jpeg" alt="Foto de Perfil" class="profile-picture" />
          <div class="details">
            <h2>Fulaninho da Silva</h2>
            <p>Email: fulaninho@example.com</p>
            <p>Telefone: (11) 12345-6789</p>
          </div>
        </div>
      </div>
  
      <!-- Ações -->
      <div class="actions">
        <button @click="editProfile">Editar Perfil</button>
        <button @click="changePassword">Alterar Senha</button>
      </div>
    </main>
  </div>
</template>

<script>
import Sidebar from "@/components/Sidebar.vue";

export default {
  name: "Profile",
  components: {
    Sidebar,
  },
  methods: {
    editProfile() {
      // Lógica para editar o perfil
      alert('Editar perfil');
    },
    changePassword() {
      // Lógica para alterar a senha
      alert('Alterar senha');
    }
  }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Afacad&display=swap');

.profile-page {
  display: flex;
  flex-direction: row; /* Sidebar e conteúdo ao lado */
  height: 100vh; /* Garante que a página ocupe toda a altura da tela */
  background-color: #ffffff;
  font-family: 'Afacad', sans-serif;
}

.main-content {
  display: flex;
  flex-direction: column; /* Organiza o conteúdo em coluna */
  flex: 1; /* Faz o conteúdo principal ocupar o restante da altura disponível */
  padding: 16px;
  overflow-y: auto; /* Permite a rolagem quando o conteúdo ultrapassar a altura da tela */
}


.search-bar {
  display: flex;
  align-items: center;
  justify-content: center; /* Centraliza os elementos horizontalmente */
  width: 100%; /* Garante que a barra ocupe toda a largura disponível */
  gap: 10px; /* Espaçamento entre os elementos */
}

.search-bar input {
  width: 70%; /* Ajusta a largura do campo de pesquisa */
  padding: 10px;
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

.profile-header {
  margin-bottom: 24px;
}

.profile-header h1 {
  font-size: 2rem;
  color: #333;
}

.profile-header p {
  font-size: 1rem;
  color: #666;
}

.profile-details {
  display: flex;
  gap: 20px;
  margin-bottom: 24px;
}

.profile-info {
  display: flex;
  align-items: center;
  gap: 20px;
}

.profile-picture {
  width: 120px;
  height: 120px;
  border-radius: 50%;
}

.details h2 {
  font-size: 2rem;
  color: #333;
}

.details p {
  font-size: 1rem;
  color: #666;
}

.actions {
  display: flex;
  gap: 16px;
}

.actions button {
  padding: 10px 20px;
  background-color: #FFD1A3;
  border: 1px solid black;
  border-radius: 10px;
  color: black;
  font-size: 16px;
  cursor: pointer;
}

.actions button:hover {
  background-color: #F8B500;
}
</style>
