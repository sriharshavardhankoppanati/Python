# Project: Survey Feedback Analyzer
# Python Fundamentals - Module End Assignment 3
# Additional relevant features are included while keeping all required steps.

feedback_data = {
    "S_No": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Name": ["Ravi", "Meera", "Sam", "Anu", "Raj", "Divya", "Arjun", "Kiran", "Leela", "Nisha"],
    "Feedback": [
        "   Very GOOD Service!!!",
        "poor support,        not happy   ",
        "GREAT experience! will come again.",
        "okay     okay...",
        "   not    BAD",
        "Excellent care, excellent staff!",
        "good food and good ambience!",
        "Poor response and poor handling of issue",
        "Satisfied. But could be better.",
        "Good support... quick service."
    ],
    "Rating": [5, 2, 5, 3, 2, 5, 4, 1, 3, 4]
}

print("=" * 60)
print("              SURVEY FEEDBACK ANALYZER")
print("=" * 60)

print("\nInitial feedback records:", len(feedback_data["S_No"]))

# STEP 2: Add more feedbacks
# Validate the number of records and ensure each rating is between 1 and 5.
while True:
    try:
        num_new_feedbacks = int(input("\nHow many more feedbacks do you want to add? "))
        if num_new_feedbacks < 0:
            print("Please enter zero or a positive number.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a whole number.")

for i in range(num_new_feedbacks):
    print(f"\nEnter details for feedback {i + 1}")

    name = input("Enter name: ").strip()
    while not name:
        print("Name cannot be empty.")
        name = input("Enter name: ").strip()

    feedback = input("Enter written feedback: ").strip()
    while not feedback:
        print("Feedback cannot be empty.")
        feedback = input("Enter written feedback: ").strip()

    while True:
        try:
            rating = int(input("Enter rating (1-5): "))
            if 1 <= rating <= 5:
                break
            print("Rating must be between 1 and 5.")
        except ValueError:
            print("Invalid rating. Enter a whole number from 1 to 5.")

    s_no = len(feedback_data["S_No"]) + 1
    feedback_data["S_No"].append(s_no)
    feedback_data["Name"].append(name)
    feedback_data["Feedback"].append(feedback)
    feedback_data["Rating"].append(rating)

print("\nFeedback entry completed.")
print("Total feedback records:", len(feedback_data["S_No"]))


# STEP 3: Text Cleaning
# Remove the punctuation requested in the assignment, normalize spaces,
# trim the text, and convert it to lowercase.
punctuation = [".", ",", "!", "?"]

for i in range(len(feedback_data["Feedback"])):
    text = feedback_data["Feedback"][i]

    for mark in punctuation:
        text = text.replace(mark, "")

    text = " ".join(text.split())
    text = text.strip()
    text = text.lower()

    feedback_data["Feedback"][i] = text

print("\nFeedback text cleaned successfully.")


# STEP 4: Word Count Insights
# Count the number of feedback entries containing a whole word.
def count_word_in_feedbacks(word):
    count = 0
    search_word = word.lower().strip()

    for feedback in feedback_data["Feedback"]:
        words = feedback.split()
        if search_word in words:
            count += 1

    return count


print("\nWORD COUNT INSIGHTS")
for word in ["good", "poor", "excellent"]:
    print(f"Feedbacks containing '{word}': {count_word_in_feedbacks(word)}")


# STEP 5: Final Summary and Insights
print("\n" + "=" * 60)
print("FINAL CLEANED FEEDBACK DATA")
print("=" * 60)
print(feedback_data)

# Average rating
average_rating = sum(feedback_data["Rating"]) / len(feedback_data["Rating"])
print(f"\nAverage rating: {average_rating:.2f} / 5")

# Highest and lowest ratings
highest_rating = max(feedback_data["Rating"])
lowest_rating = min(feedback_data["Rating"])
print("Highest rating:", highest_rating)
print("Lowest rating:", lowest_rating)

# Feedback with the longest comment (based on word count)
longest_feedback = max(feedback_data["Feedback"], key=lambda comment: len(comment.split()))
longest_word_count = len(longest_feedback.split())
print("\nFeedback with the longest comment:")
print(longest_feedback)
print("Word count:", longest_word_count)

# Unique words across all feedbacks
unique_words = set()
for feedback in feedback_data["Feedback"]:
    unique_words.update(feedback.split())

print("\nUnique words used across all feedbacks (alphabetical order):")
print(sorted(unique_words))
print("Total unique words:", len(unique_words))

# Additional insight: rating distribution
print("\nRATING DISTRIBUTION")
for rating in range(5, 0, -1):
    count = feedback_data["Rating"].count(rating)
    print(f"Rating {rating}: {count} feedback(s)")

# Additional insight: simple rating-based feedback categories
positive_count = sum(1 for rating in feedback_data["Rating"] if rating >= 4)
neutral_count = sum(1 for rating in feedback_data["Rating"] if rating == 3)
negative_count = sum(1 for rating in feedback_data["Rating"] if rating <= 2)

print("\nCUSTOMER SATISFACTION SUMMARY")
print("Positive ratings (4-5):", positive_count)
print("Neutral ratings (3):", neutral_count)
print("Low ratings (1-2):", negative_count)

# Optional assignment feature: sort entries from highest to lowest rating.
sorted_feedbacks = sorted(
    zip(
        feedback_data["S_No"],
        feedback_data["Name"],
        feedback_data["Feedback"],
        feedback_data["Rating"]
    ),
    key=lambda entry: entry[3],
    reverse=True
)

print("\nFEEDBACKS SORTED BY RATING (HIGHEST TO LOWEST)")
for s_no, name, feedback, rating in sorted_feedbacks:
    print(f"S.No: {s_no} | Name: {name} | Rating: {rating} | Feedback: {feedback}")

print("\nAnalysis completed successfully.")
