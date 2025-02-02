<template>
  <div class="profile-page">
    <Sidebar />
  
    <main class="main-content">
      <div class="search-bar">
        <input type="text" placeholder="Pesquisar" />
        <button>
          <img src="@/assets/icones/icone-lupa.png" alt="Buscar" class="logo" height="20px">
        </button>
      </div>
  
      <div class="profile-header">
        <h1 style="margin: 0; font-size: 50px; margin-top: 30px">Meu Perfil</h1>
        <p style="margin: 0; font-size: 20px">Gerencie suas informações e preferências</p>
      </div>
  
      <div class="profile-details">
        <div class="profile-info">
          <img :src="getImageUrl(userProfile.profile_photo)" alt="Foto de Perfil" class="profile-picture" />
          <div class="details">
            <h2>{{ userProfile.full_name || 'Nome não disponível' }}</h2>
            <p><strong>Cargo: </strong> {{ userProfile.role || 'Cargo não disponível' }}</p>
            <p><strong>E-mail: </strong> {{ userProfile.email || 'Email não disponível' }}</p>
            <p><strong>Contato: </strong> {{ userProfile.phone_number || 'Telefone não disponível' }}</p>
          </div>
        </div>
      </div>
  
      <div class="actions">
        <router-link to="/profile/edit-profile">
          <button>
            Editar Perfil
          </button>
        </router-link>
        <button @click="changePassword">Alterar Senha</button>
      </div>
    </main>
  </div>
</template>

<script>
import axios from "axios";
import Sidebar from "@/components/Sidebar.vue";

export default {
  name: "Profile",
  components: {
    Sidebar,
  },
  data() {
    return {
      userProfile: {
        name: '',
        email: '',
        phone_number: '',
        profile_photo: '',
      },
    };
  },
  created() {
    this.fetchUserProfile();
  },
  methods: {
    async fetchUserProfile() {
      try {
        const response = await axios.get("http://127.0.0.1:8000/customuser/user-info/", {
          headers: {
            Authorization: `Bearer ${localStorage.getItem("authToken")}`, // Supondo que o token esteja no localStorage
          },
        });
        console.log("Dados do usuário:", response.data);  // Verifica os dados retornados da API
        this.userProfile = response.data;
      } catch (error) {
        console.error("Erro ao buscar informações do usuário:", error.response || error);
        if (error.response && error.response.status === 401) {
          console.error("Token inválido ou expirado.");
        }
      }
    },
    changePassword() {
      alert('Essa funcionalidade ainda não foi implementada');
    },

    getImageUrl(profilePhoto) {
    // Verifica se a foto é um caminho relativo, que começa com "profile_pictures/"
    if (profilePhoto) {
      if (profilePhoto.startsWith('profile_pictures/')) {
        return `http://localhost:8000/media/${profilePhoto}`;
      }
      // Se já for uma URL completa (http), retorna a URL diretamente
      if (profilePhoto.startsWith('http')) {
        return profilePhoto;
      }
    }
    // Se não houver foto, retorna uma imagem padrão
    return '/path/to/default-profile.jpg';
  }
}
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Afacad&display=swap');

.profile-page {
  display: flex;
  flex-direction: row;
  height: 100%;
  background-color: #ffffff;
  gap: 40px;
  font-family: 'Afacad', sans-serif;
}

.main-content {
  display: flex;
  flex-direction: column;
  flex: 1;
  padding: 10px;
  overflow-y: auto;
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
