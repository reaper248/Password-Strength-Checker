import os
print("=" * 55)
print("             PASSWORD STRENGTH CHECKER")
print("=" * 55)
special_characters = "!@#$%^&*(),.?\":{}|<>-=_+[]\\;/`~"
common_passwords = [
    "password",
    "123456",
    "12345678",
    "qwerty",
    "admin",
    "welcome",
    "12345",
    "football",
    "monkey",
    "letmein",
    "dragon",
    "master",
    "sunshine",
    "princess",
    "solo"
]
keyboard_patterns = [
    "qwerty",
    "asdfgh",
    "zxcvbn",
    "123456",
    "654321"
]
common_names = ["john","alex","david","emma","smith","mike","sam"]
password = input("Enter a password to evaluate: ")
name=input("Enter YOur Name: ")
regno=(input("Enter Your Regisration Number: "))
length = len(password)
upper_count = 0
lower_count = 0
digit_count = 0
special_count = 0
space_count = 0
has_upper = False
has_lower = False
has_digit = False
has_special = False
has_spaces = False
for char in password:
    if char.isupper():
        upper_count = upper_count + 1
        has_upper = True
    elif char.islower():
        lower_count = lower_count + 1
        has_lower = True
    elif char.isdigit():
        digit_count = digit_count + 1
        has_digit = True
    elif char in special_characters:
        special_count = special_count + 1
        has_special = True
    elif char.isspace():
        space_count = space_count + 1
        has_spaces = True
password_lower = password.lower()
is_common = False
found_common_word = ""
for common in common_passwords:
    if common in password_lower:
        is_common = True
        found_common_word = common
        break
has_keyboard_walk = False
found_pattern = ""
for pattern in keyboard_patterns:
    if pattern in password_lower:
        has_keyboard_walk = True
        found_pattern = pattern
        break
has_name = False
found_name = ""
for name in common_names:
    if name in password_lower:
        has_name = True
        found_name = name
        break
has_repeats = False
consecutive_count = 0
for i in range(len(password) - 1):
    if password[i] == password[i + 1]:
        consecutive_count = consecutive_count + 1
        if consecutive_count >= 2:
            has_repeats = True
            break
    else:
        consecutive_count = 0
starts_with_letter = False
ends_with_special = False
if length > 0:
    if password[0].isalpha():
        starts_with_letter = True
    if password[-1] in special_characters:
        ends_with_special = True
score = 0
feedback = []
if length >= 8:
    score = score + 1
else:
    feedback.append("Password is too short. Must be at least 8 characters long.")
if length >= 12:
    score = score + 1
if length >= 16:
    score = score + 1
if has_upper:
    score = score + 1
else:
    feedback.append("Include at least one uppercase letter (A-Z).")
if has_lower:
    score = score + 1
else:
    feedback.append("Include at least one lowercase letter (a-z).")
if has_digit:
    score = score + 1
else:
    feedback.append("Include at least one numeric digit (0-9).")
if has_special:
    score = score + 1
else:
    feedback.append("Include at least one special character (!@#$%^&*).")
if upper_count >= 2 and lower_count >= 2 and digit_count >= 2:
    score = score + 1
if is_common:
    score = score - 2
    feedback.append("Warning: Contains a very common password pattern ('" + found_common_word + "').")
if has_keyboard_walk:
    score = score - 1
    feedback.append("Warning: Contains a sequential keyboard pattern ('" + found_pattern + "').")
if has_name:
    score = score - 1
    feedback.append("Warning: Contains an easily guessable name ('" + found_name + "').")
if has_repeats:
    score = score - 1
    feedback.append("Warning: Contains 3 or more identical characters in a row.")
if has_spaces:
    feedback.append("Notice: Password contains whitespace characters.")
max_score = 10
if score < 0:
    score = 0
if score > max_score:
    score = max_score
if score <= 2:
    strength = "Very Weak"
elif score <= 4:
    strength = "Weak"
elif score <= 6:
    strength = "Moderate"
elif score <= 8:
    strength = "Strong"
else:
    strength = "Very Strong"
bar_total_blocks = 10
filled_blocks = score
empty_blocks = bar_total_blocks - filled_blocks
visual_bar = "[" + ("#" * filled_blocks) + ("-" * empty_blocks) + "]"
print("\n" + "=" * 55)
print("                 EVALUATION REPORT")
print("=" * 55)
print("Password Length       :", length)
print("Uppercase Count       :", upper_count)
print("Lowercase Count       :", lower_count)
print("Digit Count           :", digit_count)
print("Special Char Count    :", special_count)
print("Whitespace Count      :", space_count)
print("-" * 55)
print("Security Score        :", score, "/", max_score)
print("Score Visualizer      :", visual_bar)
print("Strength Rating       :", strength)
print("-" * 55)
if len(feedback) > 0:
    print("Actionable Suggestions:")
    for tip in feedback:
        print("  *", tip)
else:
    print("Excellent! Your password passed all security checks.")
print("=" * 55)
save_option = input("\nDo you want to save this report to a file? (yes/no): ")
if save_option.lower() == "yes" or save_option.lower() == "y":
    file_name = "saved_passwords.txt"
    file = open(file_name, "a")
    file.write("=" * 50 + "\n")
    file.write("           PASSWORD AUDIT ENTRY\n")
    file.write("=" * 50 + "\n")
    file.write("Name: "+ name + "\n")
    file.write("Registration Number: " +regno)
    file.write("Evaluated Password : " + password + "\n")
    file.write("Length             : " + str(length) + "\n")
    file.write("Uppercase Letters  : " + str(upper_count) + "\n")
    file.write("Lowercase Letters  : " + str(lower_count) + "\n")
    file.write("Numeric Digits     : " + str(digit_count) + "\n")
    file.write("Special Characters : " + str(special_count) + "\n")
    file.write("Score              : " + str(score) + "/" + str(max_score) + "\n")
    file.write("Strength Rating    : " + strength + "\n")
    file.write("Visual Meter       : " + visual_bar + "\n")
    if len(feedback) > 0:
        file.write("\nIssues & Feedback:\n")
        for tip in feedback:
            file.write(" - " + tip + "\n")
    else:
        file.write("\nStatus: Meets all requirements.\n")
        
    file.write("=" * 50 + "\n\n")
    file.close()
    print("[+] Report successfully saved to", file_name)
else:
    print("[-] Result was not saved.") 