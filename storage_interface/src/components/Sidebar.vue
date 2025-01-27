<template>
    <div class="sidebar">
      <ul class="menu">
        <li @click="navigateTo('/')">
          <img src="@/assets/storage_logo.png" alt="Logo" style="width: 100%">
        </li>
        <li @click="navigateTo('/produtos')">
          <i class="icon">📦</i> Produtos
        </li>
        <li @click="navigateTo('/categorias')">
          <i class="icon">📋</i> Categorias
        </li>
        <li @click="navigateTo('/fornecedor')">
          <i class="icon">🚚</i> Fornecedores
        </li>
        <li>
          <i class="icon">👥</i> Clientes
        </li>
        <li @click="navigateTo('/funcionarios')">
          <i class="icon">👷</i> Funcionários
        </li>
        <li>
          <i class="icon">💰</i> Caixa
        </li>
      </ul>
      <div class="profile">
        <img src="@/assets/profile_pattern.jpeg" alt="Foto de Perfil" class="profile-picture" />
        <div class="profile-details">
          <p class="profile-title" @click="navigateTo('/profile')">Meu Perfil</p> <!-- Redireciona para a página Profile.vue -->
          <p class="name">Fulaninho da Silva</p>
          <p class="logout" @click="logout">Sair</p> <!-- Redireciona para a página de login -->
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    methods: {
      navigateTo(route) {
        this.$router.push(route);
      },
      logout() {
        // Aqui você pode adicionar a lógica de logout, como limpar o token de sessão
        this.$router.push('/login'); // Redireciona para a página de login
      }
    },
  };
  </script>
  
  <style scoped>
  @import url('https://fonts.googleapis.com/css2?family=Afacad&display=swap');
  
  .sidebar {
  background-color: #f7e0b5;
  width: 250px;
  position: sticky; /* Torna a sidebar "pegajosa", ou seja, ela fica fixa apenas depois de atingir o topo */
  top: 0; /* Fica no topo quando a rolagem atinge */
  padding: 1rem;
  display: flex;
  flex-direction: column;
  font-family: 'Afacad', sans-serif;
  justify-content: space-between;
  z-index: 10; /* Garante que a sidebar não fique atrás de outros conteúdos */
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
    cursor: pointer;
    font-size: 1rem;
  }
  
  .menu li:hover {
    background-color: #f3d89d;
    border-radius: 5px;
  }
  
  .icon {
    margin-right: 0.5rem;
  }
  
  .profile {
    display: flex;
    align-items: center;
    justify-content: flex-start; /* Ajusta o alinhamento à esquerda */
    margin-top: 1rem; /* Ajuste a margem superior para aproximar o perfil dos itens acima */
  }
  
  .profile-picture {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    margin-right: 8px; /* Ajuste o espaço entre a imagem e o nome */
  }
  
  .profile-details {
    display: flex;
    flex-direction: column;
    gap: 0; /* Ajusta o espaço entre os elementos do nome e título */
  }
  
  .profile-title {
    font-size: 1rem;
    margin: 0;
    cursor: pointer; /* Torna o título interativo */
  }
  
  .profile .name {
    font-size: 0.9rem;
    color: #666;
    margin: 0; /* Ajuste a distância entre o título e o nome */
  }
  
  .profile .logout {
    font-size: 0.9rem;
    color: #c80000;
    margin-top: 0px; /* Ajuste a distância entre o título e o nome */
    cursor: pointer; /* Torna o logout interativo */
  }
  </style>
  