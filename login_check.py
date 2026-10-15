username = input("Enter username: ")
password = input("Enter password: ")
email = input("Enter email: ")

def login_check(username,password,email):
    validation_count = 0
    # Username validation
    ch_count = 0
    for ch in username:
        ch_count += 1
    
    if(ch_count > 3):
        validation_count += 1
    else:
        print("Username must be more than 3 characters")

    # Password validation
    char = 0
    is_num = False
    for i in password:
        char += 1
        if i in '1234567890':
            is_num = True

    if char >= 8 and is_num == True:
        validation_count += 1
    else:
        print("Password must contain minimum 8 characters and atleast 1 number")

    # Email validation
    is_sym = False
    for cha in email:
        if cha in '@':
            is_sym = True
    if is_sym == True:
        validation_count += 1
    else:
        print("Invalid email")

    if validation_count == 3:
        print("Your entered data is correct. Sign-up successful!")
    else:
        print("Please try again")
            

login_check(username,password,email)