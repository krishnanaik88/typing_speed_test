from TySpeed import TySpeed
from Database import Database
class TypingApp:
    def __init__(self):
        self.user_id = None
        self.username = None
        self.typing_test = TySpeed.TypingSpeedTest()
        self.db_manager = Database.DatabaseManager()

    def authenticate_user(self):
        while True:
            username = input("Enter your username: ")
            user = self.db_manager.user_exists(username)

            if user:
                print("User found. Logging you in...\n")
                self.user_id = user[0]
                self.username = username
                break
            else:
                print("User not found. Please sign up.\n")
                choice = input("Do you want to sign up? (yes/no): ").lower()
                if choice == "yes":
                    self.user_id = self.db_manager.create_user(username)
                    self.username = username
                    print("Sign-up successful. You are now logged in.\n")
                    break

    def view_test_history(self):
        history = self.db_manager.get_test_history(self.user_id)
        if not history:
            print(f"\nNo test history available for {self.username}.\n")
            return

        print(f"\nTyping Test History for {self.username}:")
        for idx, (test_date, accuracy, speed) in enumerate(history, start=1):
            print(f"{idx}. Date: {test_date}, Accuracy: {accuracy:.2f}%, WPM: {speed:.2f}")
        print()

    def run(self):
        while True:
            self.authenticate_user()
            while True:
                print("Typing Speed Test Menu:")
                print("1. Start Typing Test")
                print("2. View Test History")
                print("3. Log Out")
                print("4. Exit")
                choice = input("Enter your choice (1/2/3/4): ")

                if choice == "1":
                    difficulty = input("Choose difficulty (easy/medium/hard): ").lower()
                    result = self.typing_test.start_test(difficulty)
                    if result:
                        self.db_manager.save_test_result(self.user_id, result)
                elif choice == "2":
                    self.view_test_history()
                elif choice == "3":
                    print("Logging out...\n")
                    break
                elif choice == "4":
                    print("Exiting Typing Speed Test. Goodbye!")
                    return
                else:
                    print("Invalid choice. Please select a valid option.\n")