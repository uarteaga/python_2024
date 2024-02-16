import re

mensaje = "A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern. RegEx can be used to check if a string contains the specified search pattern."

palabra = "sequence"

if palabra in mensaje:
    print('found!')

else:
    print('NOT found!')

email = "dkdjd@gmail.com"

if '@' in email and '.' in email:
    print('Valid email')