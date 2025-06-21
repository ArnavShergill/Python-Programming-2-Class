import formatting as f
import random as r

# Display title and separator
f.title("Independent Practice #16")
f.dash()

# Define questions and answers in a more organized way
quiz = [
    {
        "question": "What is the name of Hennessey Performance's hypercar?\n",
        "answer": "Hennessey Venom F5"
    },
    {
        "question": "Where is the Microsoft Headquarters?\n",
        "answer": "Redmond, Washington"
    },
    {
        "question": "Who was the initial developer of Minecraft?\n",
        "answer": "Notch"
    },
    {
        "question": "When was Minecraft released to the public?\n",
        "answer": "May 17, 2009"
    },
    {
        "question": "Why do people hate FWD vehicles like the Honda Civic?\n",
        "answer": "They understeer a lot"
    },
    {
        "question":"What does Micro Center sell?\n",
        "answer":"PC parts and other electronics"
    },
    {
        "question":"What car was Sally from Cars based on?\n",
        "answer":"Porsche 911"
    },
    {
        "question":"What was the name of the movie where Ford sets out to beat Ferrari at 24 Hours of Le Mans?\n",
        "answer":"Ford vs Ferrari"
    },
    {
        "question":"What is the released date of 'A Minecraft Movie?'\n",
        "answer":"April 4, 2025"
    },
    {
        "question":"Did the ring have an affect on Bilbo at the end of the last 'Lord of the Rings' movie?\n",
        "answer":"Yes"
    },
    {
        "question":"What is the nickname given to the Mustang GTD?\n",
        "answer":"Porsche 911 GT3 Killer"
    },
    {
        "question":"What is the most powerful gpu the average consumer can buy?\n",
        "answer":"Nvidia RTX 5090 TI"
    },
    {
        "question":"Is the NVMe, SSD, or HDD the fastest?\n",
        "answer":"NVMe"
    },
    {
        "question":"Is there going to be a Minecraft 2 in the future?\n",
        "answer":"Yes"
    },
    {
        "question":"What is considered the final boss in Minecraft?\n",
        "answer":"Ender Dragon"
    }
]

correct_counter = 0
incorrect_counter = 0
incorrect_answers = []
counter = 0

while counter < len(quiz):
    # Get current question and answer
    current_item = quiz[counter]
    question = current_item["question"]
    correct_answer = current_item["answer"]
    
    # Display question and get user input
    print(question)
    user_response = input("Your answer: ")
    
    # Check answer and provide feedback
    if str(user_response.strip()) == str(correct_answer):  # Convert to strings and remove whitespace
        print("\nCorrect!")
        correct_counter += 1
    else:
        print(f"\nIncorrect. The correct answer is '{correct_answer}'")
        incorrect_counter += 1
        incorrect_answers.append(current_item)
    
    counter += 1
    f.dash()

# Print results
print(f"You got {correct_counter} questions right.")
print(f"You got {incorrect_counter} questions wrong.")

# Cycle through incorrect answers
if incorrect_counter > 0:
    print("\nHere are the questions you got wrong with their correct answers:")
    for item in incorrect_answers:
        print(f"\nQuestion: {item['question']}Correct Answer: {item['answer']}")
else:
    print("\nCongratulations! You got all questions correct!")

f.dash()
