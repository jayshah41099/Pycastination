import speech_recognition as sr
import sys

def speech_to_text(duration):
    recognizer = sr.Recognizer()

    # Use the default system microphone as the audio source
    with sr.Microphone() as source:
        print(f"Please speak. Recording for {duration} seconds...")
        audio_data = recognizer.listen(source, timeout=duration)

    # Convert audio to text
    try:
        text = recognizer.recognize_google(audio_data)
        return text
    except sr.UnknownValueError:
        return "Speech recognition could not understand audio"
    except sr.RequestError:
        return "Speech recognition service is unavailable"

def save_text_to_file(text, filename='AudioFile.txt'):
    with open(filename, 'w') as file:
        file.write(text)
    print(f"Text saved to {filename}")

def main():
    # Run the speech-to-text conversion and save the text to a file

    duration = sys.argv[1]
    Text = speech_to_text(duration)
    save_text_to_file(Text)

if __name__ == "__main__":
    main()


