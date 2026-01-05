#!/usr/bin/env python3

import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame


def play_music(folder, song):

    song_path = os.path.join(folder, song)
    if not os.path.exists(song_path):
        print("File does not exist!")
        return
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play()

    print(f"\nNow Playing: {song}")
    print("Command [P]ause, [R]esume, Rewind [S]top: ")

    while True:
        command = input('> ').upper()
        if command == 'P':
            pygame.mixer.music.pause()
            print(f"Paued {song}")
        elif command == 'R':
            pygame.mixer.music.unpause()
            print(f"Resumed {song}")
        elif command == 'S':
            pygame.mixer.music.stop()
            print(f"Stopped {song}")
            return
        else:
            print("Enter a valid command!")




def main():

    try:
        pygame.mixer.init()
    except pygame.error as e:
        print(f"Audio initilization failed! {e}")

    folder = 'music'

    if not os.path.isdir(folder):
        print(f"Folder {folder} does not exist!")

    mp3_files = [music for music in os.listdir(folder) if music.endswith('.mp3')]

    if not mp3_files:
        print(f"No mp3 files found in {folder}!")

    while True:
        print("****** MP3 Player ******")
        print("My Song list:")
        for index, song in enumerate(mp3_files, start=1):
            print(f"{index}. {song}")
        choice_input = input("\nEnter song number to play (or 'Q' to quit): ")

        if choice_input.upper() == 'Q':
            print("Bye!")
            break

        if not choice_input.isdigit():
            print("Enter a valid number: ")
            continue

        choice = int(choice_input) - 1

        if 0 <= choice < len(mp3_files):
            play_music(folder=folder, song=mp3_files[choice])
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
