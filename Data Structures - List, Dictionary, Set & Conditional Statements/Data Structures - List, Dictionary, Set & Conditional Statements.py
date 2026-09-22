#1. List – Creation, Modification and Access
#1(a). List Creation – age_list
# Create a list containing five integer values
age_list = [24, 25, 26, 27, 28]
# Print the age list
print(age_list)
#1(b). Create name_list
# Create a list containing five names
name_list = ["Harsha", "Rahul", "Priya", "Anjali", "Kiran"]
# Print the name list
print(name_list)
#2. List Operations / Modifications
#2(a). Append "Yazhini"
# Add "Yazhini" to the end of name_list
name_list.append("Yazhini")
# Print the updated list
print(name_list)
#2(b). Insert 30 at index 2
# Insert 30 at index position 2
age_list.insert(2, 30)
# Print the updated age list
print(age_list)
#2(c). Remove "Yazhini"
# Remove "Yazhini" from the list
name_list.remove("Yazhini")
# Print the updated list
print(name_list)
#2(d). Pop the last element
# Remove the last element from age_list
age_list.pop()
# Print the updated list
print(age_list)
#2(e). Extend age_list
# Add multiple ages to the end of age_list
age_list.extend([29, 30, 26])
# Print the updated list
print(age_list)
#2(f). Sort age_list in descending order
# Sort the age list from highest to lowest
age_list.sort(reverse=True)
# Print the sorted list
print(age_list)
#2(g). Find Max, Min and Sum
# Find the highest age
maximum_age = max(age_list)
# Find the lowest age
minimum_age = min(age_list)
# Find the total of all ages
total_age = sum(age_list)
# Print the results
print("Maximum age:", maximum_age)
print("Minimum age:", minimum_age)
print("Sum of all ages:", total_age)
#3. Accessing List Elements
#3(a). Print the first element
# Access the first element using index 0
print(name_list[0])
#3(b). Print the last element
# Access the last element using index -1
print(name_list[-1])
#3(c). Print elements from index 2 to index 4
# Access elements from index 2 up to index 4
print(name_list[2:5])
#3(d). Print the list in reverse order
# Reverse the list using slicing
print(name_list[::-1])
#4. Dictionary – Creation, Modification and Access
#4(a). Create student_marks
# Create a dictionary with student names as keys
# and their marks as values
student_marks = {
"Harsha": 85,
"Rahul": 78,
"Priya": 92,
"Anjali": 88,
"Kiran": 75
}
# Print the dictionary
print(student_marks)
#4(b). Access a specific student's mark
# Access Harsha's mark using the dictionary key
print(student_marks["Harsha"])
#4(c). Add Janani with mark 80
# Add a new student and their mark
student_marks["Janani"] = 80
# Print the updated dictionary
print(student_marks)
#4(d). Update an older student's mark to 82
# Update Rahul's existing mark to 82
student_marks["Rahul"] = 82
# Print the updated dictionary
print(student_marks)
#4(e). Use keys(), values() and items()
# Print all the keys (student names)
print("Keys:", student_marks.keys())
# Print all the values (marks)
print("Values:", student_marks.values())
# Print all key-value pairs
print("Items:", student_marks.items())
#5. Sets – Operations
#5(a). Create my_set and analyze the output
# Create a set containing vowels
my_set = {'a', 'e', 'i', 'o', 'u', 'a', 'a', 'i'}
# Print the set
print(my_set)
#5(b). Attempt to change my_set[4]
# Attempt to change an element at index 4
my_set[4] = 's'
#5(c). Create set1 and set2
# Create the first set
set1 = {1, 3, 5, 7, 9}
# Create the second set
set2 = {2, 3, 5, 8, 10}
# Print both sets
print("Set 1:", set1)
print("Set 2:", set2)
#5(d). Compute union and intersection
# Find the union of set1 and set2
union_set = set1.union(set2)
# Find the intersection of set1 and set2
intersection_set = set1.intersection(set2)
# Print the results
print("Union:", union_set)
print("Intersection:", intersection_set)
#7. Operators & Conditional Statements 
# Ask the user to enter a score
score = float(input("Enter your score (0 to 10): "))
# Check whether the score is within the valid range
if score < 0 or score > 10:
    print("Invalid score. Please enter a score between 0 and 10.")

# Check whether the score is greater than 7
elif score > 7:
    print("Above Average: Excellent work! Keep up the great performance.")

# Check whether the score is between 4 and 7
elif score >= 4:
    print("Average: Good effort! Keep practicing, there's room for improvement.")

# If the score is less than 4
else:
    print("Below Average: Need to improve your performance. Consistent practice will lead to better results.")