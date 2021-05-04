import {mount} from '@vue/test-utils';
import Todo from './Todo.vue';

test('Is title in the p tag control', () => {
    const wrapper = mount(Todo, {
        props: {
            todo: {'title': 'buy some milk'}
        }
    })
    expect(wrapper.find('p').text()).toContain('buy some milk');
})
