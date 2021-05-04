<template>
  <div>
    <h2>My todolist</h2>
    <ul v-bind:key="todo.id" v-for="todo in todos">
      <li>
        <Todo v-bind:todo="todo" />
      </li>
    </ul>
    <hr>
  </div>
</template>
<script>
import Todo from './Todo.vue';

export default {
  name: 'Todos',
  components: {
    Todo,
  },
  props: [
    "todos"
  ]
}
</script>
<style scoped>
</style>