from SingleLinkedList import *

def test_push():
    cars_menu = SingleLinkedList()
    cars_menu.push("Dacia")
    assert(cars_menu.count == 1)
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

def test_get_node_at_index():
    cars_menu = SingleLinkedList()
    cars_menu.push("Dacia")
    cars_menu.push("Renault")
    cars_menu.push("Audi")
    cars_menu.push("Jeep")

    node = cars_menu.get_node_at_index(1)
    assert node.value == "Dacia"
    print("test_get_node_at_index has passed!")

test_push()
test_get_first_element()
test_get_last_element()
test_get_node_at_index()
