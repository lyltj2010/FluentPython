"""
In 2014 the best definition of “character” we have is a **Unicode character**.
Accordingly, the items you get out of a Python 3 str are Unicode characters,
just like the items of a unicode object in Python 2 —
and not the raw bytes you get from a Python 2 str.

The Unicode standard explicitly separates the [identity of characters] from [specific byte representations].

* The identity of a character — its code point — is a number from 0 to 1,114,111 (base 10), 
    shown in the Unicode standard as 4 to 6 hexadecimal digits with a “U+” prefix. 
    For example, the code point for the letter A is U+0041, 
    the Euro sign is U+20AC 
    and the musical symbol G clef is assigned to code point U+1D11E. 
    About 10% of the valid code points have characters assigned to them in Unicode 6.3, the standard used in Python 3.4.
* The actual bytes that represent a character depend on the encoding in use. 
    An encoding is an algorithm that converts code points to byte sequences and vice-versa.
    The code point for A (U+0041) is encoded as the single byte \x41 in the UTF-8 encoding, 
    or as the bytes \x41\x00 in UTF-16LE encoding. 
    As another example, the Euro sign (U+20AC) becomes three bytes in UTF-8 — \xe2\x82\xac —
    but in UTF-16LE it is encoded as two bytes: \xac\x20.
# Encoding and decoding.
>>> s = 'café' # The str 'café' has 4 Unicode characters.
>>> len(s)
4
>>> b = s.encode('utf8') # encode, convert code points to byte sequences
>>> b # bytes literals start with a b prefix.
b'caf\xc3\xa9'
>>> len(b) # bytes b has five bytes (the code point for “é” is encoded as two bytes in UTF-8).
5
>>> b.decode('utf8')
'café'
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()