<template>
  <div class="funcionario-page">
    <!-- Sidebar -->
    <Sidebar />

    <main class="main-content">
      <section class="edit-section">
        <h2>Editar funcionário</h2>
        <form @submit.prevent="salvar">
          <label>Primeiro Nome</label>
          <input type="text" v-model="funcionario.primeiroNome" />

          <label>Último Nome</label>
          <input type="text" v-model="funcionario.ultimoNome" />

          <label>Telefone</label>
          <input type="text" v-model="funcionario.telefone" />

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
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';
import Sidebar from "@/components/Sidebar.vue";

export default {
  components: { Sidebar },
  setup() {
    const router = useRouter();
    const funcionario = ref({
      primeiroNome: '',
      ultimoNome: '',
      telefone: '',
      situacao: '',
      cargo: '',
      permissao: '',
      matricula: '',
      cpf: '',
      profilePhoto: null,  // Para armazenar a imagem
    });

    const carregarFuncionario = async () => {
      try {
        const response = await axios.get("http://127.0.0.1:8000/customuser/user-info/", {
          headers: {
            Authorization: `Bearer ${localStorage.getItem("authToken")}`,
          },
        });

        funcionario.value = {
          primeiroNome: response.data.first_name,
          ultimoNome: response.data.last_name,
          telefone: response.data.phone_number,
          situacao: response.data.situation,
          cargo: response.data.role,
          permissao: response.data.is_staff ? "Administrador" : "Somente Consulta",
          matricula: response.data.registration,
          cpf: response.data.cpf,
          profilePhoto: response.data.profile_photo ? `http://127.0.0.1:8000/media/${response.data.profile_photo}` : null,  // Exibe a imagem com base no caminho
        };
      } catch (error) {
        console.error("Erro ao buscar informações do usuário:", error.response || error);
      }
    };

    onMounted(carregarFuncionario);

    const uploadImagem = (event) => {
      const file = event.target.files[0];
      if (file) {
        funcionario.value.profilePhoto = file;  // Armazena o arquivo selecionado
      }
    };

    const salvar = async () => {
  try {
    const token = localStorage.getItem('authToken');
    if (!token) {
      console.error('Usuário não autenticado.');
      return;
    }

    const formData = new FormData();
    formData.append('first_name', funcionario.value.primeiroNome);
    formData.append('last_name', funcionario.value.ultimoNome);
    formData.append('phone_number', funcionario.value.telefone);
    formData.append('situation', funcionario.value.situacao);
    formData.append('role', funcionario.value.cargo);
    formData.append('registration', funcionario.value.matricula);
    formData.append('cpf', funcionario.value.cpf);
    formData.append('is_staff', funcionario.value.permissao === "Admin" ? true : false);

    if (funcionario.value.profilePhoto) {
      formData.append('profile_photo', funcionario.value.profilePhoto); // Envia o arquivo da imagem
    }

    const response = await axios.put(
      "http://127.0.0.1:8000/customuser/user-info/",  // Verifique a URL da sua API
      formData,
      {
        headers: {
          Authorization: `Bearer ${token}`,
          'Content-Type': 'multipart/form-data',
        },
      }
    );

    if (response.status === 200) {
      alert('Dados salvos com sucesso!');
      router.push('/profile');
    }
  } catch (error) {
    console.error('Erro ao salvar dados do funcionário:', error);
    alert('Erro ao salvar dados do funcionário.');
  }
};

    const voltar = () => router.push('/profile');

    return { funcionario, uploadImagem, salvar, voltar };
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
