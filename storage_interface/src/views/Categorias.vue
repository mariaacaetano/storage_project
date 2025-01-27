<template>
  <div class="home">
    <!-- Sidebar -->
    <Sidebar />

    <!-- Conteúdo principal -->
    <main class="main-content">
      <h1 style="font-size:50px; margin: 0;">Categorias</h1>
      <div class="search-bar">
        <input type="text" v-model="searchQuery" placeholder="Pesquisar" />
        <button @click="searchcategorias">🔍</button>

        <!-- Botão Criar Novo ao lado da search-bar -->
        <div class="new-employee">
          <button @click="newExmployee">Criar novo</button>
        </div>
      </div>

      <!-- Lista de funcionários -->
      <div v-for="categoria in filteredcategorias" :key="categoria.id" class="card">
        <p style="font-size: 30px;"><strong>{{ categoria.nome }}</strong></p>
        <p><strong>Descrição:</strong> {{ categoria.descricao }}</p>

        <div style="display: flex; justify-content: flex-end; align-items: center;">
          <button class="general-button" @click="editarcategoria(categoria.id)">Editar</button>
          <button class="delete-button" @click="deletarcategoria(categoria.id)">Deletar</button>
        </div>

      </div>
    </main>
  </div>
</template>

<script>
import Sidebar from "@/components/Sidebar.vue";
import { ref, computed } from "vue";

export default {
  name: "categorias",
  components: {
    Sidebar,
  },
  setup() {
    // Dados fictícios de funcionários
    const categorias = ref([
      { id: 1, nome: "Maquiagem", descricao:"Qualquer produto de maquiagem (rímel, batom, pó translucido, etc)"},
      { id: 2, nome: "Perfume", descricao: "Fragrâncias diversas para uso pessoal, como eau de toilette, eau de parfum, etc." },
      { id: 3, nome: "Skincare", descricao: "Produtos para cuidados com a pele, como cremes, sabonetes e loções hidratantes." }
    ]);

    // Variável para busca
    const searchQuery = ref("");

    // Filtrando funcionários com base na pesquisa
    const filteredcategorias = computed(() => {
      return categorias.value.filter((categoria) => 
        categoria.nome.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
        categoria.cargo.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
        categoria.localizacao.toLowerCase().includes(searchQuery.value.toLowerCase())
      );
    });

    // Função para editar funcionário
    const editarcategoria = (id) => {
      console.log(`Editando funcionário com id: ${id}`);
    };

    // Função para deletar funcionário
    const deletarcategoria = (id) => {
      console.log(`Deletando funcionário com id: ${id}`);
      categorias.value = categorias.value.filter(categoria => categoria.id !== id);
    };

    // Função de busca
    const searchcategorias = () => {
      console.log("Buscando por: ", searchQuery.value);
    };

    return {
      categorias,
      searchQuery,
      filteredcategorias,
      editarcategoria,
      deletarcategoria,
      searchcategorias,
    };
  },
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Afacad&display=swap');

.home {
  display: flex;
  font-family: 'Afacad', sans-serif; /* Definir a fonte Afacad */
  height: 100vh; /* A altura da tela será 100% da altura da viewport */
}

.main-content {
  flex: 1; /* Faz com que o conteúdo ocupe o restante da altura */
  padding-left: 16px; /* Dá espaço suficiente para a sidebar */
  background-color: #ffffff;
  overflow-y: auto; /* Habilita rolagem vertical quando necessário */
  padding-bottom: 20px; /* Garantir que o conteúdo não fique colado na parte inferior */
  display: flex;
  flex-direction: column;
}

.search-bar {
  display: flex;
  align-items: center;
  justify-content: flex-start; /* Alinha os itens à esquerda */
  width: 100%; /* Garante que a barra ocupe toda a largura disponível */
  gap: 10px; /* Espaçamento entre os elementos */
  margin-bottom: 20px; /* Ajuste o espaçamento para o botão "Criar novo" */
}

.search-bar input {
  width: 70%; /* Ajusta a largura do campo de pesquisa */
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

/* Coloca o botão "Criar novo" ao lado da barra de pesquisa */
.new-employee {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-left: 20px; /* Dá um pequeno espaço entre o botão de pesquisa e o botão de criar */
}

.new-employee button {
  padding: 10px 16px; /* Mais confortável para clique */
  border: px solid rgb(0, 0, 0);
  border-radius: 20px;
  color: black;
  font-size: 16px;
  cursor: pointer;
  background-color: #FFD1A3;
  transition: background-color 0.3s;
  box-shadow: 2px 2px 5px #a7a7a7;
  border: 1px solid rgb(0, 0, 0);
}

.new-employee button:hover {
  background-color: #ffebb2;
}

.card {
  padding: 16px;
  background-color: #fff5db;
  border: 1px solid #ccc;
  border-radius: 8px;
  margin: 8px 0;
  box-shadow: 2px 2px 5px #a7a7a7;
}

.card:hover {
  background-color: #fddeb8;
}

.card p {
  margin: 0;
}

/* Estilos gerais para botões */
.general-button {
  padding: 10px;
  background-color: #f0aa54;
  color: rgb(0, 0, 0);
  border-radius: 20px;
  width: 70px;
  cursor: pointer;
  margin-right: 8px;
  box-shadow: 2px 2px 5px #a7a7a7;
  border: 1px solid rgb(0, 0, 0);
}

.general-button:hover {
  background-color: #c88a3d;
}

/* Estilos específicos para o botão de deletar */
.delete-button {
  padding: 10px;
  background-color: #cf0e00;  /* Cor vermelha */
  border: none;
  color: white;
  border-radius: 20px;
  width: 70px;
  cursor: pointer;
  box-shadow: 2px 2px 5px #a7a7a7;
  border: 1px solid rgb(0, 0, 0);
}

.delete-button:hover {
  background-color: #a20a08;  /* Tom mais escuro de vermelho */
}
</style>
