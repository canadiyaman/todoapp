<template>
  <todo-app list-name="ToDo App" />
</template>

<script>
import TodoList from "./components/ToDoApp.vue";
export default {
  name: "App",
  components: {
    TodoList,
  },
};
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>