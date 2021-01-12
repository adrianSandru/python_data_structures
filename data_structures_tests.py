from SingleLinkedList import *

def test_push():
    cars_menu = SingleLinkedList()
    cars_menu.push("Dacia")
    assert(cars_menu.get_number_of_items() == 1)
    cars_menu.push("Renault")
    cars_menu.push("Audi")

    assert(cars_menu.get_number_of_items() == 3)
    print("test_push has passed!")

def test_get_first_element():
    cars_menu = SingleLinkedList()
    cars_menu.push("Dacia")
    cars_menu.push("Renault")
    cars_menu.push("Audi")

    first_element = cars_menu.get_first_item()
    assert first_element.value == "Dacia"

    print("test_get_first_element has passed!")

def test_get_last_element():
    cars_menu = SingleLinkedList()
    cars_menu.push("Dacia")
    cars_menu.push("Renault")
    cars_menu.push("Audi")

    first_element = cars_menu.get_last_item()
    assert first_element.value == "Audi"

    print("test_get_last_element has passed!")

def test_remove_first_item():
    cars_menu = SingleLinkedList()
    cars_menu.push("Dacia")
    cars_menu.push("Renault")
    cars_menu.push("Audi")
    cars_menu.push("Jeep")

    cars_menu.remove_first_item()
    assert cars_menu. get_number_of_items() == 3

    cars_menu.remove_first_item()
    cars_menu.remove_first_item()
    cars_menu.remove_first_item()
    assert cars_menu. get_number_of_items() == 0

    print("test_remove_first_item has passed!")

def test_get_node_at_index():
    cars_menu = SingleLinkedList()
    cars_menu.push("Dacia")
    cars_menu.push("Renault")
    cars_menu.push("Audi")
    cars_menu.push("Jeep")

    node = cars_menu.get_node_at_index(1)
    assert node.value == "Dacia"
    print("test_get_node_at_index has passed!")

def test_remove_last_item():
    cars_menu = SingleLinkedList()
    cars_menu.push("Dacia")
    cars_menu.push("Renault")
    cars_menu.push("Audi")
    cars_menu.push("Jeep")

    print("Current items:")
    cars_menu.traverse_and_print_items()

    cars_menu.remove_last_item()
    assert cars_menu. get_number_of_items() == 3

    print("Current items after removing 1 element from the end:")
    cars_menu.traverse_and_print_items()

    cars_menu.remove_last_item()
    cars_menu.remove_last_item()
    cars_menu.remove_last_item()

    print("Current items after removing 3 element from the end:")
    cars_menu.traverse_and_print_items()

    assert cars_menu. get_number_of_items() == 0
    print("test_remove_last_item has passed!")

test_push()
test_get_first_element()
test_get_last_element()
test_get_node_at_index()
test_remove_first_item()
test_remove_last_item()
