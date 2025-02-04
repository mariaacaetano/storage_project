<template>
    <div class="fornecedor-page">
      <!-- Sidebar -->
      <Sidebar />
  
      <main class="main-content">
        <h1 style="font-size:50px; margin: 0;">Criar Fornecedor</h1>
  
        <section class="edit-section">
          <h2>Cadastro de Fornecedor</h2>
          <form @submit.prevent="salvar">
            <label>Razão Social</label>
            <input type="text" v-model="fornecedor.razao_social" required />
  
            <label>Nome Fantasia</label>
            <input type="text" v-model="fornecedor.nome_fantasia" required />
  
            <label>CNPJ</label>
            <input type="text" v-model="fornecedor.cnpj" required />
  
            <label>Inscrição Estadual</label>
            <input type="text" v-model="fornecedor.inscricao_estadual" required />
  
            <label>Telefone</label>
            <input type="text" v-model="fornecedor.telefone" required />
  
            <label>Endereço</label>
            <input type="text" v-model="fornecedor.endereco" required />
  
            <label>Tipo de Produto</label>
            <input type="text" v-model="fornecedor.tipo_produto" required />
  
            <div class="buttons">
              <button class="voltar" @click="voltar">Voltar</button>
              <button class="editar" type="submit">Salvar</button>
            </div>
          </form>
        </section>
      </main>
    </div>
  </template>
  
  <script>
  import { ref } from 'vue';
  import { useRouter } from 'vue-router';
  import axios from 'axios';
  import Sidebar from "@/components/Sidebar.vue";
  
  export default {
    components: { Sidebar },
    setup() {
      const router = useRouter();
      const fornecedor = ref({
        razao_social: '',
        nome_fantasia: '',
        cnpj: '',
        inscricao_estadual: '',
        telefone: '',
        endereco: '',
        tipo_produto: ''
      });
  
      // Função para salvar o fornecedor
      const salvar = async () => {
        try {
          const token = localStorage.getItem('authToken');
          if (!token) {
            console.error('Usuário não autenticado.');
            return;
          }
  
          // Faz a requisição para criar o fornecedor
          const response = await axios.post(
            `http://127.0.0.1:8000/storage_management/create_fornecedor/`,
            {
              razao_social: fornecedor.value.razao_social,
              nome_fantasia: fornecedor.value.nome_fantasia,
              cnpj: fornecedor.value.cnpj,
              inscricao_estadual: fornecedor.value.inscricao_estadual,
              telefone: fornecedor.value.telefone,
              endereco: fornecedor.value.endereco,
              tipo_produto: fornecedor.value.tipo_produto
            },
            {
              headers: { Authorization: `Bearer ${token}` },
            }
          );
  
          if (response.status === 201) {
            alert('Fornecedor criado com sucesso!');
            router.push('/fornecedor');
          }
        } catch (error) {
          console.error('Erro ao salvar fornecedor:', error);
          alert('Erro ao salvar fornecedor. Verifique o console para mais detalhes.');
        }
      };
  
      // Função para voltar à lista de fornecedores
      const voltar = () => {
        router.push('/fornecedor');
      };
  
      return { fornecedor, salvar, voltar };
    },
  };
  </script>
  
  <style scoped>
  @import url('https://fonts.googleapis.com/css2?family=Afacad&display=swap');
  
  .fornecedor-page {
    display: flex;
    font-family: 'Afacad', sans-serif;
    background-color: #ffffff;
  }
  
  .main-content {
    flex: 1;
    padding: 2rem;
  }
  
  .edit-section {
    background: #fff;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
  }
  
  form {
    display: flex;
    flex-direction: column;
  }
  
  label {
    margin-top: 10px;
    font-weight: bold;
  }
  
  input {
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 5px;
    margin-bottom: 10px;
  }
  
  .buttons {
    display: flex;
    justify-content: space-between;
    margin-top: 15px;
  }
  
  .voltar,
  .editar {
    padding: 10px 15px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  
  .voltar {
    background-color: #ddd;
  }
  
  .editar {
    background-color: #f7e0b5;
  }
  </style>
