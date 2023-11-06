LETTER_TO_MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.',
    'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----',
    '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----',
    ', ': '--..--', '.': '.-.-.-', '?': '..--..',
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-',
    ' ': ' '
}

MORSE_TO_LETTER = {
    morse: letter
    for letter, morse in LETTER_TO_MORSE.items()
}


def encode(message: str) -> str:
    """
    Кодирует строку в соответсвие с таблицей азбуки Морзе

    >>> encode('SOS')
    '... --- ...'
    >>> encode('HELLO')
    '.... . .-.. .-.. ---'
    >>> encode('')
    ''
    >>> encode('whitespace test')
    '.-- .... .. - . ...        .--. .- -.-. .   - . ... -'
    >>> encode('directive test') # doctest: +NORMALIZE_WHITESPACE
    '-.. .. .-. . -.-. -          .. ...- .   - . ... -'
    >>> encode(1)
    Traceback (most recent call last):
    AttributeError: 'int' object has no attribute 'upper'
    """
    encoded_signs = [
        LETTER_TO_MORSE[letter] for letter in message.upper()
    ]
    return ' '.join(encoded_signs)
