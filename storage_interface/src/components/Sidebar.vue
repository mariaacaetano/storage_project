<template>
  <div class="sidebar">
    <ul class="menu">
      <li>
        <router-link to="/">
          <img src="@/assets/storage_logo.png" alt="Logo" class="logo" height="220px">
        </router-link>
      </li>
      <li>
        <router-link to="/produtos">
          <i class="icon">
            <img src="@\assets\icones\icone-produtos.png" height="25px">
          </i> Produtos
        </router-link>
      </li>
      <li>
        <router-link to="/categorias">
          <i class="icon">
            <img src="@\assets\icones\icone-categorias.png" height="25px">
          </i> Categorias
        </router-link>
      </li>
      <li>
        <router-link to="/fornecedor">
          <i class="icon">
            <img src="@\assets\icones\icone-fornecedores.png" height="25px">
          </i> Fornecedores
        </router-link>
      </li>
      <li>
        <router-link to="">
          <i class="icon">
            <img src="@\assets\icones\icone-clientes.png" height="25px">
          </i> Clientes
        </router-link>
      </li>
      <li>
        <router-link to="/funcionarios">
          <i class="icon">
            <img src="@\assets\icones\icone-funcionarios.png" height="25px">
          </i> Funcionários
        </router-link>
      </li>
      <li>
        <router-link to="">
          <i class="icon">
            <img src="@\assets\icones\icone-caixa.png" height="25px">
          </i> Caixa
        </router-link>
      </li>
    </ul>
    
     <div class="profile">
        <img src="@/assets/profile_pattern.png" style="height: 60px; margin: 10px"> 
        <div class="profile-details">
          <p class="profile-title" @click="navigateTo('/profile')">Meu Perfil</p> <!-- Redireciona para a página Profile.vue -->
          <p class="name">{{ userProfile.name }}</p>
          <p class="logout" @click="logout">Sair</p> <!-- Redireciona para a página de login -->
        </div>
      </div>
  </div>
</template>

<script>
import userStore from "@/store/userGetInfo.js";

export default {
  name: "Profile",
  components: {},
  computed: {
    // Acessando diretamente o estado da store
    userProfile() {
      return userStore.state.userProfile;
    },
  },
  created() {
    // Se os dados do usuário não estiverem carregados, chamar a ação para obter os dados
    userStore.fetchUserInfo(); // Chama a função para buscar os dados
    console.log(this.userProfile); // Verifique o que está sendo armazenado no state
  },
  methods: {
    editProfile() {
      alert('Editar perfil');
    },
    changePassword() {
      alert('Alterar senha');
    },
    navigateTo(route) {
      this.$router.push(route);
    },
    logout() {
      // Aqui você pode adicionar a lógica de logout, como limpar o token de sessão
      this.$router.push('/login'); // Redireciona para a página de login
    },
  },
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Afacad&display=swap');

.sidebar {
  background-color: #f7e0b5;
  width: 250px;
  position: sticky;
  top: 0;
  padding: 1rem;
  display: flex;
  flex-direction: column;
  font-family: 'Afacad', sans-serif;
  justify-content: space-between;
  z-index: 10;
}

.menu {
  list-style: none;
  padding: 0;
  margin: 0;
}

.menu li {
  display: flex;
  align-items: center;
  padding: 0.5rem 0;
}

.menu li a {
  text-decoration: none;
  color: black;
  display: flex;
  align-items: center;
  font-size: 1rem;
  width: 100%;
  padding: 8px;
}

.menu li a:hover {
  background-color: #f3d89d;
  border-radius: 5px;
}

.icon {
  margin-right: 0.5rem;
}

.profile {
  display: flex;
  align-items: center;
  margin-top: 1rem;
}

.profile-picture {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  margin-right: 8px;
}
.profile-details {
  display: flex;
  flex-direction: column;
  gap: 0.2rem; /* Adiciona um pequeno espaço entre os elementos */
}

.profile-title,
.name,
.logout {
  font-size: 1rem;
  margin: 0; /* Remove margens extras */
  cursor: pointer;
}

.profile .name {
  color: #666;
}

.profile .logout {
  color: #c80000;
  cursor: pointer;
}
</style>
