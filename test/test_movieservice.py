import os

from com.story.common.util import get_root_path
from com.story.movie.service.movieservice import MovieService

move_service = MovieService()


def remove_temp_files_in_directory(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            if ".mp" in file_path:
                os.remove(file_path)


# 기존파일 삭제
remove_temp_files_in_directory("{get_root_path()}/output")
remove_temp_files_in_directory("{get_root_path()}/upload")

subtitle = "안녕하세요, 파이썬으로 한글 TTS를 만들고 있습니다.\n안녕하세요, 파이썬으로 한글 TTS를 만들고 있습니다."
# subtitle = "hello. i am making korean TTS with python."
voice_file = move_service.make_tts(subtitle)
image_clip = move_service.make_scene(f"{get_root_path()}/resources/0.webp", 1)
movie_1 = move_service.merge_video(image_clip, voice_file, subtitle)
