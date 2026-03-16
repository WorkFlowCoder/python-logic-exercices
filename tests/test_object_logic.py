from python_logic_exercices.object_logic import ObjectLogic
import pytest

@pytest.fixture
def object_logic():
	return ObjectLogic()

def test_get_values(object_logic):
    scores = {"level1": 100,"level2": 85,"level3": 95}
    assert object_logic.get_values(scores) == [100, 85, 95]
    other_object = {"a": 1, "b": 2, "c": 3}
    assert object_logic.get_values(other_object) == [1, 2, 3]

def test_transform_values(object_logic):
    prices_in_euros = {"book": 20,"pen": 5,"notebook": 10}
    expected_result = {"book": 22.0, "pen": 5.5, "notebook": 11.0}
    assert object_logic.transform_values(prices_in_euros, 1.1) == expected_result
    other_object = {"x": 2, "y": 3}
    expected_result = {"x": 4, "y": 6}
    assert object_logic.transform_values(other_object, 2) == expected_result

def test_merge_objects(object_logic):
    store1_sales = { "january": 1000, "february": 1200, "march": 900 }
    store2_sales = { "january": 800, "february": 950, "march": 1100 }
    expected_result = { "january": 1800, "february": 2150, "march": 2000 }
    assert object_logic.merge_objects(store1_sales, store2_sales) == expected_result
    object1 = {"a": 1, "b": 2}
    object2 = {"b": 3, "c": 4}
    expected_result = {"a": 1, "b": 5, "c": 4}
    assert object_logic.merge_objects(object1, object2) == expected_result

def test_filter_object(object_logic):
    inventory = {"laptop": 0,"smartphone": 5,"tablet": 0,"headphones": 8}
    expected_result = {"laptop": 0, "tablet": 0}
    assert object_logic.filter_object(inventory, 0) == expected_result
    other_object = {"x": 1, "y": 2, "z": 3}
    expected_result = {"x": 1, "y": 2}
    assert object_logic.filter_object(other_object, 2) == expected_result

def test_flat_to_nested(object_logic):
    flat_config = {
        'app.name': 'MyApp',
        'app.version': '1.0.0',
        'database.host': 'localhost',
        'database.port': 5432
    }
    expected_result = {
        'app': {
            'name': 'MyApp',
            'version': '1.0.0'
        },
        'database': {
            'host': 'localhost',
            'port': 5432
        }
    }
    assert object_logic.flat_to_nested(flat_config) == expected_result
    other_flat_config = {
        'user.name': 'Alice',
        'user.age': 30,
        'settings.theme': 'dark'
    }
    expected_result = {
        'user': {
            'name': 'Alice',
            'age': 30
        },
        'settings': {
            'theme': 'dark'
        }
    }
    assert object_logic.flat_to_nested(other_flat_config) == expected_result

def test_find_keys_by_value(object_logic):
    product_stock = {"laptop": 0,"mouse": 5,"keyboard": 0,"monitor": 3}
    expected_result = ["laptop", "keyboard"]
    assert object_logic.find_keys_by_value(product_stock, 0) == expected_result
    other_object = {"a": 1, "b": 2, "c": 1}
    expected_result = ["a", "c"]
    assert object_logic.find_keys_by_value(other_object, 1) == expected_result

def test_create_object_from_arrays(object_logic):
    player_names = ["Alice", "Bob", "Charlie"]
    scores = [100, 85, 90]
    expected_result = {"Alice": 100, "Bob": 85, "Charlie": 90}
    assert object_logic.create_object_from_arrays(player_names, scores) == expected_result
    other_list_a = ["x", "y", "z"]
    other_list_b = [1, 2, 3]
    expected_result = {"x": 1, "y": 2, "z": 3}
    assert object_logic.create_object_from_arrays(other_list_a, other_list_b) == expected_result
    with pytest.raises(ValueError):
        object_logic.create_object_from_arrays(["a", "b"], [1])
    
def test_count_values(object_logic):
    order_statuses = {"order1": "pending","order2": "delivered","order3": "pending",
    "order4": "cancelled","order5": "pending"}
    expected_result = {"pending": 3, "delivered": 1, "cancelled": 1}
    assert object_logic.count_values(order_statuses) == expected_result
    other_object = {"a": 1, "b": 2, "c": 1, "d": 3}
    expected_result = {1: 2, 2: 1, 3: 1}
    assert object_logic.count_values(other_object) == expected_result

