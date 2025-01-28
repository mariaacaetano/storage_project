// store/userGetInfo.js

import { reactive } from 'vue';
import axios from 'axios';

// Definindo o estado reativo
const state = reactive({
  userProfile: {
    name: "",
    email: "",
    phone: "",
    picture: "@/assets/profile_pattern.jpeg", // Valor padrão
  }
});

// Função para buscar os dados do usuário
async function fetchUserInfo() {
  try {
    const response = await axios.get("http://localhost:8000/customuser/user-info/", {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("authToken")}`, // Autenticando com token
      },
    });

    // Atualizando os dados do usuário
    state.userProfile = {
      name: response.data.full_name,
      email: response.data.email,
      phone: response.data.phone_number,
      picture: response.data.picture || "@/assets/profile_pattern.jpeg", // Se houver, usa a foto, caso contrário, usa a padrão
    };
  } catch (error) {
    console.error("Erro ao carregar informações do usuário:", error);
    alert("Ocorreu um erro ao carregar as informações. Tente novamente mais tarde.");
  }
}

export default {
  state,
  fetchUserInfo,
};
