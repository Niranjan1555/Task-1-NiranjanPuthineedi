from datetime import datetime

print("AI Chatbot")
print("Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    
    if user in ["hello", "hi", "hey"]:
        print("Bot: Hello! How can I help you?")

    
    elif user == "what is your name":
        print("Bot: I am a Rule-Based AI Chatbot.")

    
    elif user == "how are you":
        print("Bot: I am doing great. Thank you!")

    elif user == "date":
        today = datetime.now().strftime("%d-%m-%Y")
        print("Bot: Today's date is", today)

    
    elif user == "time":
        current_time = datetime.now().strftime("%H:%M:%S")
        print("Bot: Current time is", current_time)

    
    elif user == "which college are you from":
        print("Bot: I am from Malla Reddy University.")

    elif user == "which branch":
        print("Bot: Artificial Intelligence and Machine Learning (AIML).")

    
    elif user == "tell me a joke":
        print("Bot: Why do programmers prefer dark mode? Because light attracts bugs!")

    elif user == "tell me a story title":
        print("Bot: Professional Student!")

   
    elif user == "add":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Bot: Sum =", num1 + num2)

    elif user == "subtract":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Bot: Difference =", num1 - num2)

    elif user == "multiply":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Bot: Product =", num1 * num2)

    elif user == "divide":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if num2 != 0:
            print("Bot: Quotient =", num1 / num2)
        else:
            print("Bot: Cannot divide by zero.")

    
    elif user == "help":
        print("""
Bot: Available commands:
- hello, hi, hey
- how are you
- what is your name
- date
- time
- which college are you from
- which branch
- tell me a joke
- tell me a story title
- add
- subtract
- multiply
- divide
- bye
""")


    elif user == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    
    else:
        print("Bot: Sorry, I don't understand that.")