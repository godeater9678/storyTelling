import asyncio
import base64
import os
from typing import Any

from openai import OpenAI
from openai.types import Image

from com.story.config.logger_config import get_logger
from com.story.config.profile import active_profile

logger = get_logger()
profile = active_profile()

# gets API Key from environment variable OPENAI_API_KEY
os.environ["OPENAI_API_KEY"] = base64.b64decode(profile["key1"]).decode('utf-8')
client = OpenAI()


async def generate_single_image(client, prompt: str) -> Image:
    """단일 이미지 생성"""
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    return response.data[0]


async def generate_images(prompt: str, imageCount: int = 5) -> tuple[Any]:
    """비동기로 여러 이미지를 생성"""
    tasks = []
    for _ in range(imageCount):
        tasks.append(generate_single_image(client, prompt))

    # 모든 태스크를 병렬로 실행
    images = await asyncio.gather(*tasks)
    return images

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
