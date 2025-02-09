name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))
age = 2025 - birth_year
print("Hello", name, ", you are", age, "years old.")

txt = "LMaasleitbtui"
car = txt[1] + txt[5] + txt[6] + txt[-1]
print(car)

text = input("Enter a string: ")
length = 0
for char in text:
    length += 1
print("Length:", length)
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())

text = input("Enter a string: ")
reverse = ""
for char in text:
    reverse = char + reverse
if text == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")

text = input("Enter a string: ")
vowels = "aeiouAEIOU"
v_count = 0
c_count = 0
for char in text:
    if char in vowels:
        v_count += 1
    elif char.isalpha():
        c_count += 1
print("Vowels:", v_count, "Consonants:", c_count)

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
if str2 in str1:
    print("Found")
else:
    print("Not found")

sentence = input("Enter a sentence: ")
old_word = input("Word to replace: ")
new_word = input("Replace with: ")
new_sentence = ""
words = sentence.split()
for word in words:
    if word == old_word:
        new_sentence += new_word + " "
    else:
        new_sentence += word + " "
print(new_sentence.strip())

text = input("Enter a string: ")
print("First:", text[0], "Last:", text[-1])

text = input("Enter a string: ")
reverse = ""
for char in text:
    reverse = char + reverse
print(reverse)

sentence = input("Enter a sentence: ")
words = sentence.split()
count = 0
for word in words:
    count += 1
print("Word count:", count)

text = input("Enter a string: ")
found_digit = False
for char in text:
    if char.isdigit():
        found_digit = True
        break
if found_digit:
    print("Contains digits")
else:
    print("No digits found")

words = input("Enter words separated by spaces: ").split()
separator = input("Enter separator: ")
result = words[0]
for word in words[1:]:
    result += separator + word
print(result)

text = input("Enter a string: ")
new_text = ""
for char in text:
    if char != " ":
        new_text += char
print(new_text)

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
if str1 == str2:
    print("Equal")
else:
    print("Not equal")

sentence = input("Enter a sentence: ")
acronym = ""
for word in sentence.split():
    acronym += word[0].upper()
print(acronym)

text = input("Enter a string: ")
char = input("Enter character to remove: ")
new_text = ""
for c in text:
    if c != char:
        new_text += c
print(new_text)

text = input("Enter a string: ")
vowels = "aeiouAEIOU"
new_text = ""
for char in text:
    if char in vowels:
        new_text += "*"
    else:
        new_text += char
print(new_text)

text = input("Enter a sentence: ")
start = input("Starts with: ")
end = input("Ends with: ")
if text.startswith(start):
    print("Starts with", start)
else:
    print("Does not start with", start)
if text.endswith(end):
    print("Ends with", end)
else:
    print("Does not end with", end)
