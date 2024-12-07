import random
from googletrans import Translator

# Initialize the translator
translator = Translator()

# Sample phrases for the quiz
PHRASES = {
    "easy": ["Hello", "Thank you", "Good morning", "How are you?", "Yes", "No"],
    "medium": ["I love programming", "Where is the nearest station?", "What is your name?", "Nice to meet you"],
    "hard": ["The quick brown fox jumps over the lazy dog", "Do you believe in fate?", "Can you recommend a good restaurant?"],
}

LANGUAGES = {
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Italian": "it",
    "Chinese": "zh-cn",
}

def get_translation(phrase, target_language):
    """
    Translate a phrase to the target language.
    """
    try:
        translated = translator.translate(phrase, dest=target_language)
        return translated.text
    except Exception as e:
        print(f"Error during translation: {e}")
        return None

def play_quiz():
    """
    Play the language translation quiz.
    """
    print("Welcome to the Language Translation Quiz!")
    print("Choose a difficulty level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    # Select difficulty
    difficulty_choice = input("Enter your choice (1/2/3): ").strip()
    difficulty = { "1": "easy", "2": "medium", "3": "hard" }.get(difficulty_choice, "easy")
    phrases = PHRASES[difficulty]

    # Select language
    print("\nChoose a language for the translations:")
    for i, lang in enumerate(LANGUAGES.keys(), 1):
        print(f"{i}. {lang}")
    lang_choice = input("Enter your choice (1-5): ").strip()
    selected_language = list(LANGUAGES.values())[int(lang_choice) - 1]

    # Start quiz
    score = 0
    random.shuffle(phrases)
    for phrase in phrases[:5]:
        translated_text = get_translation(phrase, selected_language)
        if not translated_text:
            print("Skipping this phrase due to translation error.")
            continue

        print(f"\nTranslate this phrase into {list(LANGUAGES.keys())[int(lang_choice) - 1]}: {phrase}")
        user_answer = input("Your answer: ").strip()

        if user_answer.lower() == translated_text.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct translation is: {translated_text}")

    print(f"\nQuiz Complete! Your final score: {score}/{len(phrases[:5])}")

if __name__ == "__main__":
    play_quiz()
