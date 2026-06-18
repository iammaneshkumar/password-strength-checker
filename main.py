def check_length(password):
    return len(password) >= 8


def check_upper(password):
    for ch in password:
        if ch.isupper():
            return True
    return False


def check_lower(password):
    for ch in password:
        if ch.islower():
            return True
    return False


def check_digit(password):
    for ch in password:
        if ch.isdigit():
            return True
    return False


def check_special(password):
    for ch in password:
        if not ch.isalnum():
            return True
    return False


def calculate_score(password):
    score = 0

    if check_length(password):
        score += 1
    if check_upper(password):
        score += 1
    if check_lower(password):
        score += 1
    if check_digit(password):
        score += 1
    if check_special(password):
        score += 1

    return score


def get_strength(score):
    if score <= 2:
        return "WEAK"
    elif score <= 4:
        return "MEDIUM"
    else:
        return "STRONG"


def show_report(password):
    score = calculate_score(password)
    strength = get_strength(score)

    print("\n==============================")
    print("   PASSWORD SECURITY REPORT")
    print("==============================\n")

    print("Password Length :", len(password))
    print("Uppercase       :", "Yes" if check_upper(password) else "No")
    print("Lowercase       :", "Yes" if check_lower(password) else "No")
    print("Digits          :", "Yes" if check_digit(password) else "No")
    print("Special Char    :", "Yes" if check_special(password) else "No")

    print("\nScore           :", f"{score}/5")
    print("Strength        :", strength)
    print("\n==============================\n")


# MAIN
password = input("Enter your password: ")
show_report(password)