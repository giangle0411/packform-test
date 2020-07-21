import OrderTable from '@/components/OrderTable.vue'
import { mount } from '@vue/test-utils'

describe('OrderTable', () => {
  test('Table is rendered with correct header', () => {
    const wrapper = mount(OrderTable)
    expect(wrapper.html()).toContain('<th>Order Name</th>')
  })
})
