import subprocess, re, os
from pytube import YouTube, Playlist
def combine_audio_and_video(video: str, audio: str):
    
    output_file_name = os.path.splitext(video)[0] + " .mp4"
    command = [
        "ffmpeg",
        "-i", video,
        "-i", audio,
        "-c:v", "copy",
        "-c:a", "copy",
        output_file_name
    ]
    subprocess.run(command)
    
def combine_audio_and_video_gpu(video_file, audio_file, output_file):
    command = [
        "ffmpeg",
        "-i", video_file,
        "-i", audio_file,
        "-c:v", "h264_nvenc",  # Use NVIDIA GPU-accelerated H.264 encoder
        "-c:a", "copy",
        output_file
    ]
    subprocess.run(command)
    
def sanitize_filename(filename):
    # Replace characters that might cause issues with underscores
    sanitized_filename = re.sub(r'[<>:"/\\|?*]', '', filename)
    return sanitized_filename


def check_is_playlist(link):
    if "playlist" in link: return True
    else: return False

