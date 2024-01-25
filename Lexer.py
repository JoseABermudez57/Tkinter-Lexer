import re

class Lexer:
    def __init__(self, input_text):
        self.input_text = input_text
        self.pos = 0

        self.reserved_words = {
            'INTEGER_TYPE': 'Ent',
            'BOOLEAN_TYPE': 'Bool',
            'DECIMAL_TYPE': 'Dec',
            'STRING_TYPE': 'Cdn',
            'IF': 'if',
            'FOR': 'for',
            'PIPE': '|',
            'EQUAL': '==',
            'ASSIGNMENT': '=',
            'GREATER_THAN': '>',
            'LESS_THAN': '<',
            'GREATER_OR_EQUAL': '>=',
            'OPEN_BODY': '=>',
            'LESS_OR_EQUAL': '<=',
            'NOT_EQUAL': '!=',
            'PARENTHESIS_CLOSE': ')',
            'PARENTHESIS_OPEN': '(',
            'QUOTATION_MARKS': '"',
            'ADDITION': '+',
            'SUBTRACTION': '-',
            'MULTIPLY': '*',
            'DIVISION': '/',
            'RETURN': 'rtn'
        }

        self.reserved_words = dict(sorted(self.reserved_words.items(), key=lambda x: len(x[1]), reverse=True))
        self.variable_regex = re.compile(r'^[a-zA-Z][a-zA-Z0-9]*$')

    def next_token(self):
        self.skip_whitespace()
        if self.pos >= len(self.input_text):
            return None

        char = self.input_text[self.pos]
        number = ''

        while self.pos < len(self.input_text) and char.isdigit():
            number += char
            self.pos += 1
            char = self.input_text[self.pos] if self.pos < len(self.input_text) else ''

        if number:
            return f'TOKEN: NUMBER - LEXEMA: {number}\n'

        for token, lexem in self.reserved_words.items():
            if self.input_text[self.pos:].startswith(lexem):
                self.pos += len(lexem)
                return f'TOKEN: {token} - LEXEMA: {lexem}\n'

        word = ''

        while self.pos < len(self.input_text) and char.isalnum():
            word += char
            self.pos += 1
            char = self.input_text[self.pos] if self.pos < len(self.input_text) else ''

        if word:
            if self.is_valid_variable(word):
                return f'TOKEN: STRING - LEXEMA: {word}\n'
            else:
                return f'TOKEN: INVALID_VARIABLE - LEXEMA: {word}\n'

        self.pos += 1

        return f'TOKEN: UNKNOWN_TOKEN - LEXEMA: {char}\n'

    def skip_whitespace(self):
        self.pos += len(self.input_text[self.pos:]) - len(self.input_text[self.pos:].lstrip())

    def is_valid_variable(self, variable):
        variable_regex = re.compile(r'^[a-zA-Z_][a-zA-Z0-9_]*$')
        return bool(variable_regex.match(variable))