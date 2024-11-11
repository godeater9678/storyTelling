import os
import shutil

from fastapi import File, UploadFile, Form, APIRouter
from fastapi.responses import FileResponse
from starlette.responses import StreamingResponse

from com.story.config.profile import active_profile
root_path = '/movie'
profile = active_profile()
# templates = Jinja2Templates(directory=profile['template_dir'])
router = APIRouter()

from com.story.common.util import get_root_path
from com.story.movie.service.movieservice import MovieService

move_service = MovieService()

@router.post("/process/")
async def process_files(
        subtitle: str = Form(...),
        voice: UploadFile = File(...),
        bg_image: UploadFile = File(...)
):
    save_directory = f"{get_root_path()}/upload"
    file_path_voice = os.path.join(save_directory, voice.filename)
    file_path_bg = os.path.join(save_directory, bg_image.filename)
    # 파일을 로컬에 저장
    with open(file_path_voice, "wb") as buffer:
        shutil.copyfileobj(voice.file, buffer)
    with open(file_path_bg, "wb") as buffer:
        shutil.copyfileobj(bg_image.file, buffer)

    # subtitle = "hello. i am making korean TTS with python."
    #voice_file = move_service.make_tts(subtitle)
    image_clip = move_service.make_scene(f"{file_path_bg}", 1)
    video_path = move_service.merge_video(image_clip, file_path_voice, subtitle)

    file_stream = open(video_path, "rb")
    return StreamingResponse(file_stream, media_type="video/mp4")
