def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    ciphertext = ""
    if len(plaintext) > len(keyword):
        keyword *= len(plaintext) // len(keyword) + 1
    for i in range(len(plaintext)):
        bc = plaintext[i]
        k = keyword[i]
        if k.isupper():
            sd = ord(k) - ord("A")
        if k.islower():
            sd = ord(k) - ord("a")
        if bc.isalpha():
            if bc.isupper():
                bc = chr((ord(bc) + sd - ord("A")) % 26 + ord("A"))
            if bc.islower():
                bc = chr((ord(bc) + sd - ord("a")) % 26 + ord("a"))
        ciphertext += bc

    return ciphertext



def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    if len(ciphertext) > len(keyword):
        keyword *= len(ciphertext) // len(keyword) + 1
    for i in range(len(ciphertext)):
        bd = ciphertext[i]
        k = keyword[i]
        if k.isupper():
            sd = ord(k) - ord("A")
        elif k.islower():
            sd = ord(k) - ord("a")
        else:
            sd = 0
        if bd.isalpha():
            if bd.isupper():
                bc = chr((ord(bd) - sd - ord("A")) % 26 + ord("A"))
            else:
                bc = chr((ord(bd) - sd - ord("a")) % 26 + ord("a"))
        else:
            bc = bd
        plaintext += bc
    return plaintext
