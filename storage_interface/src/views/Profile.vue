<template>
    <div class="profile-page">
      <!-- Inclui a Sidebar como um componente -->
      <Sidebar />
  
      <main class="main-content">
        <!-- Barra de Pesquisa -->
        <div class="search-bar">
          <input type="text" placeholder="Pesquisar" />
          <button>🔍</button>
        </div>
  
        <!-- Seção do Perfil -->
        <div class="profile-header">
          <h1 style="margin: 0; font-size: 50px">Meu Perfil</h1>
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
    background-color: #ffffff; /* Fundo leve para contraste */
    font-family: 'Afacad', sans-serif; /* Definir a fonte Afacad */
  }
  
  .main-content {
    margin-left: 30px;
    flex: 1;
    padding: 16px;
  }
  
  .search-bar {
    display: flex;
    gap: 8px;
    margin-bottom: 16px;
  }
  
  .search-bar input {
    width: 100%;
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  
  .search-bar button {
    width: 50%;
    padding: 10px;
    background-color: #FFD1A3;
    border: 1px solid black;
    border-radius: 10px;
    color: black;
    font-size: 16px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    display: block;
    margin-left: auto;
    margin-right: auto;
  }
  
  .search-bar button:hover {
    background-color: #F8B500;
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
    width: 120px;  /* Aumenta a imagem do perfil */
    height: 120px; /* Aumenta a imagem do perfil */
    border-radius: 50%;
  }
  
  .details h2 {
    font-size: 2rem;  /* Aumenta o nome */
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
  