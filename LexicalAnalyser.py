import re                                 # for performing regex expressions

tokens = []                               # for string tokens
lines = []

while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break
text = '\n'.join(lines)

text = text.split()


# Loop through each  code word
for word in text:
    
    # This will check if a token has datatype decleration
    if word in ['str', 'int', 'bool', 'float', 'long']: 
        tokens.append(['KEYWORD', word])
    
    # This will look for an identifier which would be just a word
    elif re.match("[a-z]", word) or re.match("[A-Z]", word):
        tokens.append(['IDENTIFIER', word])
    # This will look for an operator
    elif word in '*-/+%=<>!':
        tokens.append(['OPERATOR', word])
    
    # This will look for integer items and cast them as a number
    elif re.match(".[0-9]", word):
        if word[len(word) - 1] == ';': 
            tokens.append(["INTEGER", word[:-1]])
            tokens.append(['END_STATEMENT', ';'])
        else: 
            tokens.append(["INTEGER", word])

print("Number of lines:", len(lines))
print(tokens) # Outputs the token array
