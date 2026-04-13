# Simple AI Automation Agent (Mock Version)

def ai_agent(task):
    if "email" in task.lower():
        return "Generated Email: Hello, I hope you're doing well. Let’s connect soon."
    
    elif "summary" in task.lower():
        return "Summary: This text has been summarized using AI logic."

    elif "code" in task.lower():
        return "Code Suggestion: def hello(): print('Hello World')"

    else:
        return "AI Response: Task processed successfully."

if __name__ == "__main__":
    print("🤖 AI Automation Agent Started")
    
    user_input = input("Enter your task: ")
    
    result = ai_agent(user_input)
    
    print("\nResult:")
    print(result)
