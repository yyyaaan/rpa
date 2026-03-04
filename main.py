from actions.actions import Actions

if __name__ == "__main__":
    Actions(
        vision_mode=False,   # set true to "see a little"
        debug=True
    ).play_spotify_playlist(
        playlist_name="Gostan parhaat",
    )
