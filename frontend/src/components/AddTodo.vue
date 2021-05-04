<template>
  <div>
    <form @submit="addTodo">
      <input type="text" v-model="title" name="title">
      <input type="submit" value="Add">
    </form>
  </div>
</template>

<script>

export default {
  name: "AddTodo",
  data() {
    return {
      title: ''
    }
  },
  methods: {
    addTodo(e) {
      e.preventDefault();
      const newTodoObj = {
        title: this.title,
        is_completed: false
      }
      this.$emit('add-todo', newTodoObj);
      this.title = '';
    }
  }
}
</script>

<style scoped>

</style>