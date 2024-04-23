To implement LEX program of odd and even no.
import re

def lexer(input_str):
    if re.match(r'\d+', input_str):
        num = int(input_str)
        if num % 2 == 0:
            return "Even"
        else:
            return "Odd"
    else:
        return "Not a number"
    
input_str = input("Enter a number: ")
result = lexer(input_str)
print(result)


To implement LEX program of largest word.
import re

def largest_word(text):
    words = re.findall(r'\b\w+\b', text)
    return max(words, key=len)

text = "This is a sample sentence with several words of different lengths"
print("The largest word is:", largest_word(text))


To implement LEX program of prime no.
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

number = int(input("Enter a number: "))
if is_prime(number):
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")


To implement LEX program of vowels
import re

def lexer(input_string):
    vowels = re.findall('[aeiouAEIOU]', input_string)
    return vowels

input_string = input("Enter a string: ")
print("Vowels in the string:", lexer(input_string))


To implement LEX program of Lex identifier and keyword
import re

def lexer(input_string):
    keywords = ['if', 'else', 'while', 'for', 'return', 'int', 'float', 'bool']  
    identifier_regex = r'^[a-zA-Z_]\w*$'  
    
    tokens = []  
    
    for token in input_string.split():
        if token in keywords:
            tokens.append((token, 'Keyword'))
        elif re.match(identifier_regex, token):
            tokens.append((token, 'Identifier'))
        else:
            tokens.append((token, 'Invalid'))

    return tokens
input_string = "if x == 5 else while y < 10 for z in range(5) return"
tokens = lexer(input_string)
for token in tokens:
    print(token)


To Implement LEX program of operator
import re

def lex(input_string):
    tokens = []
    operators = r'[+\-*/=]'
    matches = re.findall(operators, input_string)
    for match in matches:
        tokens.append((match, "OPERATOR"))
    return tokens

input_string = input("Enter a string: ")
print(lex(input_string))


To implement Lexical Analyzer programs (identifier, keywords)(JAVA/C/C++/Python/R-lang /Lex).
import re

def lexer(input_string):
    keywords = {'if', 'else', 'while', 'for', 'int', 'float', 'return'}
    tokens = re.findall(r'\b\w+\b', input_string)
    for token in tokens:
        if token in keywords:
            print(f'{token}: keyword')
        else:
            print(f'{token}: identifier')

# Example usage:
input_string = input("Enter code: ")
lexer(input_string)


To implement Lexical Analyzer programs (operators) (JAVA/C/C++/Python/R-lang/Lex).
import re

def lexer(input_string):
    operators = ['+', '-', '*', '/', '=', '<', '>', '==', '!=', '<=', '>=', '&&', '||', '!', '&', '|']
    tokens = re.findall(r'[-+*/=<>!&|]+', input_string)
    for token in tokens:
        if token in operators:
            print(f'{token}: operator')

# Example usage:
input_string = input("Enter code: ")
lexer(input_string)


Write a program to remove left recursion by direct method for a given set of production rules (JAVA/C/C++/Python/R-lang /Lex).
def remove_left_recursion(productions):
    new_productions = {}
    non_terminals = list(productions.keys())

    for A in non_terminals:
        alpha = []
        beta = []
        
        for production in productions[A]:
            if production.startswith(A):
                alpha.append(production[1:])
            else:
                beta.append(production)

        if alpha:
            A_prime = A + "'"
            new_productions[A_prime] = [a + A_prime for a in alpha] + ['']
            new_productions[A] = [b + A_prime for b in beta]
        else:
            new_productions[A] = productions[A]

    return new_productions

if name == "main":
    productions = {
          'A': ['Ab', 'Aa', 'c']
    }
    new_productions = remove_left_recursion(productions)
    for non_terminal, productions in new_productions.items():
        print(non_terminal, "->", " | ".join(productions))


To implement of any one parser (LL(1) FIRST) (JAVA/C/C++, Python, R-lang, Lex).
(Tried and tested)
(This will run only if the production is without 'ε')
def first(productions, non_terminal):
    first_set = set()

    if non_terminal not in productions:
        return first_set

    for expression in productions[non_terminal]:
        if expression[0].islower() or expression[0] == '':
            first_set.add(expression[0])
        elif expression[0].isupper():
            first_set.update(first(productions, expression[0]))

    return first_set

productions = {
    'S': ['ab', 'bA']
}
non_terminal = 'S'
first_set = first(productions, non_terminal)
print(f'First({non_terminal}): {first_set}')


To implement of any one parser (LL(1) FOLLOW) (JAVA/C/C++, Python, R-lang, Lex).
(Tried and tested)

def first(productions, non_terminal):
    first_set = set()

    if non_terminal not in productions:
        return first_set

    for expression in productions[non_terminal]:
        if expression[0].islower() or expression[0] == '':
            first_set.add(expression[0])
        elif expression[0].isupper():
            first_set.update(first(productions, expression[0]))

    return first_set

def follow(productions, start_symbol, non_terminal):
    follow_set = set()

    if non_terminal == start_symbol:
        follow_set.add('$')

    for key, value in productions.items():
        for expression in value:
            for index, symbol in enumerate(expression):
                if symbol == non_terminal and index < len(expression) - 1:
                    follow_set.update(first(productions, expression[index + 1]))
                elif symbol == non_terminal and key != non_terminal:
                    follow_set.update(follow(productions, start_symbol, key))

    return follow_set

# Example usage:
productions = {
    'S': ['AB'],
    'A': ['a'],
    'B': ['b']
}
start_symbol = 'S'
non_terminal = 'A'
follow_set = follow(productions, start_symbol, non_terminal)
print(f'Follow({non_terminal}): {follow_set}')


productions = {
    'S': ['AB'],
    'A': ['a'],
    'B': ['b']
}
start_symbol = 'S'
non_terminal = 'A'
follow_set = follow(productions, start_symbol, non_terminal)
print(f'Follow({non_terminal}): {follow_set}')


To study & implement Code Generation Algorithm. (JAVA/C/C++/Python/R-lang /Lex).

def generate_assembly(expression):
    assembly_code = ""
    assembly_code += "MOV R0, " + expression.split()[0] + "\n"
    assembly_code += "MOV R1, " + expression.split()[2] + "\n"
    if "+" in expression:
        assembly_code += "ADD R0, R1\n"
    elif "-" in expression:
        assembly_code += "SUB R0, R1\n"
    elif "*" in expression:
        assembly_code += "MUL R0, R1\n"
    elif "/" in expression:
        assembly_code += "DIV R0, R1\n"
    return assembly_code

# Example usage:
expression = input("Enter expression (e.g., a + b): ")
assembly_code = generate_assembly(expression)
print("Generated Assembly Code:")
print(assembly_code