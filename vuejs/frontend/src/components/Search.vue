<template>
  <div>
    <h1>Busca de Operadoras</h1>
    <input v-model="query" @input="searchOperators" placeholder="Buscar por Razão Social ou Nome Fantasia" />
    
    <div v-if="loading">Carregando...</div>
    
    <ul v-if="results.length > 0">
      <li v-for="(item, index) in results" :key="index">
        {{ item.Razao_Social }} - {{ item.Nome_Fantasia || 'Sem Nome Fantasia' }}
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
    searchOperators() {
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
          console.error('Erro ao buscar operadoras:', error);
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
