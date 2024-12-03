import os

from openai import OpenAI
from openai.types import Image

from com.story.config.logger_config import get_logger
from com.story.config.profile import active_profile

logger = get_logger()
profile = active_profile()

# gets API Key from environment variable OPENAI_API_KEY
os.environ["OPENAI_API_KEY"] = profile["gpt"]["token"]
client = OpenAI()


def generate_images(prompt: str, imageCount: int = 5) -> list[Image]:
    # 하나의 프롬프트 설정
    # prompt = "A serene fairytale forest at sunrise with mystical creatures and glowing flora"

    # 이미지 생성 (5개)
    return client.images.generate(
        prompt=prompt,
        n=imageCount,
        size="1024x1024"
    ).data

# # 각 이미지 다운로드 및 로컬 저장
# for i, data in enumerate(response.data):
#     # 이미지 URL 가져오기
#     image_url = data.url
#
#     # 이미지 다운로드
#     img_data = requests.get(image_url).content
#     img = Image.open(BytesIO(img_data))
#
#     # 이미지 저장
#     img.save(f"generated_image_{i + 1}.png")
#
#     print(f"Image {i + 1} saved as 'generated_image_{i + 1}.png'")
