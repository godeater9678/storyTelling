import base64
import os

from openai import OpenAI

from com.story.config.logger_config import get_logger
from com.story.config.profile import active_profile

logger = get_logger()
profile = active_profile()
# gets API Key from environment variable OPENAI_API_KEY
os.environ["OPENAI_API_KEY"] = base64.b64decode(profile["key1"]).decode('utf-8')
client = OpenAI()


def generate_story(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-4o",  # 사용할 모델 지정
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1500,  # 결과의 최대 토큰 수 설정
            temperature=0.7  # 답변의 다양성 설정
        )
        # 응답 결과 추출
        answer = response.choices[0].message.content.strip()
        return answer
    except Exception as e:
        logger.error(f"Error occurred: {e}")
        return None
