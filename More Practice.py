#Caesar Shift

def caeser(str, index):
    uppercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    
    crypt = []
    result = []
    for letters in str:
        if letters in uppercase:
            count = uppercase.count(letters)
            crypting = (count + index) % 26
            crypt.append(crypting)
            newLetter = uppercase[crypting]
            result.append(newLetter)

    return result

print caeser('abc', 2)