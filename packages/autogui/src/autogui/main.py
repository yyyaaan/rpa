import argparse
from actions.actions import Actions

def main():
    """entry script"""
    # CLI arg
    parser = argparse.ArgumentParser(description="Spotify Automation Script")
    parser.add_argument("--delay", type=int, default=6, help="Default delay in seconds (default: 6)")
    parser.add_argument("--vision", action="store_true", help="Enable vision mode to 'see a little'")
    parser.add_argument("--debug", action="store_true", default=True, help="Enable debug printouts and screenshots")
    parser.add_argument("--playlist", type=str, default="Gostan parhaat", help="Name of the Spotify playlist to play")
    args = parser.parse_args()

    # 4. Pass arguments to your class and method
    Actions(
        delay=args.delay,
        vision_mode=args.vision,
        debug=args.debug
    ).play_spotify_playlist(
        playlist_name=args.playlist
    )

if __name__ == "__main__":
    main()
    