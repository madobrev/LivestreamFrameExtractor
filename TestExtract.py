import subprocess
import os


def extract_frames(url, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    command = [
        'ffmpeg',
        '-i', url,
        '-vf', 'scale=640:480',
        f'{output_folder}/frame_%09d.jpg'
    ]

    subprocess.run(command)


def main():
    m3u8_url = "https://e115-ts.cdn.bg/nbg/nova/live/at=O0U9MTcwMTgzMTYyMztBPTE7Sz0xMTtQPTAxMTEwO1M9ODEyZGE1MWUzNDc5ZmUxODFmN2NjMjJjMTcyYTBhOGMzNDJjMTBjNQ==/in_nova/live_1080/chunks.m3u8"
    output_folder = "frames"

    extract_frames(m3u8_url, output_folder)


if __name__ == "__main__":
    main()
