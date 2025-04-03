from moviepy.editor import VideoFileClip
import os

def extract_audio(video_path,output_audio_path):
    try:
        video = VideoFileClip(video_path)
        audio = video.audio
        if audio:
            audio.write_audiofile(output_audio_path)
            print(f'audio extraido com sucesso: {output_audio_path}')
        else:
            print(f'no audio')
    except Exception as e:
        print(f'Erro para extrair audio: {e}')

if __name__ == '__main__':
    video_file = "videos/video.mp4"
    audio_output = "audio/sample_audio.wav"

    os.makedirs(os.path.dirname(audio_output), exist_ok=True)

    extract_audio(video_file,audio_output)