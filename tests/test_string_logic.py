from python_logic_exercices.string_logic import StringLogic
import pytest

@pytest.fixture
def string_logic():
	return StringLogic()

def test_size_of_string(string_logic):
	assert string_logic.sizeOfString("Hello world!") == "12 caractères"
	assert string_logic.sizeOfString("") == "0 caractères"

def test_say_hello(string_logic):
	assert string_logic.sayHello("jean-pierre") == "Bonjour Jean-Pierre"
	assert string_logic.sayHello("marie claire") == "Bonjour Marie Claire"
	assert string_logic.sayHello("lucie_claire") == "Bonjour Lucie_Claire"
	assert string_logic.sayHello("") == "Bonjour !"

def test_check_last_caracter(string_logic):
	assert string_logic.checkLastCaracter("Hello world!") == True
	assert string_logic.checkLastCaracter("Hello world") == False
	assert string_logic.checkLastCaracter("") == False

def test_reverse_words(string_logic):
	assert string_logic.reverse_words("Hello world") == "world Hello"
	assert string_logic.reverse_words("Python is great") == "great is Python"
	assert string_logic.reverse_words("") == ""