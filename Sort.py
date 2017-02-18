#To sort the words in a string alphabetically

string = "hello, my name is navneet saggu. i want to sort this sentence alphabetically."

words = string.split()
print(words)

words.sort()

print(words)

#count the number of each vowel


str = "hello, my name is navneet saggu. i want to sort this sentence alphabetically."
count = 0
e_count=0
for letter in str:
    if letter == 'a':
        count = count+1
    elif letter == 'e':
        e_count = e_count+1
print(count)
print(e_count)

#Remove punctuations from a string
sentence = "hello!! my name is navneet saggu, i want to sort this sentence alphabetically."
no_p = ' '

for let in sentence:
    if let == '!':
        let = no_p

print(sentence)

#program to get a string from a given string where all occurrences of it's first char have been change to '$'

str1 = "hello. I am home"
n=0
for let in str1:
    if str1[n] == str1[n+1]:
        print("Same")
    else:
        print("No Bueno")


def change_char(str2):
    char = str2[0]
    str2 = str2.replace(char, '$')
    str2 = char+str2[1:]
    return str2
print(change_char('restart'))

def swap_char(str3):
    char1 = str3[2] # c
    char2 = str3[7] # z
    str4 = str3[5:8]
    print(str4)
    str3 = str3.replace(str3[2], char2)
    str3 = str3[0:4]
    print(str3)
    str5 = str4.replace(str4[2], char1)
    str3 = str3 + str5

    return str3
print(swap_char('abc, xyz'))


def chars_mix_up(a, b):
  new_a = b[:2] + a[2:]
  print(new_a)
  new_b = a[:2] + b[2:]

  return new_a + ' ' + new_b
print(chars_mix_up('abc', 'xyz'))

word = 'ing'
def ing_string(sentence):
    length = len(sentence)
    if length > 2:
        if sentence[-3:] == 'ing':
            sentence += 'ly'

        else:
            sentence += 'ing'
    return sentence
print(ing_string('navneet'))















