import time
class TypingSpeedTest:
    def __init__(self):
        self.test_texts = {
            "easy": "Python is fun.",
            "medium": "Object-oriented programming improves code reusability.",
            "hard": "Typing speed is a measure of how fast one can type correctly."
        }

    def start_test(self, difficulty):
        if difficulty not in self.test_texts:
            print("Invalid difficulty level. Choose 'easy', 'medium', or 'hard'.\n")
            return None

        print(f"\nTyping Test ({difficulty.capitalize()} Level):")
        test_text = self.test_texts[difficulty]
        print(f"\nType the following text:\n\n{test_text}\n")

        input("Press Enter when you are ready to start...\n")
        start_time = time.time()
        typed_text = input("Start typing here: ")
        end_time = time.time()

        elapsed_time = end_time - start_time
        return self.calculate_results(test_text, typed_text, elapsed_time, difficulty)

    def calculate_results(self, original_text, typed_text, elapsed_time, difficulty):
        words_in_original = len(original_text.split())
        words_typed = len(typed_text.split())
        words_per_minute = (words_typed / elapsed_time) * 60

        correct_words = sum(1 for o, t in zip(original_text.split(), typed_text.split()) if o == t)
        accuracy = (correct_words / words_in_original) * 100

        print("\nTest Results:")
        print(f"Time Taken: {elapsed_time:.2f} seconds")
        print(f"Words Per Minute (WPM): {words_per_minute:.2f}")
        print(f"Accuracy: {accuracy:.2f}%\n")

        return {"difficulty": difficulty, "wpm": words_per_minute, "accuracy": accuracy}
