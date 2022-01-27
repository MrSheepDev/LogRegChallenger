class Prompts :
    @staticmethod
    def array_load_print():
        print("""
Before starting anything, you need to initialise arrays to initialise the logistic regression.
    1. Use the Challenger data arrays
    2. Enter a custom array (WIP)
    3. Use a basic test array
    0. Quit
""")

    @staticmethod
    def main_menu_prompt():
        print("""
---== Main menu ==---
    1. Show with visuals the confusion matrix
    2. Print the confusion matrix
    3. Print the coefs b0 and b1
    4. Print the predictions for things wip shit
    5. Print the probability matrix for a specific array
    6. Print the fiability of this model
    7. Print the classification report of this model
    0. Quit
""")

    @staticmethod
    def invalid_choice():
        print("Invalid choice. Please only enter the corresponding number of your choice.")

    @staticmethod
    def wip() :
        print("This function is unavailable at the moment. Work in progress ! (WIP)")