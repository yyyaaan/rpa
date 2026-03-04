from actions.actions import Actions

if __name__ == "__main__":
    Actions(
        vision_mode=False,
        debug=True
    ).play_spotify_playlist(
        playlist_name="Gostan parhaat",
    )
