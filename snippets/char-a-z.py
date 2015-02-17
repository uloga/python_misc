# #####################################################
# creates character set ( A to Z ) lower or uppercase

def abc(start, end, letter_case= None):
        letters = []
        for letter in range(ord(start), ord(end)+1 ):
            if letter_case == 'upper':
                letters.append(str.upper(chr(letter)))
            elif letter_case == 'lower':
                letters.append(str.lower(chr(letter)))
            else:
                letters.append(str.lower(chr(letter)))
                
        return letters
 
#example one
print(abc('a', 'z'))
 
#example letter_case
print(abc('a', 'z', 'upper'))
