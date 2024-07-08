reserved_usernames = {"admin", "root", "superuser"}

username = input("Enter username: ")
if len(username) < 5 or len(username) > 20 or not username.isalnum() or username in reserved_usernames:
    print("Invalid username")
else:
    email = input("Enter email: ")
    if '@' in email and '.' in email.split('@')[-1]:
        phone = input("Enter phone number: ")
        phone_num = phone[4:] if phone.startswith("+374") else phone[1:] if phone.startswith('0') else phone

        if phone_num.isdigit() and len(phone_num) == 8:
            password = input("Enter password: ")
            if len(password) >= 8:
                has_upper = has_lower = has_digit = has_special = False
                for word in password:
                    if word.isupper():
                        has_upper = True
                    elif word.islower():
                        has_lower = True
                    elif word.isdigit():
                        has_digit = True
                    elif word in '!@#$%^&*':
                        has_special = True

                if has_upper and has_lower and has_digit and has_special:
                    password_repeat = input("Repeat password: ")
                    if password == password_repeat:
                        print("Registration successful")
                    else:
                        print("Passwords do not match")
                else:
                    print("Invalid password. It should contain uppercase, lowercase, digit and special character")
            else:
                print("Invalid password. It should have at least 8 characters")
        else:
            print("Invalid phone number")
    else:
        print("Invalid email format")
