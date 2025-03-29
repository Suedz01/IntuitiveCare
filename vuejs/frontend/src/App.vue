<template>
  <html>
    <body>
      <div id="app">
        <img src="https://voxcapital.com.br/wp-content/uploads/2022/05/intuitive-care_site-2-2048x519.png" alt="Logo" class="logo">
        <h1>Pesquisa de Procedimentos</h1>

        <div class="search-container">
          <input
            type="text"
            v-model="searchQuery"
            placeholder="Digite o nome ou grupo do procedimento"
            @keyup.enter="searchPeople"
          />
          <button @click="searchPeople">Pesquisar</button>
        </div>

        <div v-if="loading" class="loading">Carregando...</div>

        <div v-if="people.length > 0" class="results">
          <ul>
            <li v-for="(person, index) in people" :key="index">
              <strong>{{ person.PROCEDIMENTO }}</strong>
              <p>Grupo: {{ person.GRUPO }}</p>
            </li>
          </ul>
        </div>

        <div v-if="people.length === 0 && !loading" class="no-results">
          <p>Nenhum resultado encontrado.</p>
        </div>

        <footer class="rodape">
          <p>Feito por Alexandre Sued</p>
        </footer>
      </div>
    </body>
  </html>
</template>

<script>
export default {
  data() {
    return {
      searchQuery: "",
      people: [],
      loading: false,
    };
  },
  methods: {
    async searchPeople() {
      if (!this.searchQuery) return;

      this.loading = true;
      try {
        const response = await fetch(`http://localhost:5000/search?query=${this.searchQuery}`);
        const data = await response.json();
        this.people = data;
      } catch (error) {
        console.error("Erro ao buscar procedimentos:", error);
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
  justify-content: center;
  align-content: center;
  min-height: 92.5vh;
  margin: 0;
  position: relative;
  padding-bottom: 60px; /* Espaço para o footer */
}


body{
  background: #0f0e17;
  margin:0px 0px;
  padding:0px;
}

.logo {
  display: block;
  margin: 0 auto 20px;
  max-width: 20%;
  height: auto;
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
  font-weight: 700;
}

.search-container {
  margin-bottom: 20px;
}

input {
  padding: 10px;
  font-size: 16px;
  width: 300px;
  margin-right: 10px;
  background: #1a1b26;
  border: 1px solid #ff8906;
  color: #fffffe;
  border-radius: 5px;
  font-family: 'Dosis', sans-serif;
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
  font-family: 'Dosis', sans-serif;
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
  font-weight: 700;
}

.results p {
  color: #a7a9be;
  font-family: 'Dosis', sans-serif;
  font-weight: 400;
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
