from python_logic_exercices.string_logic import StringLogic
import pytest

@pytest.fixture
def string_logic():
	return StringLogic()

def test_size_of_string(string_logic):
	assert string_logic.size_of_string("Hello world!") == "12 caractères"
	assert string_logic.size_of_string("") == "0 caractères"

def test_say_hello(string_logic):
	assert string_logic.say_hello("jean-pierre") == "Bonjour Jean-Pierre"
	assert string_logic.say_hello("marie claire") == "Bonjour Marie Claire"
	assert string_logic.say_hello("lucie_claire") == "Bonjour Lucie_Claire"
	assert string_logic.say_hello("") == "Bonjour !"

def test_check_last_caracter(string_logic):
	assert string_logic.check_last_caracter("Hello world!") == True
	assert string_logic.check_last_caracter("Hello world") == False
	assert string_logic.check_last_caracter("") == False

def test_reverse_words(string_logic):
	assert string_logic.reverse_words("Hello world") == "world Hello"
	assert string_logic.reverse_words("Python is great") == "great is Python"
	assert string_logic.reverse_words("") == ""

def test_number_of_occurences(string_logic):
	assert string_logic.number_of_occurences("Hello world", "o") == 2
	assert string_logic.number_of_occurences("Python is great", "y") == 1
	assert string_logic.number_of_occurences("Hello world", "z") == 0
	assert string_logic.number_of_occurences("", "a") == 0

def test_transform_to_camel_case(string_logic):
	assert string_logic.transform_to_camel_case("hello world") == "helloWorld"
	assert string_logic.transform_to_camel_case("python_is_great") == "pythonIsGreat"
	assert string_logic.transform_to_camel_case("marie-claire") == "marieClaire"
	assert string_logic.transform_to_camel_case("") == ""

def test_count_number_of_vowels(string_logic):
	assert string_logic.count_number_of_vowels("Hello world") == 3
	assert string_logic.count_number_of_vowels("Python is great") == 5
	assert string_logic.count_number_of_vowels("bcdfghjklmnpqrstvwxz") == 0
	assert string_logic.count_number_of_vowels("") == 0
	assert string_logic.count_number_of_vowels("AAA") == 3

def test_create_upper_in_odd_position(string_logic):
	assert string_logic.create_upper_in_odd_position("Hello world") == "HeLlO WoRlD"
	assert string_logic.create_upper_in_odd_position("Python is great") == "PyThOn iS GrEaT"
	assert string_logic.create_upper_in_odd_position("") == ""
	assert string_logic.create_upper_in_odd_position("abcde") == "AbCdE"

def test_create_initials(string_logic):
	assert string_logic.create_initials("Jean-Pierre") == "JP"
	assert string_logic.create_initials("Marie Claire") == "MC"
	assert string_logic.create_initials("Lucie_Claire") == "LC"
	assert string_logic.create_initials("") == ""

def test_mask_string(string_logic):
	assert string_logic.mask_string("1234567890123456", 4) == "3456"
	assert string_logic.mask_string("1234567890123456", 0) == ""
	assert string_logic.mask_string("1234567890123456", 16) == "1234567890123456"
	assert string_logic.mask_string("123", 4) == "123"
	assert string_logic.mask_string("", 4) == ""

def test_isPalindrome(string_logic):
	assert string_logic.isPalindrome("Eh ! ça va la vache ?") == True
	assert string_logic.isPalindrome("Kayak") == True
	assert string_logic.isPalindrome("Hello world") == False
	assert string_logic.isPalindrome("") == True

def test_longest_sequence(string_logic):
	assert string_logic.longest_sequence("aaabbbbbcccc") == "bbbbb"
	assert string_logic.longest_sequence("abcde") == "a"
	assert string_logic.longest_sequence("aaaaa") == "aaaaa"
	assert string_logic.longest_sequence("") == ""

def test_truncate(string_logic):
	assert string_logic.truncate("Ceci est une très longue description d'un produit", 20) == "Ceci est une très..."
	assert string_logic.truncate("Short description", 20) == "Short description"
	assert string_logic.truncate("", 20) == ""
	assert string_logic.truncate("Exact length", 12) == "Exact len..."
	assert string_logic.truncate("Exact length", 3) == "..."

def test_capitalize_words(string_logic):
	assert string_logic.capitalize_words("bienvenue sur notre site web") == "Bienvenue Sur Notre Site Web"
	assert string_logic.capitalize_words("python is great") == "Python Is Great"
	assert string_logic.capitalize_words("") == ""
	assert string_logic.capitalize_words("a b c d e") == "A B C D E"
	assert string_logic.capitalize_words("avec") == "Avec"