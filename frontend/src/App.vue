<template>
  <div id="app">
    <h1>{{ title }}</h1>
    <Todos v-bind:todos="todos"/>
    <AddTodo v-on:add-todo="addTodo"/>
  </div>
</template>
<script>
import Todos from './components/Todos';
import AddTodo from './components/AddTodo';
import axios from "axios";
const BASE_URL = process.env.VUE_APP_BASEURL;
const VUE_APP_TITLE = process.env.VUE_APP_TITLE;
export default {
  name: 'app',
  components: {
    Todos,
    AddTodo
  },
  data() {
    return {
      title: VUE_APP_TITLE,
      todos: [],
    }
  },
  created() {
    axios.get(BASE_URL+"api/todo/")
        .then(response => this.todos = response.data);
  },
  methods: {
    addTodo(newTodoObj) {
      axios.post(BASE_URL + 'api/todo/', newTodoObj)
          .then(res => {
              this.todos = [...this.todos, res.data];
          })
          .catch(err => {console.log(err)});
    }
  }
}
</script>
<style>
</style>