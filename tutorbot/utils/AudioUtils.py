from moviepy import VideoFileClip


def save_video_as_audio(video_path: str = None,
                        audio_output_path: str = None):
    
    clip = VideoFileClip(video_path)
    clip.audio.write_audiofile(audio_output_path)
