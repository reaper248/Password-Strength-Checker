# Password Strength Checker

## PROJECT TITLE
Password Strength Checker

## ABOUT THE PROJECT
This is a simple Python program that checks how strong a password is. The user enters a password and the program looks at different things like its length, capital letters, small letters, numbers, and special characters.

It also checks for some common passwords, keyboard patterns, common names, and repeated characters. After checking everything, it gives the password a score out of 10 and shows a strength level such as `Weak`, `Moderate`, `Strong`, or `Very Strong`.

The program also gives suggestions when something is missing or easy to guess. If the user wants, the result can be saved in a text file for later use.

## MAIN FEATURES
- Checks the total length of the password.
- Counts uppercase and lowercase letters.
- Counts numbers and special characters.
- Checks if the password contains spaces.
- Checks for common passwords like `password`, `123456`, and `qwerty`.
- Checks for keyboard patterns like `asdfgh` and `zxcvbn`.
- Checks whether some common names are present in the password.
- Finds three or more same characters appearing continuously.
- Gives a security score from `0` to `10`.
- Shows a simple visual score using `#` and `-`.
- Gives suggestions based on the problems found in the password.
- Can save the final result in `saved_passwords.txt`.

## TECHNOLOGIES USED
- **Language:** Python 3
- **Module:** `os`
- **Concepts:** Strings, Lists, Loops, If-Else Statements, Boolean Variables, Counters, User Input and File Handling
- **Run Environment:** VS Code, PyCharm, Command Prompt, or any other Python-supported terminal/IDE

## HOW TO RUN

### Step 1
Make sure Python 3 is installed on your computer.

### Step 2
Save the program as:

```text
main.py
```

### Step 3
Open Command Prompt or Terminal and go to the folder where the file is saved.

```bash
cd path/to/your/folder
```

### Step 4
Run the program:

```bash
python main.py
```

## HOW TO TEST THE PROGRAM

### 1. Try a Strong Password
Enter a password with:
- At least 12 characters
- Uppercase letters
- Lowercase letters
- Numbers
- Special characters

Check the score and the strength shown by the program.

### 2. Try a Short Password
Enter a password with less than 8 characters.

The program should show that the password is too short.

### 3. Try Missing Characters
Try passwords that do not contain:
- Uppercase letters
- Lowercase letters
- Numbers
- Special characters

The program should tell you what needs to be added.

### 4. Try a Common Password
Try something containing:

```text
password
123456
qwerty
```

The program should show a warning because these patterns are easy to guess.

### 5. Try a Keyboard Pattern
Try a password containing patterns such as:

```text
qwerty
asdfgh
zxcvbn
```

A keyboard-pattern warning should appear.

### 6. Try a Common Name
Use one of the names checked by the program, for example:

```text
john
alex
david
emma
```

The program should warn that the password contains an easily guessable name.

### 7. Try Repeated Characters
Enter a password with three or more same characters together, for example:

```text
aaa
111
!!!
```

The program should detect the repeated characters.

### 8. Test Saving the Report
At the end of the program, it asks:

```text
Do you want to save this report to a file? (yes/no):
```

Enter:

```text
yes
```

The report will be added to:

```text
saved_passwords.txt
```

## OUTPUT
After checking the password, the program displays information like:

```text
Password Length
Uppercase Count
Lowercase Count
Digit Count
Special Char Count
Whitespace Count
Security Score
Score Visualizer
Strength Rating
Actionable Suggestions
```

The score is shown out of 10 and the program also gives a strength rating.

## SAVED REPORT
If the user chooses to save the result, the program creates or updates:

```text
saved_passwords.txt
```

The file contains the entered name, registration number, password details, score, strength rating, visual meter, and feedback.

## SCREENSHOTS
Screenshots of the program output can be added in this section.

## NOTE
This project is made for learning and demonstration purposes. The current version saves the evaluated password in the text report if the user chooses the save option. In a real password-security application, passwords should not be stored as plain text.
