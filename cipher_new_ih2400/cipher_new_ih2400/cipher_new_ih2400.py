def cipher(text, shift, encrypt=True):
    """
    This encrypts and decrypts any given text.
    
    Parameters
    ----------
    text: This is the text to be encrypted/decrypted.
    shift: Degree that text is to be encrpyted. Shift = 1 encrypts it one letter forward, shift=2 two letters forward, and so on. 
    encypt: encrypt=True to encrypt, encrypt=False to decrypt.
    
    
    Returns
    -------
    new_text
    
    Examples
    --------
    
    >>> cipher(Hello, shift = 1, encypt= True)
    returns: Ifmmp
    
    >>> cipher(Ifmmp, shift = 1, encrypt= False)
    returns: Hello
    
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text

