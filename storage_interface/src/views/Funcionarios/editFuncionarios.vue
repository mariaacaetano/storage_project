<template>
  <div class="funcionario-page">
    <!-- Sidebar -->
    <Sidebar />

    <main class="main-content">
      <h1 style="font-size:50px; margin: 0;">Funcionários</h1>
      <div class="search-bar">
        <input type="text" v-model="searchQuery" placeholder="Pesquisar" />
        <button @click="searchFuncionarios">🔍</button>
      </div>

      <section class="edit-section">
        <h2>Editar funcionário</h2>
        <form @submit.prevent="salvar">
          <label>Primeiro Nome</label>
          <input type="text" v-model="funcionario.primeiroNome" />

          <label>Último Nome</label>
          <input type="text" v-model="funcionario.ultimoNome" />

          <label>Telefone</label>
          <input type="text" v-model="funcionario.telefone" />

          <label>Situação</label>
          <select v-model="funcionario.situacao">
            <option>Trabalhando</option>
            <option>Férias</option>
            <option>Demitido</option>
          </select>

          <label>Cargo</label>
          <input type="text" v-model="funcionario.cargo" />

          <label>Permissão</label>
          <select v-model="funcionario.permissao">
            <option>Somente Leitura</option>
            <option>Administrador</option>
          </select>

          <label>Matrícula</label>
          <input type="text" v-model="funcionario.matricula" />

          <label>CPF</label>
          <input type="text" v-model="funcionario.cpf" />

          <label>Imagem</label>
          <input type="file" @change="uploadImagem" />

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
import { ref, onMounted, watch } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import axios from 'axios';
import Sidebar from "@/components/Sidebar.vue";

export default {
  components: { Sidebar },
  setup() {
    const router = useRouter();
    const route = useRoute();
    const searchQuery = ref("");
    const funcionario = ref({
      primeiroNome: '',
      ultimoNome: '',
      telefone: '',
      situacao: '',
      cargo: '',
      permissao: '',
      matricula: '',
      cpf: '',
      is_staff: false,
      is_superuser: false,
    });

    // Watcher para monitorar a mudança de permissão
    watch(() => funcionario.value.permissao, (newValue) => {
      if (newValue === "Somente Consulta") {
        funcionario.value.is_staff = true;
        funcionario.value.is_superuser = false;
      } else if (newValue === "Administrador") {
        funcionario.value.is_staff = true;
        funcionario.value.is_superuser = true;
      }
    });

    // Função para carregar os dados do funcionário
    const carregarFuncionario = async () => {
      try {
        const token = localStorage.getItem('authToken');
        if (!token) {
          console.error('Usuário não autenticado.');
          return;
        }

        // Obtém o ID do funcionário da rota
        const id = route.params.id;

        // Faz a requisição para o endpoint específico do funcionário
        const response = await axios.get(`http://127.0.0.1:8000/customuser/employe_info/${id}/`, {
          headers: { Authorization: `Bearer ${token}` },
        });

        // Mapeia os dados retornados para o objeto funcionario
        funcionario.value = {
          primeiroNome: response.data.first_name || '',
          ultimoNome: response.data.last_name || '',
          telefone: response.data.phone_number || '',
          situacao: response.data.situation || 'Trabalhando',
          cargo: response.data.role || '',
          permissao: response.data.is_staff ? "Administrador" : "Somente Consulta",
          matricula: response.data.registration || '',
          cpf: response.data.cpf || '',
          is_staff: response.data.is_staff,
          is_superuser: response.data.is_superuser,
        };
      } catch (error) {
        console.error('Erro ao carregar dados do funcionário:', error);
        alert('Erro ao carregar dados do funcionário. Verifique o console para mais detalhes.');
      }
    };

    // Função para salvar as alterações
    const salvar = async () => {
      try {
        const token = localStorage.getItem('authToken');
        if (!token) {
          console.error('Usuário não autenticado.');
          return;
        }

        const id = route.params.id;

        // Faz a requisição para atualizar os dados do funcionário
        const response = await axios.put(
          `http://127.0.0.1:8000/customuser/employe_info/${id}/`,
          {
            first_name: funcionario.value.primeiroNome,
            last_name: funcionario.value.ultimoNome,
            phone_number: funcionario.value.telefone,
            situation: funcionario.value.situacao,
            permission: funcionario.value.permissao,  // Ajuste aqui para enviar a permissão corretamente
            role: funcionario.value.cargo,
            is_staff: funcionario.value.is_staff,
            is_superuser: funcionario.value.is_superuser,
            registration: funcionario.value.matricula,
            cpf: funcionario.value.cpf,
            profile_photo: funcionario.value.profile_photo, // Adiciona o campo profile_photo, se necessário
          },
          {
            headers: { Authorization: `Bearer ${token}` },
          }
        );

        if (response.status === 200) {
          alert('Dados salvos com sucesso!');
          router.push('/funcionarios'); // Redireciona para a lista de funcionários
        }
      } catch (error) {
        console.error('Erro ao salvar dados do funcionário:', error);
        alert('Erro ao salvar dados do funcionário. Verifique o console para mais detalhes.');
      }
    };


    // Função para lidar com o upload de imagem
    const uploadImagem = async (event) => {
  const file = event.target.files[0];
  if (file) {
    const formData = new FormData();
    formData.append('profile_photo', file);

    const token = localStorage.getItem('authToken');
    if (!token) {
      console.error('Usuário não autenticado.');
      return;
    }

    try {
      const id = route.params.id;

      const response = await axios.put(
        `http://127.0.0.1:8000/customuser/employe_info/${id}/`,
        formData,
        {
          headers: {
            Authorization: `Bearer ${token}`,
            'Content-Type': 'multipart/form-data',
          },
        }
      );

      if (response.status === 200) {
        alert('Foto de perfil salva com sucesso!');
      }
    } catch (error) {
      console.error('Erro ao salvar foto de perfil:', error);
      alert('Erro ao salvar foto de perfil. Verifique o console para mais detalhes.');
    }
  }
};


    // Função para voltar à lista de funcionários
    const voltar = () => {
      router.push('/funcionarios');
    };

    // Carrega os dados do funcionário quando o componente é montado
    onMounted(() => {
      carregarFuncionario();
    });

    return { funcionario, searchQuery, uploadImagem, salvar, voltar };
  },
};
</script>


<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Afacad&display=swap');

.funcionario-page {
  display: flex;
  font-family: 'Afacad', sans-serif;
  background-color: #ffffff;
}

.main-content {
  flex: 1;
  padding: 2rem;
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

input,
select {
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