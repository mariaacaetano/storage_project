<template>
  <div class="home">
    <!-- Sidebar -->
    <Sidebar />

    <!-- Conteúdo principal -->
    <main class="main-content">
      <h1 style="font-size:50px; margin: 0;">Fornecedores</h1>
      <div class="search-bar">
        <input type="text" v-model="searchQuery" placeholder="Pesquisar" />
        <button @click="searchFuncionarios">🔍</button>

        <!-- Botão Criar Novo ao lado da search-bar -->
        <div class="new-employee">
          <button @click="newExmployee">Criar novo</button>
        </div>
      </div>

      <!-- Lista de funcionários -->
      <div v-for="funcionario in filteredFuncionarios" :key="funcionario.id" class="card">
        <p style="font-size: 30px;"><strong>{{ funcionario.nome }}</strong></p>
        <p><strong>Matrícula:</strong> {{ funcionario.matricula }}</p>
        <p><strong>CPF:</strong> {{ funcionario.cpf }}</p>
        <p><strong>Situação:</strong> {{ funcionario.situacao }}</p>
        <p><strong>Permissão:</strong> {{ funcionario.permissao }}</p>
        <p><strong>Telefone:</strong> {{ funcionario.contato }}</p>

        <div style="display: flex; justify-content: flex-end; align-items: center;">
          <button class="general-button" @click="editarFuncionario(funcionario.id)">Ver</button>
          <button class="general-button" @click="editarFuncionario(funcionario.id)">Editar</button>
          <button class="delete-button" @click="deletarFuncionario(funcionario.id)">Deletar</button>
        </div>

      </div>
    </main>
  </div>
</template>

<script>
import Sidebar from "@/components/Sidebar.vue";
import { ref, computed } from "vue";

export default {
  name: "Funcionarios",
  components: {
    Sidebar,
  },
  setup() {
    // Dados fictícios de funcionários
    const funcionarios = ref([
      { id: 1, nome: "João Silva", matricula: "1234", cpf: "123.456.789-10", situacao: "Trabalhando", permissao:"Acesso Vendedor", contato: "(47) 91234-6789"},
      { id: 2, nome: "Maria Costa", matricula: "1212", cpf: "098.765.432-11", situacao: "Trabalhando", permissao:"Acesso Vendedor", contato: "(47) 91212-3434"},
      { id: 3, nome: "Carlos Pereira", matricula: "5678", cpf: "234.567.890-12", situacao: "Trabalhando", permissao: "Acesso Gerente", contato: "(47) 92345-6789" },
      { id: 4, nome: "Ana Costa", matricula: "4321", cpf: "345.678.901-23", situacao: "Em licença", permissao: "Acesso Supervisor", contato: "(47) 93456-7890" },
      { id: 5, nome: "Felipe Souza", matricula: "8765", cpf: "456.789.012-34", situacao: "Trabalhando", permissao: "Acesso Administrador", contato: "(47) 94567-8901" },

    ]);

    // Variável para busca
    const searchQuery = ref("");

    // Filtrando funcionários com base na pesquisa
    const filteredFuncionarios = computed(() => {
      return funcionarios.value.filter((funcionario) => 
        funcionario.nome.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
        funcionario.cargo.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
        funcionario.localizacao.toLowerCase().includes(searchQuery.value.toLowerCase())
      );
    });

    // Função para editar funcionário
    const editarFuncionario = (id) => {
      console.log(`Editando funcionário com id: ${id}`);
    };

    // Função para deletar funcionário
    const deletarFuncionario = (id) => {
      console.log(`Deletando funcionário com id: ${id}`);
      funcionarios.value = funcionarios.value.filter(funcionario => funcionario.id !== id);
    };

    // Função de busca
    const searchFuncionarios = () => {
      console.log("Buscando por: ", searchQuery.value);
    };

    return {
      funcionarios,
      searchQuery,
      filteredFuncionarios,
      editarFuncionario,
      deletarFuncionario,
      searchFuncionarios,
    };
  },
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Afacad&display=swap');

.home {
  display: flex;
  font-family: 'Afacad', sans-serif; /* Definir a fonte Afacad */
}

.main-content {
  flex: 1;
  padding-left: 16px; /* Dá espaço suficiente para a sidebar */
  background-color: #ffffff;
}


.search-bar {
  display: flex;
  align-items: center;
  justify-content: flex-start; /* Alinha os itens à esquerda */
  width: 100%; /* Garante que a barra ocupe toda a largura disponível */
  gap: 10px; /* Espaçamento entre os elementos */
  margin-bottom: 50px;
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

.card:hover{
  background-color: #fddeb8;
}

.card p{
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
