import os

import uvicorn
from fastapi import FastAPI

from com.story.common.util import get_root_path
from com.story.movie.movie_controller import router as movie_router
from com.story.config.logger_config import get_logger
from com.story.config.profile import active_profile

# 로거 설정
logger = get_logger()

# FastAPI 앱 생성 및 라우터 포함
app = FastAPI()
app.include_router(movie_router)


# 서버를 실행하는 함수
def run_server():
    profile = active_profile()
    # logger.info(profile)  # 필요 시 로깅 활성화
    port = profile['server']['port']
    uvicorn.run(app, host="0.0.0.0", port=port)


# 이 스크립트가 직접 실행될 때만 서버 실행
if __name__ == "__main__":
    run_server()


def remove_temp_files_in_directory(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            if ".mp" in file_path:
                os.remove(file_path)


remove_temp_files_in_directory(f"{get_root_path()}/output")
remove_temp_files_in_directory(f"{get_root_path()}/upload")
