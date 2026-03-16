from python_logic_exercices.array_object_logic import ArrayObjectLogic
import pytest

@pytest.fixture
def array_object_logic():
	return ArrayObjectLogic()

def test_filter_by_property(array_object_logic):
    users = [
    {"id": 1, "name": "Alice", "age": 25, "active": True},
    {"id": 2, "name": "Bob", "age": 30, "active": False},
    {"id": 3, "name": "Charlie", "age": 35, "active": True}
    ]
    assert array_object_logic.filter_by_property(users, 'active', True) == [
    {"id": 1, "name": "Alice", "age": 25, "active": True},
    {"id": 3, "name": "Charlie", "age": 35, "active": True}
    ]
    assert array_object_logic.filter_by_property(users, 'age', 30) == [
    {"id": 2, "name": "Bob", "age": 30, "active": False}
    ]
    assert array_object_logic.filter_by_property(users, 'name', 'Alice') == [
    {"id": 1, "name": "Alice", "age": 25, "active": True}
    ]
    assert array_object_logic.filter_by_property(users, 'name', 'David') == []

def test_group_by(array_object_logic):
    products = [
        {"id": 1, "name": "Laptop", "category": "Electronics", "price": 999},
        {"id": 2, "name": "Smartphone", "category": "Electronics", "price": 699},
        {"id": 3, "name": "T-shirt", "category": "Clothing", "price": 29}
    ]
    prediction = {
        "Electronics": [
            {"id": 1, "name": "Laptop", "category": "Electronics", "price": 999},
            {"id": 2, "name": "Smartphone", "category": "Electronics", "price": 699}
        ],
        "Clothing": [
            {"id": 3, "name": "T-shirt", "category": "Clothing", "price": 29}
        ]
    }
    assert array_object_logic.group_by(products, 'category') == prediction
    assert array_object_logic.group_by(products, 'price') == {
        999: [{"id": 1, "name": "Laptop", "category": "Electronics", "price": 999}],
        699: [{"id": 2, "name": "Smartphone", "category": "Electronics", "price": 699}],
        29: [{"id": 3, "name": "T-shirt", "category": "Clothing", "price": 29}]
    }
    assert array_object_logic.group_by(products, 'genre') == {}

def test_find_intersection(array_object_logic):
    library1 = [
        {"id": 1, "title": "1984", "author": "Orwell", "available": True},
        {"id": 2, "title": "Dune", "author": "Herbert", "available": True}
    ]
    library2 = [
        {"id": 3, "title": "1984", "author": "Orwell", "available": True},
        {"id": 4, "title": "Foundation", "author": "Asimov", "available": True}
    ]
    assert array_object_logic.find_intersection(library1, library2, 'title') == [
        {"id": 1, "title": "1984", "author": "Orwell", "available": True}
    ]
    assert array_object_logic.find_intersection(library1, library2, 'author') == [
        {"id": 1, "title": "1984", "author": "Orwell", "available": True}
    ]
    assert array_object_logic.find_intersection(library1, library2, 'available') == [
        {"id": 1, "title": "1984", "author": "Orwell", "available": True},
        {"id": 2, "title": "Dune", "author": "Herbert", "available": True}
    ]
    assert array_object_logic.find_intersection(library1, library2, 'id') == []
    assert array_object_logic.find_intersection(library1, library2, 'genre') == []

def test_transform_array(array_object_logic):
    employees = [
        {"id": 1, "firstName": "John", "lastName": "Doe", "salary": 50000},
        {"id": 2, "firstName": "Jane", "lastName": "Smith", "salary": 60000}
    ]
    transformer = lambda emp: {
        "id": emp["id"],
        "fullName": f"{emp['firstName']} {emp['lastName']}",
        "annualSalary": emp["salary"] * 12
    }
    assert array_object_logic.transform_array(employees, transformer) == [
        {"id": 1, "fullName": "John Doe", "annualSalary": 600000},
        {"id": 2, "fullName": "Jane Smith", "annualSalary": 720000}
    ]
    assert array_object_logic.transform_array([], transformer) == []
    assert array_object_logic.transform_array(employees, lambda emp: emp["firstName"]) == ["John", "Jane"]
    assert array_object_logic.transform_array(employees, lambda emp: emp["salary"] * 2) == [100000, 120000]

def test_aggregate_data(array_object_logic):
    transactions = [
        {"id": 1, "type": "debit", "amount": 100, "category": "Food"},
        {"id": 2, "type": "debit", "amount": 50, "category": "Food"},
        {"id": 3, "type": "credit", "amount": 75, "category": "Income"}
    ]
    assert array_object_logic.aggregate_data(transactions, 'category', 'amount') == {
        "Food": 150,
        "Income": 75
    }
    assert array_object_logic.aggregate_data(transactions, 'type', 'amount') == {
        "debit": 150,
        "credit": 75
    }
    assert array_object_logic.aggregate_data(transactions, 'id', 'amount') == {
        1: 100,
        2: 50,
        3: 75
    }
    assert array_object_logic.aggregate_data(transactions, 'genre', 'amount') == {}