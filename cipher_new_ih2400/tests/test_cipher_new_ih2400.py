from cipher_new_ih2400 import __version__
from cipher_new_ih2400 import cipher_new_ih2400

import pytest

#these tests need to be performed on edge cases

def cipher(text, shift, encrypt=True):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    if type(shift) == str:
        raise AssertionError
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text

def test_cipher_singleword():
    example = 'Hi'
    expected = "Ij"
    actual = cipher("Hi", shift = 1)
    assert actual == expected

def test_version():
    assert __version__ == '0.1.0'

#explain what tests are doing in documentation
