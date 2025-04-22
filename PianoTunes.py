# Work in progress - still needs to fix or give choice for tunning
# This script generates a melody from lyrics by mapping syllables to piano notes.
import random
from pydub import AudioSegment # <<<<Dependency to install - pip install pydub>>>>>
import numpy as np

# Frequency table for piano notes (for one octave, A4=440Hz)
note_frequencies = {
    "C4": 261.63, "C#4": 277.18, "D4": 293.66, "D#4": 311.13, "E4": 329.63, 
    "F4": 349.23, "F#4": 369.99, "G4": 392.00, "G#4": 415.30, "A4": 440.00, 
    "A#4": 466.16, "B4": 493.88, "C5": 523.25
}

# Function to generate a tone for a note
def generate_tone(note, duration_ms=500):
    # Frequency of the note
    freq = note_frequencies[note]
    
    # Sampling rate (samples per second)
    sample_rate = 44100
    # Duration in samples
    duration_samples = int(sample_rate * (duration_ms / 1000))
    
    # Generate the sound wave (sine wave) for the note
    t = np.linspace(0, duration_ms / 1000, duration_samples, endpoint=False)
    waveform = 0.5 * np.sin(2 * np.pi * freq * t)
    
    # Convert to 16-bit PCM format
    audio = np.int16(waveform * 32767)
    
    # Convert to AudioSegment
    tone = AudioSegment(
        audio.tobytes(), 
        frame_rate=sample_rate, 
        sample_width=2, 
        channels=1
    )
    
    return tone

# Simple function to map syllables to notes (simplified version)
def map_lyrics_to_notes(lyrics):
    syllables = lyrics.split()  # This is a basic split; you can use more complex NLP to get syllables.
    
    notes = []
    for syllable in syllables:
        # Randomly choose a note for each syllable
        note = random.choice(list(note_frequencies.keys()))
        notes.append(note)
    
    return notes

# Create the melody for the lyrics
def create_melody(filename):
    with open(filename, 'r') as file:
        lyrics = file.read()
    notes = map_lyrics_to_notes(lyrics)
    melody = AudioSegment.silent(duration=0)
    
    # Generate tones for each note and append them to the melody
    for note in notes:
        tone = generate_tone(note, duration_ms=500)
        melody += tone
    
    return melody

# Save the melody to a file
def save_melody(melody, filename="melody.wav"):
    melody.export(filename, format="wav")
    print(f"Melody saved to {filename}")


def main():

    # Create melody from lyrics
    melody = create_melody("lyrics.txt")
    print("Melody created from lyrics")

    # Save the melody to a file
    save_melody(melody)

if __name__ == "__main__":
    main()
