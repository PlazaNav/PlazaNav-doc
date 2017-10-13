import os
def ask_question(self, question):
    while True:
        choice = input("%s (y/N)" % question)
        choice = choice.lower()
        if choice == '' or choice == 'n':
            return False
        elif choice == 'y':
            return True
