<template>
  <div id="app">
    <Todos v-bind:todos="todos"/>
    <AddTodo v-on:add-todo="addTodo"/>
  </div>
</template>
<script>
import Todos from './components/Todos';
import AddTodo from './components/AddTodo';
import axios from "axios";

export default {
  name: 'app',
  components: {
    Todos,
    AddTodo
  },
  data() {
    return {
      todos: [],
    }
  },
  created() {
    axios.get("http://0.0.0.0:8000/api/todo/")
        .then(response => this.todos = response.data);
  },
  methods: {
    addTodo(newTodoObj) {
      axios.post('http://0.0.0.0:8000/api/todo/', newTodoObj)
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