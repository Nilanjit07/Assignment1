#Q1. Use the len method to print the length of the string.


x = "Hello World"
print(len(x))

#Q2. Get the first character of the string txt.


txt = "Hello World"
x = txt[0]

#Q3. Get the characters from index 2 to index 4 (llo).


txt = "Hello World"
x = txt[2:5]

#Q4. Return the string without any whitespace at the beginning or the end.

txt = " Hello World "
x = txt.strip()

#Q5. Convert the value of txt to upper case.


txt = "Hello World"
txt = txt.upper()

#Q6. Convert the value of txt to lower case.


txt = "Hello World"
txt = txt.lower()

#Q7. Replace the character H with a J.


txt = "Hello World"
txt = txt.replace("H","J")

#Q8. Insert the correct syntax to add a placeholder for the age parameter.


age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
