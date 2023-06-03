import time

def SpeedTypingTest():
    text = "The quick brown fox jumps over the lazy dog."
    print("Type the following text:\n")
    print(text)
    print("\nPress Enter when you are ready to start.")
    input()

    start = time.time()

    typed = input("Start typing: ")

    end_time = time.time()
    elapsed_time = end_time - start

    words = len(typed.split())
    characters = len(typed)

    typing_speed = characters / elapsed_time
    accuracy = calculate_accuracy(text, typed)

    print("\n--- Results ---")
    print(f"Time taken: {elapsed_time:.2f} seconds")
    print(f"Typed words: {words}")
    print(f"Typed characters: {characters}")
    print(f"Typing speed: {typing_speed:.2f} characters per second")
    print(f"Accuracy: {accuracy:.2f}%")

def calculate_accuracy(original, typed):
    correct_characters = 0
    for i in range(len(original)):
        if i >= len(typed):
            break
        if original[i] == typed[i]:
            correct_characters += 1
    
    acc = (correct_characters / len(original)) * 100
    return acc

SpeedTypingTest()
