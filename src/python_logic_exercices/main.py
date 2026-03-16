from python_logic_exercices.string_logic import StringLogic

string_logic = StringLogic()

def stringLogicTest():
	content = "Bonjour le monde !"
	print(f"Taille de la chaine : '{content}' : {string_logic.sizeOfString(content)}")
	name = "jean-pierre"
	print(f"Dire bonjour à '{name}' : {string_logic.sayHello(name)}")
	print(f"Le message '{content}' se termine-t-il par un point d'exclamation ? : {string_logic.checkLastCaracter(content)}")
	content2 = "Je mange une pomme"
	print(f"inversion des mots de '{content2}' : {string_logic.reverse_words(content2)}")

def main():
	stringLogicTest()

if __name__ == "__main__":
	main()
