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

*,
*::before,
*::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html, body {
  height: 100%; /* Faz com que o corpo ocupe toda a altura da tela */
  display: flex;
  flex-direction: column;
}

.home {
  display: flex;
  height: 100vh; /* Define a altura para 100% da altura da tela */
  background-color: #ffffff;
  font-family: 'Afacad', sans-serif;
}

.main-content {
  flex: 1;
  padding: 16px;
  display: flex;
  flex-direction: column;
  justify-content: flex-start; /* Alinha o conteúdo ao topo */
}

.search-bar {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  gap: 10px;
}

.search-bar input {
  width: 70%;
  padding: 10px;
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
