import os
from pytube import YouTube

def download_mp3(url: str, output_path: str) -> None:
    try:
        yt = YouTube(url)
        audio_stream  = yt.streams.filter(only_audio = True).first()

        if audio_stream is not None:
            audio_stream.download(output_path)
            audio_path = os.path.join(output_path, audio_stream.default_filename)
            audio_rename = audio_path[:-4] + '.mp3'
            os.rename(audio_path, audio_rename)

            print(f'Download complete! File {audio_rename} at {output_path}')
        else:
            raise Exception('The given url is not valid.')


    except Exception as e:
        print(f'An error occurred: {e}')

if __name__ == "__main__":
    video_url = input('Enter Youtube video url: ')
    output_dir = input('Enter output directory (press Enter for the current directory): ')

    if not output_dir:
        output_dir = os.getcwd()
    download_mp3(video_url, output_dir)
