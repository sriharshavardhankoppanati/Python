# 1.String Concatenation:
string1 = "Hello"
string2 = input("Enter the name:")
string3 = string1 +" "+ string2
print(string3)
string4 = ", welcome to Python programming"
string5 = string3+string4
print(string5)
#2.String Slicing and Indexing:
#Print the first character of the string.
a= string5
print(a[0])
#Print the last character of the string.
print(a[-1])
#Print the first 5 characters of the string.
print(a[:5])
#Print the last 11 characters of the string.
print(a[-11:])
#Print the string in reverse.
print(a[::-1])
#Use slicing and print the word “Python” from the existing string.
print(a[25:31])
#3. String Methods:
strM = "Python beginner tutorial"
#Convert the sentence to uppercase.
print(strM.upper())
#Convert the sentence to lowercase.
print(strM.lower())
#Use Capitalize and return the sentence to the original input form.
print(strM.capitalize())
#Count the total number of occurrences of character ‘t’ in the string
print(strM.count('t'))
#Replace all occurrences of “Python” with “Machine Learning” in the input string strM = “Python beginner tutorial”
print(strM.replace("Python","Machine Learning"))
#4.Tuples (Creation, Modification and Access) :
t1=(10,20,30)
t2=(40,50,60)
t_combine = t1+t2
print(t_combine)
#Repeat the elements of “t_combine” 3 times
print(t_combine*3)
#Access the 3rd element from “t_combine”
print(t_combine[2])
#Access the first three elements from “t_combine”
print(t_combine[:3])
#Access the last three elements from “t_combine”
print(t_combine[3:])