class StringLogic:

	def sizeOfString(self, message : str) -> float:
		size = len(message)
		return str(size)+" caractères"

	def sayHello(self, name : str) -> str:
		if len(name) == 0:
			return "Bonjour !"
		name_tmp = name[0].upper()
		isSpecial = False
		for i in range(1, len(name)):
			if isSpecial and not name[i] in [" ", "-", "_"]:
				name_tmp+=name[i].upper()
				isSpecial = False
			else:
				name_tmp+=name[i]
				if name[i] in [" ", "-", "_"]:
					isSpecial = True
		return "Bonjour "+name_tmp
	
	def checkLastCaracter(self, message : str) -> bool:
		if len(message) == 0:
			return False
		return message[-1] == "!"

	def reverse_words(self, message : str) -> str:
		words = message.split(" ")
		reverse_message = ""
		for i in range(len(words)-1, -1, -1):
			reverse_message+=words[i]
			if i != 0:
				reverse_message+=" "
		return reverse_message