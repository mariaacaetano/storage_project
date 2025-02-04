<template>
  <div class="produto-page">
    <!-- Sidebar -->
    <Sidebar />
  
    <main class="main-content">
      <h1 style="font-size:50px; margin: 0;">Editar Produto</h1>
  
      <!-- Formulário de Edição -->
      <section class="edit-section">
        <h2>Editar Produto</h2>
        <form @submit.prevent="editarProduto">
          <label>Nome do Produto</label>
          <input type="text" v-model="produto.nome_produto" />

          <label>Categoria</label>
          <input type="text" v-model="produto.categoria_id" />

          <label>Quantidade</label>
          <input type="number" v-model="produto.quantidade" />

          <label>Código do Produto</label>
          <input type="text" v-model="produto.codigo_produto" />

          <label>Preço</label>
          <input type="number" v-model="produto.preco_produto" />

          <label>Status</label>
          <input type="text" v-model="produto.status" />

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
import { useRoute, useRouter } from 'vue-router';
import axios from 'axios';
import Sidebar from "@/components/Sidebar.vue";

export default {
  components: { Sidebar },
  setup() {
    const router = useRouter();
    const route = useRoute();
    const produtoId = route.params.id; // Obtém o ID do produto da URL
    const produto = ref({
      nome_produto: '',
      categoria_id: '',
      quantidade: '',
      codigo_produto: '',
      preco_produto: '',
      status: '',
    });

    // Função para carregar os dados do produto
    const carregarProduto = async () => {
      try {
        const token = localStorage.getItem('authToken');
        if (!token) {
          console.error('Usuário não autenticado.');
          return;
        }

        const response = await axios.get(
          `http://127.0.0.1:8000/storage_management/produtos/${produtoId}/`,
          {
            headers: { Authorization: `Bearer ${token}` },
          }
        );
        produto.value = response.data; // Preenche os dados do produto
      } catch (error) {
        console.error('Erro ao carregar produto:', error);
        alert('Erro ao carregar produto. Verifique o console para mais detalhes.');
      }
    };

    // Função para editar o produto
    const editarProduto = async () => {
      try {
        const token = localStorage.getItem('authToken');
        if (!token) {
          console.error('Usuário não autenticado.');
          return;
        }

        const response = await axios.put(
          `http://127.0.0.1:8000/storage_management/produtos/${produtoId}/update/`,
          {
            nome_produto: produto.value.nome_produto,
            categoria: produto.value.categoria_id,
            quantidade: produto.value.quantidade,
            codigo_produto: produto.value.codigo_produto,
            preco_produto: produto.value.preco_produto,
            status: produto.value.status,
          },
          {
            headers: { Authorization: `Bearer ${token}` },
          }
        );

        if (response.status === 200) {
          alert('Produto atualizado com sucesso!');
          router.push('/produtos');
        }
      } catch (error) {
        console.error('Erro ao atualizar produto:', error);
        alert('Erro ao atualizar produto. Verifique o console para mais detalhes.');
      }
    };

    // Função para voltar para a lista de produtos
    const voltar = () => {
      router.push('/produtos');
    };

    // Carregar os dados do produto quando a página for carregada
    onMounted(() => {
      carregarProduto();
    });

    return { produto, editarProduto, voltar };
  },
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Afacad&display=swap');

.produto-page {
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
