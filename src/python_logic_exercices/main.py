from python_logic_exercices.string_logic import StringLogic
from python_logic_exercices.object_logic import ObjectLogic
from python_logic_exercices.array_object_logic import ArrayObjectLogic

string_logic = StringLogic()
object_logic = ObjectLogic()
array_object_logic = ArrayObjectLogic()


def string_logic_test():
    # Tests sur les chaînes de caractères
    content = "Bonjour le monde !"
    print(f"Taille de la chaîne '{content}': {string_logic.size_of_string(content)}")

    name = "jean-pierre"
    print(f"Dire bonjour à '{name}': {string_logic.say_hello(name)}")
    print(f"Le message '{content}' se termine-t-il par un point d'exclamation? : {string_logic.check_last_caracter(content)}")

    content2 = "Je mange une pomme"
    print(f"Inversion des mots de '{content2}': {string_logic.reverse_words(content2)}")
    print(f"Nombre d'occurrences de 'e' dans '{content}': {string_logic.number_of_occurences(content, 'e')}")
    print(f"Transformation de '{content2}' en camel case: {string_logic.transform_to_camel_case(content2)}")
    print(f"Nombre de voyelles dans '{content}': {string_logic.count_number_of_vowels(content)}")
    print(f"Ajout de majuscules aux positions paires du message '{content}': {string_logic.create_upper_in_odd_position(content)}")

    content3 = "Bonjouuuur !!! J'ai besoiiiin d'aide...."
    print(f"Suppression des duplicats dans le message '{content3}': {string_logic.remove_duplicates(content3)}")
    print(f"Création des initiales du nom '{name}': {string_logic.create_initials(name)}")

    card_number = "1234567890123456"
    print(f"Masquage du numéro de carte '{card_number}' avec les 4 derniers caractères: {string_logic.mask_string(card_number, 4)}")

    content4 = "Eh ! ça va la vache ?"
    print(f"Le message '{content4}' est-il un palindrome? : {string_logic.isPalindrome(content4)}")

    input_str = "aaabbbbbcccc"
    print(f"Le message '{input_str}' comprend la plus longue séquence identique: {string_logic.longest_sequence(input_str)}")

    description = "Ceci est une très longue description d'un produit"
    print(f"Résumé de la description '{description}': {string_logic.truncate(description, 20)}")

    title = "bienvenue sur notre site web"
    print(f"Le titre '{title}' transformé en title avec majuscules: {string_logic.capitalize_words(title)}")


def object_logic_test_part_1():
    # Tests sur les objets / dictionnaires
    scores = {"level1": 100, "level2": 85, "level3": 95}
    print(f"Les valeurs de l'objet {scores}: {object_logic.get_values(scores)}")

    prices_in_euros = {"book": 20, "pen": 5, "notebook": 10}
    print(f"Transformation des prix en dollars avec un taux de change de 1.1: {object_logic.transform_values(prices_in_euros, 1.1)}")

    store1_sales = {"january": 1000, "february": 1200, "march": 900}
    store2_sales = {"january": 800, "february": 950, "march": 1100}
    print(f"Fusion des objets: {object_logic.merge_objects(store1_sales, store2_sales)}")

    inventory = {"laptop": 0, "smartphone": 5, "tablet": 0, "headphones": 8}
    print(f"Filtrage des produits en rupture de stock: {object_logic.filter_object(inventory, 0)}")

    flat_config = {
        'app.name': 'MyApp',
        'app.version': '1.0.0',
        'database.host': 'localhost',
        'database.port': 5432
    }
    print(f"Transformation du config plat en config imbriquée: {object_logic.flat_to_nested(flat_config)}")

    product_stock = {"laptop": 0, "mouse": 5, "keyboard": 0, "monitor": 3}
    print(f"Recherche des clés ayant une valeur de 0: {object_logic.find_keys_by_value(product_stock, 0)}")

    player_names = ["Alice", "Bob", "Charlie"]
    scores = [100, 85, 90]
    print(f"Création d'un objet à partir des deux listes: {object_logic.create_object_from_arrays(player_names, scores)}")

    order_statuses = {
        "order1": "pending",
        "order2": "delivered",
        "order3": "pending",
        "order4": "cancelled",
        "order5": "pending"
    }
    print(f"Comptage du nombre d'occurrences de chaque statut: {object_logic.count_values(order_statuses)}")


