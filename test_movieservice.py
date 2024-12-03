import os

from moviepy.audio.io.AudioFileClip import AudioFileClip

from com.story.common.util import get_root_path
from com.story.movie.service.movieservice import MovieService

movie_service = MovieService()


def remove_temp_files_in_directory(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            if ".mp" in file_path:
                os.remove(file_path)


# 기존파일 삭제
remove_temp_files_in_directory(f"{get_root_path()}/output")
remove_temp_files_in_directory(f"{get_root_path()}/upload")

subtitle = "동화에서 목소리 생성을 TTS로 하고자 할때 사용하는 목소리입니다."
voiceClip = AudioFileClip(movie_service.make_tts(subtitle))
imageClip = movie_service.make_image_to_imageClip(f"{get_root_path()}/resources/0.webp", 3)
compositeVideoClip = movie_service.add_subtitle(imageClip, subtitle)
resultPath = movie_service.add_audioClip(compositeVideoClip.to_ImageClip(), voiceClip)

print(resultPath)

