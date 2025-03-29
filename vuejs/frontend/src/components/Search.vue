<template>
  <div>
    <h1>Busca de Procedimentos</h1>
    <input v-model="query" @input="searchPeople" placeholder="Buscar Procedimento ou Grupo" />
    
    <div v-if="loading">Carregando...</div>
    
    <ul v-if="results.length > 0">
      <li v-for="(item, index) in results" :key="index">
        {{ item.PROCEDIMENTO }} - {{ item.GRUPO }}
      </li>
    </ul>
    
    <div v-if="results.length === 0 && !loading">Nenhum resultado encontrado</div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      query: '',
      results: [],
      loading: false,
    };
  },
  methods: {
    searchPeople() {
      if (this.query.trim() === '') {
        this.results = [];
        return;
      }

      this.loading = true;

      axios.get(`http://localhost:5000/search?query=${this.query}`)
        .then(response => {
          this.results = response.data;
        })
        .catch(error => {
          console.error('Erro ao buscar procedimentos:', error);
        })
        .finally(() => {
          this.loading = false;
        });
    },
  },
};
</script>

<style scoped>
input {
  padding: 10px;
  font-size: 16px;
  margin-bottom: 20px;
}

ul {
  list-style: none;
  padding: 0;
}

li {
  margin-bottom: 10px;
}
</style>
