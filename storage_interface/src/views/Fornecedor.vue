// src/views/Fornecedores.vue
<template>
  <div class="home">
    <div class="search-bar">
      <input type="text" placeholder="pesquisar" />
      <button>🔍</button>
    </div>
    <div class="content">
      <h1>Fornecedores</h1>
      <div class="card">
        <p>Descrição: Exemplo de fornecedor</p>
        <p>Localização: Prateleira A1</p>
        <button>Editar</button>
        <button>Deletar</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Fornecedores",
};
</script>

<style scoped>
.home {
  padding: 16px;
}
.search-bar {
  display: flex;
  gap: 8px;
  margin-bottom: 16px;
}
.card {
  padding: 16px;
  border: 1px solid #ccc;
  border-radius: 8px;
  margin: 8px 0;
}
</style>