def object_logic_test_part_2():
    # Tests sur les objets / dictionnaires
    user_profile = {
        "name": "Jean Martin",
        "email": "jean@email.com",
        "password": "secret123",
        "age": 35,
        "address": "123 rue Principal"
    }
    public_info = ["name", "age"]
    print(f"Création d'un profil public: {object_logic.extract_properties(user_profile, public_info)}")

    player_scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 95}
    print(f"Joueur ayant le score le plus élevé: {object_logic.sort_object_by_value(player_scores)}")

    game_scores = {"level1": 850, "level2": 920, "level3": 880, "level4": 1020}
    print(f"Tri des niveaux de jeu par score décroissant: {object_logic.find_max_value(game_scores)}")

    product_pairs = [["pommes", 2.5], ["bananes", 1.8], ["oranges", 2.2]]
    print(f"Création d'un objet à partir de paires produit-prix: {object_logic.create_object_from_pairs(product_pairs)}")

    config = {
        "app": {
            "name": "MonApp",
            "settings": {
                "theme": "dark",
                "notifications": {"email": True, "push": False}
            }
        }
    }
    print(f"Recherche de 'dark' dans une structure: {object_logic.find_value_in_object(config, 'dark')}")

def object_logic_test_part_3():
    # Tests sur les objets / dictionnaires
    students = [
        {"name": "Alice", "level": "Débutant"},
        {"name": "Bob", "level": "Intermédiaire"},
        {"name": "Charlie", "level": "Débutant"},
        {"name": "David", "level": "Avancé"}
    ]
    print(f"Regroupement des étudiants par niveau: {object_logic.group_by_property(students, 'level')}")

    user_schema = {"name": "string", "age": "number", "email": "string"}
    user_input = {"name": "Marie", "age": 25, "email": "marie@email.com"}
    print(f"Validation de l'objet utilisateur: {object_logic.validate_object(user_schema, user_input)}")

    old_profile = {"name": "Jean Dupont", "email": "jean@email.com", "age": 30}
    new_profile = {"name": "Jean Dupont", "email": "jean.dupont@email.com", "age": 31, "phone": "0123456789"}
    print(f"Comparaison des différences entre deux profils: {object_logic.compare_differences(old_profile, new_profile)}")

    search_params = {"query": "ordinateur portable", "maxPrice": 1000, "brand": "Dell", "inStock": True}
    print(f"Transformation en paramètres d'URL: {object_logic.object_to_url_params(search_params)}")

    monthly_revenues = {"january": 1000, "february": 1200, "march": 900, "april": 1500}
    print(f"Résumé des revenus sous forme de statistiques: {object_logic.get_object_stats(monthly_revenues)}")

def array_logic():
	users = [
    {"id": 1, "name": "Alice", "age": 25, "active": True},
    {"id": 2, "name": "Bob", "age": 30, "active": False},
    {"id": 3, "name": "Charlie", "age": 35, "active": True}
	]
	print(f"Filtrage des utilisateurs actifs: {array_object_logic.filter_by_property(users, 'active', True)}")

	products = [
    {"id": 1, "name": "Laptop", "category": "Electronics", "price": 999},
    {"id": 2, "name": "Smartphone", "category": "Electronics", "price": 699},
    {"id": 3, "name": "T-shirt", "category": "Clothing", "price": 29}
	]
	print(f"Regroupement des produits par catégorie: {array_object_logic.group_by(products, 'category')}")

	library1 = [
    {"id": 1, "title": "1984", "author": "Orwell", "available": True},
    {"id": 2, "title": "Dune", "author": "Herbert", "available": False}
	]
	library2 = [
    {"id": 3, "title": "1984", "author": "Orwell", "available": True},
    {"id": 4, "title": "Foundation", "author": "Asimov", "available": True}
	]
	print(f"Intersection des deux bibliothèques par titre: {array_object_logic.find_intersection(library1, library2, 'title')}")

	employees = [
    {"id": 1, "firstName": "John", "lastName": "Doe", "salary": 50000},
    {"id": 2, "firstName": "Jane", "lastName": "Smith", "salary": 60000}
	]
	transformer = lambda emp: {
		"id": emp["id"],
		"fullName": f"{emp['firstName']} {emp['lastName']}",
		"annualSalary": emp["salary"] * 12
	}
	print(f"Transformation des employés avec un transformer personnalisé: {array_object_logic.transform_array(employees, transformer)}")
	transactions = [
		{"id": 1, "type": "debit", "amount": 100, "category": "Food"},
		{"id": 2, "type": "debit", "amount": 50, "category": "Food"},
		{"id": 3, "type": "credit", "amount": 75, "category": "Income"}
	]
	print(f"Agrégation des montants par catégorie: {array_object_logic.aggregate_data(transactions, 'category', 'amount')}")


def main():
	print(" -- Tests sur les chaînes de caractères -- ")
	string_logic_test()
	#print(" -- Tests sur les objets / dictionnaires -- ")
    #object_logic_test_part_1()
    #object_logic_test_part_2()
	#object_logic_test_part_3()
	#print(" -- Tests sur les listes d'objets -- ")
	#array_logic()

if __name__ == "__main__":
    main()