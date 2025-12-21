# main.py

import os
from playsound import playsound

MUSIC_FOLDER = "music"

def list_songs():
    if not os.path.exists(MUSIC_FOLDER):
        os.makedirs(MUSIC_FOLDER)

    songs = [f for f in os.listdir(MUSIC_FOLDER)
             if f.lower().endswith((".mp3", ".wav"))]

    if not songs:
        print("No audio files found in the 'music' folder.")
        return []

    print("\n🎵 Available Songs:")
    for i, song in enumerate(songs, start=1):
        print(f"{i}. {song}")

    return songs

def play_song():
    songs = list_songs()
    if not songs:
        return

    choice = input("\nEnter song number to play: ")

    try:
        index = int(choice) - 1
        if 0 <= index < len(songs):
            filepath = os.path.join(MUSIC_FOLDER, songs[index])
            print(f"\n▶️ Playing: {songs[index]}")
            playsound(filepath)
            print("✅ Finished playing.")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        print("\n🎵 Music Player")
        print("1. List songs")
        print("2. Play a song")
        print("3. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            list_songs()
        elif choice == "2":
            play_song()
        elif choice == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
