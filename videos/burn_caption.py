import subprocess
import os

def burn_subtitles(video_path, srt_relative_path, output_path, ffmpeg_path):
    # Obtém os caminhos absolutos do vídeo e da saída
    video_full = os.path.abspath(video_path)
    output_full = os.path.abspath(output_path)

    # Usa o caminho relativo para as legendas exatamente como no comando manual
    # Certifique-se de que ffmpeg_path está no diretório correto
    command = f"{ffmpeg_path} -i \"{video_full}\" -vf \"subtitles={srt_relative_path}\" \"{output_full}\""

    print("Running command:")
    print(command)

    try:
        subprocess.run(command, shell=True, check=True)
        print(f"✅ Video with burned-in captions generated: {output_full}")
    except subprocess.CalledProcessError as e:
        print(f"[!] Error burning subtitles: {e}")

if __name__ == "__main__":
    # Caminho do executável do FFmpeg
    ffmpeg_path = "ffmpeg"  # Certifique-se de que está no PATH ou forneça o caminho absoluto

    # Caminhos dos arquivos
    video_file = "videos/video.mp4"  # Nome correto do arquivo
    srt_relative_path = "captions/output.srt"  # Arquivo SRT com legendas
    output_video = "videos/output_video.mp4"  # Arquivo de saída do vídeo com legendas

    # Chama a função para queimar legendas no vídeo
    burn_subtitles(video_file, srt_relative_path, output_video, ffmpeg_path)
