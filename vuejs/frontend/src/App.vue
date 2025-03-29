<template>
  <div id="app">
    <img src="https://voxcapital.com.br/wp-content/uploads/2022/05/intuitive-care_site-2-2048x519.png" alt="Logo" class="logo">
    <h1>Pesquisa de Operadoras</h1>

    <div class="search-container">
      <input
        type="text"
        v-model="searchQuery"
        placeholder="Digite o nome ou CNPJ da operadora"
        @keyup.enter="searchOperators"
      />
      <button @click="searchOperators">Pesquisar</button>
    </div>

    <div v-if="loading" class="loading">Carregando...</div>

    <div v-if="operators.length > 0" class="results">
      <ul>
        <li v-for="(operator, index) in operators" :key="index">
          <strong>{{ operator.Razao_Social }}</strong>
          <p>Nome Fantasia: {{ operator.Nome_Fantasia || 'N/A' }}</p>
          <p>CNPJ: {{ operator.CNPJ }}</p>
          <p>Modalidade: {{ operator.Modalidade }}</p>
        </li>
      </ul>
    </div>

    <div v-if="operators.length === 0 && !loading" class="no-results">
      <p>Nenhum resultado encontrado.</p>
    </div>

    <footer class="rodape">
      <p>Feito por Alexandre Sued</p>
    </footer>
  </div>
</template>

<script>
export default {
  data() {
    return {
      searchQuery: "",
      operators: [],
      loading: false,
    };
  },
  methods: {
    async searchOperators() {
      if (!this.searchQuery) return;

      this.loading = true;
      try {
        const response = await fetch(`http://localhost:5000/search?query=${this.searchQuery}`);
        const data = await response.json();
        this.operators = data;
      } catch (error) {
        console.error("Erro ao buscar operadoras:", error);
      } finally {
        this.loading = false;
      }
    },
  },
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Kanit:wght@700&family=Dosis:wght@400;600&display=swap');

#app {
  font-family: 'Dosis', sans-serif;
  text-align: center;
  background: #0f0e17;
  color: #fffffe;
  padding: 20px;
  min-height: 92.5vh;
  position: relative;
  padding-bottom: 60px;
}

body {
  background: #0f0e17;
  margin: 0;
  padding: 0;
}

.logo {
  display: block;
  margin: 0 auto 20px;
  max-width: 20%;
}

.rodape {
  color: #e57805;
  background: #1a1b26;
  text-align: center;
  position: fixed;
  bottom: 0;
  left: 0;
  padding: 10px;
  width: 100%;
}

h1 {
  font-family: 'Kanit', sans-serif;
  color: #fffffe;
}

.search-container {
  margin-bottom: 20px;
}

input {
  padding: 10px;
  font-size: 16px;
  width: 300px;
  background: #1a1b26;
  border: 1px solid #ff8906;
  color: #fffffe;
  border-radius: 5px;
}

button {
  padding: 10px 20px;
  font-size: 16px;
  background: #ff8906;
  color: #fffffe;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: 0.3s;
}

button:hover {
  background: #e57805;
}

.results ul {
  list-style-type: none;
  padding: 0;
}

.results li {
  margin: 20px 0;
  padding: 10px;
  border: 1px solid #ff8906;
  background: #1a1b26;
  border-radius: 5px;
}

.results strong {
  color: #fffffe;
  font-family: 'Kanit', sans-serif;
}

.results p {
  color: #a7a9be;
}

.loading {
  font-size: 18px;
  color: #ff8906;
}

.no-results {
  font-size: 18px;
  color: #a7a9be;
}
</style>
