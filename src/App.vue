<style src="./assets/css/raw.css" />
<style src="./assets/css/layout.css" />

<template lang="pug">
main(grid id="app" v-if="loaded")
  div(block)
    h3 Input Data
    fieldset
      select(v-model="selected_file")
        option(v-for="file in files" :value="file") {{ file }}
      div Selected file: {{ selected_file }}
    h3 Model Parameters
    fieldset
      label Multiplier
      input(type="number" v-model="multiplier")
    button.action.primary(@click="parse") Start
  div(block)
    h2 Results
    div(v-if="result") {{ result }}

main(id="app" v-else) Loading ...
</template>

<script>
window.API_ROUTE = 'http://127.0.0.1:1101/'
export default {
  name: 'app',
  data() {
    return {
      files: null,
      loaded: null,
      selected_file:null,
      multiplier: 1,
      result: null,
    }
  },
  mounted() {
    axios.get(API_ROUTE + 'listfiles').then(r => {
      this.files = r.data
      this.loaded = true
    })
  },
  methods: {
    parse() {
      if (!this.selected_file) return
      axios.post(API_ROUTE + 'run', {path: this.selected_file, params: {multiplier: this.multiplier}}).then(r => this.result = r.data)
    }
  }
}
</script>

<style>
main {
  height:100vh;
  position:relative;
}

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  padding: 60px 40px;
}
h3 {
  margin-bottom: 10px;
}
fieldset {
  margin-bottom: 20px;
}
</style>
