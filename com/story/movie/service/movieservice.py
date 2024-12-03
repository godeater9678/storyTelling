import platform
from datetime import datetime

from gtts import gTTS
from moviepy.editor import ImageClip, AudioFileClip, TextClip, CompositeVideoClip

from com.story.common.util import get_root_path
from com.story.config.logger_config import get_logger
from com.story.config.profile import active_profile

logger = get_logger()
profile = active_profile()
output_path = get_root_path() + profile['output']['path']
scene_path = get_root_path() + profile['output']['scene_path']
tts_path = get_root_path() + profile['output']['tts_path']


class MovieService:
    fps: int = 24

    def image_to_movie(self):
        return None

    def make_tts(self, text):
        file_name = f"{tts_path}/{self.random_name()}.mp3"
        language = 'ko'
        # TTS 객체 생성
        tts = gTTS(text=text, lang=language, slow=False)
        tts.save(file_name)

        print(f"음성 파일이 {file_name}로 저장되었습니다.")
        return file_name

    def make_image_to_imageClip(self, str_image_path, seconds) -> ImageClip:
        str_output_path = f"{scene_path}/{self.random_name()}.mp4"

        # 이미지 파일을 불러와서 지정된 시간 동안 재생되는 클립을 생성합니다
        image_clip = ImageClip(str_image_path, duration=seconds)
        image_clip.fps = self.fps

        # 비디오 파일로 저장합니다
        image_clip.write_videofile(str_output_path)

        print("이미지가 성공적으로 동영상으로 저장되었습니다.")

        return image_clip

    def add_audioClip(self, video_clip: ImageClip, audio_clip: AudioFileClip) -> str:
        # Set duration if not set, using the audio's duration
        if not video_clip.duration:
            video_clip = video_clip.set_duration(audio_clip.duration)

        # Merge audio with the video
        video_with_audio = video_clip.set_audio(audio_clip)

        # Optional: Save to file
        str_output_path = f"{output_path}/{self.random_name()}.mp4"
        video_with_audio.write_videofile(str_output_path, codec='libx264', audio_codec='aac', fps=self.fps)

        return str_output_path

    def add_subtitle(self, video_clip: ImageClip, subtitle_text: str) -> CompositeVideoClip:
        font_path = None
        if platform.system() == "Windows":
            font_path = "C:/Windows/Fonts/malgun.ttf"
        else:
            font_path = f"{get_root_path()}/resources/fonts/AppleSDGothicNeo.ttc"
        subtitle = TextClip(subtitle_text, fontsize=30, color='white', font=font_path)
        subtitle = subtitle.set_position(
            ("center", video_clip.size[1] - 100)).set_duration(
            video_clip.duration).set_start(0)

        # 자막을 포함한 영상 생성
        #str_result_path = f"{output_path}/result-{self.random_name()}.mp4"
        final_video = CompositeVideoClip([video_clip, subtitle])
        #final_video.write_videofile(str_result_path, codec="libx264", fps=24)

        return final_video

    # def merge_video(self, video_clip: ImageClip, audio_clip: AudioFileClip, subtitle_text):
    #     # 출력 파일 경로를 설정합니다
    #     str_output_path = f"{output_path}/{self.random_name()}.mp4"
    #     str_result_path = f"{output_path}/result-{self.random_name()}.mp4"
    #
    #     # 오디오 파일을 영상에 추가합니다
    #     video_with_audio = video_clip.set_audio(audio_clip)
    #     video_with_audio.write_videofile(str_output_path, codec='libx264',
    #                                      audio_codec='aac', fps=24)
    #
    #     # 자막 클립 생성 (영상의 전체 길이로 설정)
    #     font_path = None
    #     if platform.system() == "Windows":
    #         font_path = "C:/Windows/Fonts/malgun.ttf"
    #     else:
    #         font_path = f"{get_root_path()}/resources/NanumMyeongjo.ttf"
    #     subtitle = TextClip(subtitle_text, fontsize=30, color='white', font=font_path)
    #     subtitle = subtitle.set_position(
    #         ("center", video_with_audio.size[1] - 100)).set_duration(
    #         video_with_audio.duration).set_start(0)
    #
    #     # 자막을 포함한 최종 영상 생성
    #     final_video = CompositeVideoClip([video_with_audio, subtitle])
    #     final_video.write_videofile(str_result_path, codec="libx264", fps=24)
    #
    #     print("영상과 오디오가 성공적으로 합쳐졌습니다.")
    #     return str_result_path

    def random_name(self):
        # 현재 시간을 가져와서 원하는 형식으로 변환합니다
        current_time = datetime.now()
        str_formatted_time = current_time.strftime("%Y%m%d%H%M%S%f")[
                             :-3]  # 밀리초까지만 유지
        return str_formatted_time
