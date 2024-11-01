while True:
    user_input = input("Enter something (type 'exit' to stop): ")
    
    if user_input.lower() == 'exit':
        print("Exiting the loop.")
        break
    else:
        print(f"You entered: {user_input}")
