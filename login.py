# login.py
# Simple Login Function
# Author: Hema Keerthi Pati
# Branch: feature-login

# Predefined username and password
VALID_USERNAME = "hema"
VALID_PASSWORD = "hema@123"

def login(username, password):
    """
    Simple login function to validate
    username and password
    """
    if username == VALID_USERNAME and password == VALID_PASSWORD:
        print("✅ Login Successful! Welcome", username)
        return True
    else:
        print("❌ Login Failed! Invalid credentials")
        return False

# Main program
if __name__ == "__main__":
    print("===== Login System =====")
    username = input("Enter username: ")
    password = input("Enter password: ")
    login(username, password)