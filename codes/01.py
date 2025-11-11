try:
    user_input = int(input("input: "))
    for i in range(user_input+1):
        print("*" * i)
except ValueError as e:
    print(f"Error type: {type(e)}")      
    print(f"Error message: {e}")         
    print(f"Error args: {e.args}")       
    print(f"First arg: {e.args[0]}")     