class StringLogic:

	specialCase = [" ", "-", "_","?","!"]
	vowels = "aeiouyAEIOUY"
	replacements = {
        "à": "a", "â": "a", "ä": "a",
        "é": "e", "è": "e", "ê": "e", "ë": "e",
        "î": "i", "ï": "i",
        "ô": "o", "ö": "o",
        "ù": "u", "û": "u", "ü": "u",
        "ç": "c"
    }

	def size_of_string(self, message : str) -> float:
		size = len(message)
		return str(size)+" caractères"

	def say_hello(self, name : str) -> str:
		if len(name) == 0:
			return "Bonjour !"
		name_tmp = name[0].upper()
		isSpecial = False
		for i in range(1, len(name)):
			if isSpecial and not name[i] in self.specialCase:
				name_tmp+=name[i].upper()
				isSpecial = False
			else:
				name_tmp+=name[i]
				if name[i] in self.specialCase:
					isSpecial = True
		return "Bonjour "+name_tmp
	
	def check_last_caracter(self, message : str) -> bool:
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
	
	def number_of_occurences(self, message : str, caracter : str) -> int:
		count = 0
		for c in message:
			if c == caracter:
				count+=1
		return count

	def transform_to_camel_case(self, message : str) -> str:
		name = ""
		isSpecial = False
		for i in range(len(message)):
			if isSpecial and not message[i] in self.specialCase:
				name+=message[i].upper()
				isSpecial = False
			elif message[i] in self.specialCase:
				isSpecial = True
			else:
				name+=message[i]
		return name
	
	def count_number_of_vowels(self, message : str) -> int:
		count = 0
		for c in message:
			if c in self.vowels:
				count+=1
		return count
	
	def create_upper_in_odd_position(self, message : str) -> str:
		result = ""
		for i in range(len(message)):
			if i%2 == 0:
				result+=message[i].upper()
			else:
				result+=message[i]
		return result
	
	def remove_duplicates(self, message : str) -> str:
		result = ""
		last_char = ""
		for c in message:
			if c != last_char:
				result+=c
				last_char = c
		return result
	
	def create_initials(self, name : str) -> str:
		initials = ""
		isSpecial = True
		for i in range(len(name)):
			if isSpecial and not name[i] in self.specialCase:
				initials+=name[i].upper()
				isSpecial = False
			elif name[i] in self.specialCase:
				isSpecial = True
		return initials
	
	def mask_string(self, message : str, size : int ) -> str:
		if size == 0:
			return ""
		if len(message)<=size:
			return message
		return message[-size:]
	
	def isPalindrome(self, message : str) -> bool:
		message_tmp = ""
		for c in message:
			if c not in self.specialCase and c!=" ":
				letter = c.lower()
				if letter in self.replacements:
					letter = self.replacements[letter]
				message_tmp+=letter
		message_tmp_reverse = message_tmp[::-1]
		return message_tmp == message_tmp_reverse
	
	def longest_sequence(self, message : str) -> int:
		if len(message) == 0:
			return ""
		best_longest = ""
		current_longest = ""
		last_char = ""
		for i in range(0, len(message)):
			if message[i] != last_char:
				if len(current_longest) > len(best_longest):
					best_longest = current_longest
				current_longest=message[i]
				last_char = message[i]
			else:
				current_longest+=message[i]
		if len(current_longest) > len(best_longest):
			best_longest = current_longest
		return best_longest
	
	def truncate(self, content : str, size : int) -> str:
		if size == 0:
			return ""
		if size <= 3:
			return "..."
		if len(content) <= size-3:
			return content
		return content[:size-3]+"..."
	
	def capitalize_words(self, content : str) -> str:
		result = ""
		isSpecial = True
		for i in range(len(content)):
			if isSpecial and not content[i] in self.specialCase:
				result+=content[i].upper()
				isSpecial = False
			elif content[i] in self.specialCase:
				isSpecial = True
				result+=content[i]
			else:
				result+=content[i]
		return result