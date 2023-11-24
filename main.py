import os
from pytube import YouTube
import music_tag

def download_mp3(url: str, output_path: str):
    try:
        yt = YouTube(url)
        audio_stream  = yt.streams.filter(only_audio = True).first()

        if audio_stream is not None:
            audio_stream.download(output_path)
            audio_path = os.path.join(output_path, audio_stream.default_filename)
            audio_final_path = audio_path[:-4] + '.mp3'
            os.rename(audio_path, audio_final_path)

            print(f'Download complete! File {audio_final_path} at {output_path}')
            return audio_final_path
        else:
            raise Exception('The given url is not valid.')


    except Exception as e:
        print(f'An error occurred: {e}')

def format_metadata(audio_path: str):
    file = music_tag.load_file(audio_path)

    title = input('What is the title of the song? ')
    if title is not None:
        file['title'] = title
    artist = input('Who made this song? ')
    if artist is not None:
        file['artist'] = artist
    file.save()

    print('Done editing metadata.')

if __name__ == "__main__":
    video_url = input('Enter Youtube video url: ')
    output_dir = input('Enter output directory (press Enter for the current directory): ')
    if not output_dir:
        output_dir = os.getcwd()

    audio_path = download_mp3(video_url, output_dir)
    edit = input('Edit mp3 metadata? (y for yes) ')
    if edit == 'y':
        format_metadata(audio_path)
    else:
        print('cya')
