songs = ["  yellow", "fix you   ", "  sparks", "love story   ", "   patutunguhan"]
print(f"\n{[song.strip() for song in songs]}")
print(f"\n{[song.strip().title() for song in songs]}")
final_songs = [song.strip().replace("yellow", "multo").title() for song in songs]
print(f"\n{final_songs}")

while True:
    print("\nDo you want to add a song?")
    choice = input("Enter: ")
    if choice.lower() == "yes":
        entry = input("\nEnter song: ")
        final_songs.append(entry)
    else:
        break

print(f"\n{final_songs}\n")
# we can either use final_songs = sorted(final_songs) then print, or use >>
final_songs.sort()
try:
    with open("playlist.txt", "w") as writer:
        for song in final_songs:
            writer.write(f"{song}\n")
except IOError:
    for _ in range(3):
        print("\nERROR")
finally:
    with open("playlist.txt", "r") as reader:
        print(reader.read())

print(len(final_songs))
print(final_songs[:3])
print(final_songs[-2:])