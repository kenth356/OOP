songs = ["yellow  ", " fix you", "kyusi  ", "patutunguhan   ", "  oNLY"]
songs_cleaned = []
for song in songs:
    song_receiver = song.strip().replace("yellow", "marilag").title()
    songs_cleaned.append(song_receiver)

while True:
    print("\nDo you want to add a song?")
    choice = input("Enter: ")
    if choice.lower() == "yes":
        additional_song = input("\nEnter song: ")
        songs_cleaned.append(additional_song)
    else:
        break

songs_cleaned.sort()
songs_in_strings = "\n".join(songs_cleaned)

try:
    with open("playlist.txt", "w") as writer:
        writer.write(songs_in_strings)
except Exception as e:
    print("\n[ERROR]", e)
finally:
    with open("playlist.txt", "r") as reader:
        print("\n[PLAYLIST]")
        print(reader.read())

print(f"\nnumber of songs: {len(songs_cleaned)}")
print(f"first 3 songs: {songs_cleaned[:3]}")
print(f"last 2 songs: {songs_cleaned[-2:]}")