#1
string1 = "Reverse"
reveresed_string = ''
for letter in range(len(string1) -1, -1, -1):
    reveresed_string += string1[letter]

print(reveresed_string)

#2
string2 = "capital letters"
capital_string = string2.title()
print(capital_string)

#3
def compress_string(string3): 
    result = ""
    count = 1
    for letter in range(1, len(string3)):
        if string3[letter - 1] == string3[letter]:
            count += 1
        else:
            result = result + string3[letter - 1]
            if count > 1:
                result += str(count)
                count = 1
    result = result + string3[-1]
    if count > 1:
        result += str(count)
    return result 

string3 = "stttrrrrrriinnng"
print(compress_string(string3))

#4
string4 = input("Enter string ")
if (string4 == string4[::-1]):
    print("This string is a palindrome")
else:
    print("This string is not a palindrome")









