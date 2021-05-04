import {mount} from '@vue/test-utils';
import Todo from './Todo.vue';
import Todos from './Todos.vue';

test('checking todos list is working', () => {
    const wrapper = mount(Todos, {
        components: {
            Todo,
        },
        props: {
            todos: [
                {'id': 1, 'title': 'buy some milk', 'is_completed': true},
                {'id': 2, 'title': 'this is test', 'is_completed': false}]
        }
    });

    expect(wrapper.findAll('li')).toHaveLength(2)

})
