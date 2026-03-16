from python_logic_exercices.string_logic import StringLogic

string_logic = StringLogic()

def stringLogicTest():
	content = "Bonjour le monde !"
	print(f"Taille de la chaine : '{content}' : {string_logic.size_of_string(content)}")
	name = "jean-pierre"
	print(f"Dire bonjour à '{name}' : {string_logic.say_hello(name)}")
	print(f"Le message '{content}' se termine-t-il par un point d'exclamation ? : {string_logic.check_last_caracter(content)}")
	content2 = "Je mange une pomme"
	print(f"inversion des mots de '{content2}' : {string_logic.reverse_words(content2)}")
	print(f"Nombre d'occurences de 'e' dans '{content}' : {string_logic.number_of_occurences(content, 'e')}")
	print(f"Transformation de '{content2}' en camel case : {string_logic.transform_to_camel_case(content2)}")
	print(f"Nombre de voyelles dans '{content}' : {string_logic.count_number_of_vowels(content)}")
	print(f"Ajout de majuscules aux positions paire du message '{content}' : {string_logic.create_upper_in_odd_position(content)}")
	content3 = "Bonjouuuur !!! J'ai besoiiiin d'aide...."
	print(f"Suppression des duplicats dans le message '{content3}' : {string_logic.remove_duplicates(content3)}")
	print(f"Création des initiales du nom '{name}' : {string_logic.create_initials(name)}")
	card_number = "1234567890123456"
	print(f"Masquage du numéro de carte '{card_number} avec les 4 derniers caractères' : {string_logic.mask_string(card_number, 4)}")
	content4 = "Eh ! ça va la vache ?"
	print(f"Le message '{content4}' est-il un palindrome ? : {string_logic.isPalindrome(content4)}")
	input = "aaabbbbbcccc"
	print(f"Le message '{input}' comprend la plus longue sequence identique : {string_logic.longest_sequence(input)}")
	description = "Ceci est une très longue description d'un produit"
	print(f"Le résumé de la description '{description}' est : {string_logic.truncate(description, 20)}")
	title = "bienvenue sur notre site web"
	print(f"Le titre '{title}' transformé en title avec majuscule est : {string_logic.capitalize_words(title)}")

def main():
	stringLogicTest()

if __name__ == "__main__":
	main()
