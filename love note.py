# Greet the user
input("hello there... :3")

# Display a personalized greeting
per_son = "cutie"
input("I love you, " + per_son + "!")

# Ask the question
user_reply = input("Do you feel the same way by chance...? y/n ^_^ ").lower()

# Check the reply
if user_reply in ["yes", "y", "affirmative"]:
    print(f"You're so sweet, {per_son} *hugs* >///< <3")
else:
    print("acknowledged... ._.")
    input("Press Enter to exit...")
