<template>
  <div class="home">
    <!-- Inclui a Sidebar como um componente -->
    <Sidebar />

    <main class="main-content">
      <div class="search-bar">
        <input type="text" placeholder="pesquisar" />
        <button>🔍</button>
      </div>
    </main>
  </div>
</template>

<script>
import Sidebar from "@/components/Sidebar.vue";

export default {
  name: "Home",
  components: {
    Sidebar,
  },
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Afacad&display=swap');

.home {
display: flex;
background-color: #ffffff; /* Fundo leve para contraste */
font-family: 'Afacad', sans-serif; /* Definir a fonte Afacad */
}
.main-content {
  flex: 1;
  padding: 16px;
}
.search-bar {
  display: flex;
  align-items: center;
  justify-content: center; /* Centraliza os elementos horizontalmente */
  width: 100%; /* Garante que a barra ocupe toda a largura disponível */
  gap: 10px; /* Espaçamento entre os elementos */
  margin-bottom: 16px;
}

.search-bar input {
  width: 70%; /* Ajusta a largura do campo de pesquisa */
  padding: 10px;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
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
</style>
