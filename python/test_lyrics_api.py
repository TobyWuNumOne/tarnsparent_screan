from lrclib import LrcLibAPI

# Create an instance of the API
api = LrcLibAPI(user_agent="my-app/0.0.1")

# Get lyrics for a track
lyrics = api.get_lyrics(
    track_name="I Want to Live",
    artist_name="Borislav Slavov",
    album_name="Baldur's Gate 3 (Original Game Soundtrack)",
    duration=233,
)

found_lyrics = lyrics.synced_lyrics or lyrics.plain_lyrics
print(type(lyrics))
print(lyrics.track_name)
print(lyrics)
print("\n".join(found_lyrics.split("\n")[:10]))
