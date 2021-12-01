from LinkedList import*


def print_menu():
    print('Menu:')
    print('1 - Fill list with keyboard')
    print('2 - Fill list with randoms from interval [a,b]')
    print('3 - Add element on position k')
    print('4 - Delete element from position k')
    print('5 - Write all elements with an even indexes, and then with an odd indexes')
    print('6 - Print list')
    print('7 - Exit')


print_menu()
choice = int(input('Choice:'))
lst = List()
while choice != 7:
    if choice == 1:
        number = input_and_check_size()
        lst.fill_list_with_keyboard(number)
        print_menu()
        choice = int(input('Choice:'))

    if choice == 2:
        number = input_and_check_size()
        left = input_check_list_element_or_interval_limit()
        right = input_check_list_element_or_interval_limit()
        if left > right:
            temp = left
            left = right
            right = temp
        lst.fill_list_with_randoms(number, left, right)
        print_menu()
        choice = int(input('Choice:'))

    if choice == 3:
        value = input_check_list_element_or_interval_limit()
        index = input_and_check_index(lst.get_size())
        lst.add_new_node(value, index)
        print_menu()
        choice = int(input('Choice:'))

    if choice == 4:
        if lst.get_head() is None:
            print("You can't delete node, because your list is empty")
        else:
            index = input_and_check_index(lst.get_size())
            lst.delete_node(index)
        print_menu()
        choice = int(input('Choice:'))

    if choice == 5:
        lst.even_and_odd_indexes()
        print_menu()
        choice = int(input('Choice:'))

    if choice == 6:
        lst.print_list()
        print_menu()
        choice = int(input('Choice:'))

    if 7 < choice < 1:
        print('There is no such choice')
        choice = int(input('Choice:'))
