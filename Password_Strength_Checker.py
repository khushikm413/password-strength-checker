import re

def check_password_strength(password):
    strength = 0
    feedback = []
    
    # Length Check
    if len(password) >= 12:
        strength += 2
    elif len(password) >= 8:
        strength += 1
    else:
        feedback.append("Use at least 12 characters for a stronger password.")
    
    # Upper and Lowercase Check
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Mix uppercase and lowercase letters.")
    
    # Digits Check
    if re.search(r'\d', password):
        strength += 1
    else:
        feedback.append("Include at least one number.")
    
    # Special Characters Check
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    else:
        feedback.append("Add special characters (!@#$%^&* etc.) for better security.")
    
    # Common Password Check
    common_passwords = ["123456", "password", "qwerty", "abc123", "letmein", "123456789"]
    if password.lower() in common_passwords:
        strength = 0
        feedback = ["Avoid using common passwords."]
    
    # Strength Rating
    strength_levels = {0: "Very Weak", 1: "Weak", 2: "Moderate", 3: "Strong", 4: "Very Strong", 5: "Excellent"}
    
    return {
        "strength": strength_levels.get(strength, "Unknown"),
        "feedback": feedback
    }

# Example Usage
password = input("Enter a password: ")
result = check_password_strength(password)
print(f"Strength: {result['strength']}")
if result['feedback']:
    print("Suggestions:")
    for tip in result['feedback']:
        print(f"- {tip}")
