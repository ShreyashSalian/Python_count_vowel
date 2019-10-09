#Wap to count the number of each vowel in string

def count_vowel(string):
    vowel  = "aeiou"
    c = {}.fromkeys(vowel,0)
    string = string.lower()
    for co in string:
        if co in c:
            c[co] += 1
    return c
string = input("Enter The String : ")
print(count_vowel(string))