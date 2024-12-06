import base64
from datetime import datetime

from com.story.common.util import get_root_path
from com.story.config.logger_config import get_logger
from com.story.config.profile import active_profile

logger = get_logger()
profile = active_profile()
output_path = get_root_path() + profile['output']['path']

from elevenlabs import save, Voice
from elevenlabs.client import ElevenLabs

# ElevenLabs API 키로 클라이언트 설정
client = ElevenLabs(
    api_key=base64.b64decode(profile["key2"]).decode('utf-8'),  # Defaults to ELEVEN_API_KEY
)


def get_voice(text, voice_id) -> str:
    # Voice 객체 생성
    voice = Voice(voice_id=voice_id)
    audio = client.generate(
        text=text,
        voice=voice,
        model="eleven_multilingual_v2"
    )
    # 오디오를 MP3 파일로 저장
    output_mp3_path = f"{output_path}/{datetime.now().strftime('%Y%m%d%H%M%S%f')}.mp3"
    save(audio, output_mp3_path)

    return output_mp3_path