def test_extract_properties(object_logic):
    user_profile = {
        "name": "Jean Martin",
        "email": "jean@email.com",
        "password": "secret123",
        "age": 35,
        "address": "123 rue Principal"
    }
    public_info = ["name", "age"]
    expected_result = {"name": "Jean Martin", "age": 35}
    assert object_logic.extract_properties(user_profile, public_info) == expected_result

def test_sort_object_by_value(object_logic):
    player_scores = {
        "Alice": 85,
        "Bob": 92,
        "Charlie": 78,
        "David": 95
    }
    expected_result = {"David": 95, "Bob": 92, "Alice": 85, "Charlie": 78}
    assert object_logic.sort_object_by_value(player_scores) == expected_result

def test_find_max_value(object_logic):
    game_scores = {
        "level1": 850,
        "level2": 920,
        "level3": 880,
        "level4": 1020
    }
    expected_result = 1020
    assert object_logic.find_max_value(game_scores) == expected_result

def test_create_object_from_pairs(object_logic):
    product_pairs = [
        ["pommes", 2.5],
        ["bananes", 1.8],
        ["oranges", 2.2]
    ]
    expected_result = {"pommes": 2.5, "bananes": 1.8, "oranges": 2.2}
    assert object_logic.create_object_from_pairs(product_pairs) == expected_result
    other_pairs = [
        ["x", 1],
        ["y", 2],
        ["z", 3]
    ]
    expected_result = {"x": 1, "y": 2, "z": 3}
    assert object_logic.create_object_from_pairs(other_pairs) == expected_result

def test_find_value_in_object(object_logic):
    config = {
        "app": {
            "name": "MonApp",
            "settings": {
                "theme": "dark",
                "notifications": {
                    "email": True,
                    "push": False
                }
            }
        }
    }
    assert object_logic.find_value_in_object(config, 'dark') == True
    assert object_logic.find_value_in_object(config, 'MonApp') == True
    assert object_logic.find_value_in_object(config, 'light') == False
    assert object_logic.find_value_in_object(config, True) == True
    assert object_logic.find_value_in_object(config, False) == True

def test_group_by_property(object_logic):
    students = [
        { "name": "Alice", "level": "Débutant" },
        { "name": "Bob", "level": "Intermédiaire" },
        { "name": "Charlie", "level": "Débutant" },
        { "name": "David", "level": "Avancé" }
    ]
    expected_result = {
        "Débutant": [
            { "name": "Alice", "level": "Débutant" },
            { "name": "Charlie", "level": "Débutant" }
        ],
        "Intermédiaire": [
            { "name": "Bob", "level": "Intermédiaire" }
        ],
        "Avancé": [
            { "name": "David", "level": "Avancé" }
        ]
    }
    assert object_logic.group_by_property(students, 'level') == expected_result

def test_validate_object(object_logic):
    user_schema = {
        "name": "string",
        "age": "number",
        "email": "string"
    }
    user_input = {
        "name": "Marie",
        "age": 25,
        "email": "marie@email.com"
    }
    assert object_logic.validate_object(user_schema, user_input) == True

def test_compare_differences(object_logic):
    old_profile = {
        "name": "Jean Dupont",
        "email": "jean@email.com",
        "age": 30,
        "gender": "female"
    }
    new_profile = {
        "name": "Jean Dupont",
        "email": "jean.dupont@email.com",
        "age": 31,
        "phone": "0123456789"
    }
    expected_result = {
        "email": {"type": "modified", "old": "jean@email.com", "new": "jean.dupont@email.com"},
        "age": {"type": "modified", "old": 30, "new": 31},
        "phone": {"type": "added", "new": "0123456789"},
        "gender": {"type": "deleted", "old": "female"}
    }
    assert object_logic.compare_differences(old_profile, new_profile) == expected_result

def test_object_to_url_params(object_logic):
    search_params = {
        "query": "ordinateur portable",
        "maxPrice": 1000,
        "brand": "Dell",
        "inStock": True
    }
    expected_result = "query=ordinateur%20portable&maxPrice=1000&brand=Dell&inStock=True"
    assert object_logic.object_to_url_params(search_params) == expected_result

def test_get_object_stats(object_logic):
    monthly_revenues = {
        "january": 1000,
        "february": 1200,
        "march": 900,
        "april": 1500
    }
    expected_result = {
        "basic": {
            "min": 900,
            "max": 1500,
            "average": 1150,
            "total": 4600
        },
        "advanced": {
            "median": 1100,
            "variance": 52500,
            "standardDeviation": 229.13
        }
        }
    assert object_logic.get_object_stats(monthly_revenues) == expected_result