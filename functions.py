def get_chatbot_response(message):
    if message[:2] != "!!":
        
        return ''

    points, command, args = message.split(' ', 2)
    
    if command == "Hey":
        return "What's up!"
    elif command == "add":
        num1, num2 = args.split()
        return int(num1) + int(num2)
    elif command == "divide":
        num1, num2 = args.split()
        return int(num1) / int(num2)
    elif command == "say":
        return args
    else:
        return "Oops! I didn't recognize your command :("

print (get_chatbot_response("!! add 6 2"))
print (get_chatbot_response("!! divide 6 2"))