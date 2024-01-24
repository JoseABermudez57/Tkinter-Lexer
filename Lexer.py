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
            'GREATER_THAN': '>',
            'LESS_THAN': '<',
            'GREATER_OR_EQUAL': '>=',
            'OPEN_BODY': '=>',
            'LESS_OR_EQUAL': '<=',
            'NOT_EQUAL': '!=',
            'AND': '&&',
            'OR': '||',
            'PARENTHESIS_CLOSE': ')',
            'PARENTHESIS_OPEN': '(',
            'OPEN_BRACKETS': '{',
            'CLOSE_BRACKETS': '}',
            'QUOTATION_MARKS': '"',
            'ADDITION': '+',
            'SUBTRACTION': '-',
            'MULTIPLY': '*',
            'DIVISION': '/',
        }

        self.reserved_words = dict(sorted(self.reserved_words.items(), key=lambda x: len(x[1]), reverse=True))

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
            return f'LEXEM: NUMBER       -      TOKEN: {number}\n'

        for lexem, word in self.reserved_words.items():
            if self.input_text[self.pos:].startswith(word):
                self.pos += len(word)
                return f'LEXEM: {lexem}      -      TOKEN: {word}\n'

        word = ''

        while self.pos < len(self.input_text) and char.isalnum():
            word += char
            self.pos += 1
            char = self.input_text[self.pos] if self.pos < len(self.input_text) else ''

        if word:
            return f'LEXEM: UNKNOWN_TOKEN     -     TOKEN: {word}\n'

        self.pos += 1

        return f'LEXEM: UNKNOWN_TOKEN     -     TOKEN: {char}\n'

    def skip_whitespace(self):
        self.pos += len(self.input_text[self.pos:]) - len(self.input_text[self.pos:].lstrip())
        