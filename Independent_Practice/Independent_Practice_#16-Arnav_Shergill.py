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
        "question":"What does Micro Center sell?",
        "answer":"PC parts and other electronics"
    }
]

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
    else:
        print(f"\nIncorrect. The correct answer is '{correct_answer}'")
    
    f.user_continue()
    counter += 1
    f.dash()
