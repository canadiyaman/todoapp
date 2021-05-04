import {mount} from '@vue/test-utils';
import AddTodo from './AddTodo.vue';

test('create new todo control', () => {
    const wrapper = mount(AddTodo);

    expect(wrapper.find('input[type="text"]').element.value).toBe('')
    wrapper.find('input[type="text"]').setValue('buy some milk')
    expect(wrapper.find('input[type="text"]').element.value).toBe('buy some milk')

    const button = wrapper.get('input[type="submit"]');
    button.trigger('submit');
    expect(wrapper.emitted()).toHaveProperty('submit')

})
