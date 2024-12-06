import asyncio
import os
import shutil

from fastapi import File, UploadFile, Form, APIRouter
from moviepy.audio.io.AudioFileClip import AudioFileClip
from starlette.responses import StreamingResponse

from com.story.common.util import get_root_path
from com.story.config.profile import active_profile
from com.story.dto.CommonResponse import CommonResponse
from com.story.movie.service.imageService import generate_images
from com.story.movie.service.movieService import MovieService
from com.story.movie.service.storyService import generate_story
from com.story.movie.service.voiceService import get_voice

root_path = '/movie'
profile = active_profile()
# templates = Jinja2Templates(directory=profile['template_dir'])
router = APIRouter()

movieService = MovieService()


@router.post(f"{root_path}/movie/compose", response_description="파일 스트림을 반환합니다. 반환된 스트림을 클라이언트에서 파일로 저장하세요.")
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
    voiceClip = AudioFileClip(file_path_voice)
    imageClip = movieService.make_image_to_imageClip(file_path_bg, 3)
    compositeVideoClip = movieService.add_subtitle(imageClip, subtitle)
    resultFilePath = movieService.add_audioClip(compositeVideoClip.to_ImageClip(), voiceClip)

    file_stream = open(resultFilePath, "rb")
    return StreamingResponse(file_stream, media_type="video/mp4")


@router.post(f"{root_path}/story")
def story(prompt):
    data = generate_story(prompt)
    return CommonResponse(data, 200 if data is not None else 500)


@router.post(f"{root_path}/images")
def image(prompt, imageCount: int = 5):
    data = asyncio.run(generate_images(prompt, imageCount))
    return CommonResponse(data, 200 if data is not None else 500)


@router.post(f"{root_path}/voice")
def image(text, voice_id='ZcZcEsYxXAIc3nNSev1H'):
    file = get_voice(text, voice_id=voice_id)
    file_stream = open(file, "rb")
    return StreamingResponse(file_stream, media_type="audio/mp3")
