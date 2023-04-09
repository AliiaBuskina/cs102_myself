import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for l in plaintext:
        if l.isalpha():
            if l.isupper():
                l = chr((ord(l) + shift - ord("A")) % 26 + ord("A"))
            if l.islower():
                l = chr((ord(l) + shift - ord("a")) % 26 + ord("a"))
        ciphertext += l
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for l in ciphertext:
        if l.isalpha():
            if l.isupper():
                l = chr((ord(l) - shift - ord("A")) % 26 + ord("A"))
            if l.islower():
                l = chr((ord(l) - shift - ord("a")) % 26 + ord("a"))
        plaintext += l
        return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift
