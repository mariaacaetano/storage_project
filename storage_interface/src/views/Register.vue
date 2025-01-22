<template>
    <div class="register-container">
      <div class="logo-container">
        <img :src="logo" alt="Storage Logo" class="logo" />
      </div>
      <form @submit.prevent="handleRegister" style="padding: 10px">
        <h1>Cadastre-se</h1>
        <div class="form-group">
          <input
            type="text"
            id="primeironome"
            v-model="primeironome"
            placeholder="Primeiro nome"
            required
          />
        </div>
  
        <div class="form-group">
          <input
            type="text"
            id="ultimonome"
            v-model="ultimonome"
            placeholder="Último nome"
            required
          />
        </div>
  
        <div class="form-group">
          <input
            type="text"
            id="matricula"
            v-model="matricula"
            placeholder="Matrícula"
            required
          />
        </div>
  
        <div class="form-group">
          <input
            type="email"
            id="email"
            v-model="email"
            placeholder="E-mail"
            required
          />
        </div>
  
        <div class="form-group">
          <input
            type="password"
            id="password"
            v-model="password"
            placeholder="Senha"
            required
          />
        </div>
  
        <div class="form-group">
          <input
            type="password"
            id="confirmPassword"
            v-model="confirmPassword"
            placeholder="Confirme a senha"
            required
          />
        </div>
  
        <button type="submit">Registrar</button>
  
        <p>Já tem um cadastro? <router-link to="/login">Clique aqui</router-link>.</p>
      </form>
    </div>
    <footer class="pattern-footer">
      <p>
        Projeto apresentado para avaliação parcial da disciplina de
        Desenvolvimento Web II no Instituto Federal Catarinense - Campus
        Araquari. 2025.
      </p>
    </footer>
  </template>
  
  <script>
  import axios from "axios";
  import logo from "@/assets/storage_logo.png"; // Caminho correto para o logo
  
  export default {
    name: "RegisterPage",
    data() {
      return {
        primeironome: "",
        ultimonome: "",
        matricula: "",
        email: "",
        password: "",
        confirmPassword: "",
        logo: logo,
      };
    },
    methods: {
      async handleRegister() {
        // Verificar se as senhas coincidem
        if (this.password !== this.confirmPassword) {
          alert("As senhas não coincidem");
          return;
        }
  
        try {
          // Dados que serão enviados para a API
          const userData = {
            first_name: this.primeironome,
            last_name: this.ultimonome,
            registration: this.matricula,
            email: this.email,
            password: this.password,
          };
  
          // Endpoint da API Django (substituir pela URL correta)
          const apiUrl = "http://127.0.0.1:8000/customuser/signup/";
  
          // Requisição POST usando Axios
          const response = await axios.post(apiUrl, userData);
  
          if (response.status === 201) {
            // Cadastro bem-sucedido
            alert("Cadastro realizado com sucesso! Faça login para continuar.");
            this.$router.push("/login");
          } else {
            alert("Erro ao cadastrar. Por favor, tente novamente.");
          }
        } catch (error) {
          console.error("Erro ao realizar cadastro:", error);
          alert("Houve um problema ao cadastrar. Verifique os dados e tente novamente.");
        }
      },
    },
  };
  </script>
  
  <style scoped>
  @import url("https://fonts.googleapis.com/css2?family=Afacad&display=swap");
  
  .register-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh; /* 100% da altura da tela */
    background-color: #ffffff; /* Fundo leve para contraste */
    font-family: "Afacad", sans-serif; /* Definir a fonte Afacad */
  }
  
  .form-group {
    border-radius: 4px; /* Bordas arredondadas */
    width: 400px;
    margin-bottom: 15px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  }
  
  .logo {
    max-width: 400px; /* Tamanho máximo da imagem */
    width: 100%;
    height: auto;
  }
  
  .logo-container {
    display: flex;
    margin-right: 50px;
  }
  
  .pattern-footer {
    font-family: "Afacad", sans-serif;
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
    background-color: #ffd1a3;
    border: solid, 1px;
    border-radius: 10px;
    color: black;
    font-size: 16px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  }
  
  button:hover {
    background-color: #f8b500;
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
  