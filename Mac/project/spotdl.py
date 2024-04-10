import ssl, os
from function import combine_audio_and_video, check_is_playlist
ssl._create_default_https_context = ssl._create_stdlib_context
from pytube import YouTube
from pytube import Playlist

print("Please specify  'URL TYPE IN 1st ROW on url.txt File'",
      "\n    0 = video ",
      "\n    1 = playlist\n")

path = os.getcwd()
path = os.path.dirname(path)
with open(os.path.join(path, 'project/url.txt')) as file: url = file.readlines()
IS_PLAYLIST = bool(int(url[0]) == 1)
del url[0]
for i in url:
    if check_is_playlist(i):
        p = Playlist(i)
        for num, yt in enumerate(p.videos):
            video = yt.streams.filter(adaptive=True).filter(mime_type='video/webm').first()
            audio = yt.streams.filter(only_audio=True).all()
            print(f'Downloading {video.title} {yt} {num + 1} / {len(p.videos)}')
            
            # video_fileN, audio_fileN = sanitize_filename(f'{video.title}.webm'), sanitize_filename(f'{audio[0].title}.mp4')

            title_path = os.path.join(path, 'download', p.title)
            audio_f_path = audio[0].download(output_path= title_path)
            video_f_path = video.download(output_path= title_path)
            combine_audio_and_video(video_f_path, audio_f_path)
            os.remove(audio_f_path)
            os.remove(video_f_path)

    else:
        yt = YouTube(i)
        print(f'Downloading {yt.title} {yt}')
        video = yt.streams.filter(adaptive=True).filter(mime_type='video/webm').first()
        audio = yt.streams.filter(only_audio=True).all()

        title_path = os.path.join(path, 'download')
        audio_f_path = audio[0].download(output_path=title_path)
        video_f_path = video.download(output_path=title_path)
        combine_audio_and_video(video_f_path, audio_f_path)
        os.remove(audio_f_path)
        os.remove(video_f_path)
