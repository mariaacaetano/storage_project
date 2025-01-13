<template>
    <div class="login-page">
      <div class="login-container">
        <!-- Imagem do logo -->
        <div class="logo-container">
          <img :src="logo" alt="Storage Logo" class="logo" />
        </div>
        
        
        <form @submit.prevent="handleLogin">
          <div class="form-group">
            <input type="email" id="email" v-model="email" placeholder="Digite seu e-mail" required />
          </div>
  
          <div class="form-group">
            <input type="password" id="password" v-model="password" placeholder="Digite sua senha" required />
          </div>
          <div>
            <p><router-link to="/register">Esqueci a senha.</router-link></p>
          </div>
  
          <button type="submit">Login</button>
  
          <p>Ainda não tem uma conta? <router-link to="/register">Clique aqui</router-link></p>
        </form>
      </div>
    </div>
    <footer class="pattern-footer">
        <p>Projeto apresentado para avaliação parcial da disciplina de Desenvolvimento Web II no Instituto Federal Catarinense - Campus Araquari. 2025.</p>
    </footer>
  </template>
  
  <script>
  import logo from '@/assets/storage_logo.png'; // Importando a imagem
  
  export default {
    name: 'LoginPage',
    data() {
      return {
        email: '',
        password: '',
        logo: logo, // Definindo o logo no data
      };
    },
    methods: {
      handleLogin() {
        console.log('Login realizado com', this.email, this.password);
        // Aqui você pode integrar com a API Django para o login
      }
    }
  };
  </script>
  
  <style scoped>
    /* Centralizar a página */
    @import url('https://fonts.googleapis.com/css2?family=Afacad&display=swap');

    /* Centralizar a página */
    .login-page {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh; /* 100% da altura da tela */
    background-color: #ffffff; /* Fundo leve para contraste */
    font-family: 'Afacad', sans-serif; /* Definir a fonte Afacad */
    }

    .pattern-footer {
        font-family: 'Afacad', sans-serif;
    }

    .login-container {
    width: 300px;
    padding: 20px;
    border-radius: 5px;
    background-color: #fff; /* Fundo branco para o card */
    }
  
  .logo-container {
    text-align: center;
  }
  
  .logo {
    max-width: 300px; /* Ajuste o tamanho conforme necessário */
    max-height: 300px;
  }
  
  .form-group {
    margin-bottom: 15px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* Adiciona uma sombra suave */
   }

  
  label {
    display: block;
    margin-bottom: 5px;
  }
  
  input {
    width: 100%;
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  
  button {
    width: 50%;
    padding: 10px;
    background-color: #FFD1A3;
    border: solid, 1px;
    border-radius: 10px;
    color: black;
    font-size: 16px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }

    button:hover {
    background-color: #F8B500;
    }

    /* Centralizar o botão */
    button {
    margin-top: 15px; /* Adiciona margem para separar do formulário */
    display: block; /* Garante que o botão ocupe a linha inteira */
    margin-left: auto; /* Alinha o botão à esquerda */
    margin-right: auto; /* Alinha o botão à direita, fazendo com que ele fique centralizado */
    }
  
  p {
    margin-top: 10px;
    text-align: center;
  }
  </style>
  