import logging
from logging.handlers import TimedRotatingFileHandler

import com.story.common.util as util


def get_logger():
    mylogger = logging.getLogger("common")
    if mylogger.hasHandlers():
        return mylogger

    mylogger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # 콘솔 핸들러
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    mylogger.addHandler(stream_handler)

    # 파일 핸들러 (시간 단위로 로테이션)
    project_path = util.get_root_path()
    file_handler = TimedRotatingFileHandler(
        filename=f'{project_path}/logs/logger.log',
        when='H',  # 시간 단위로 로테이션
        interval=1,  # 1시간마다 로테이션
        backupCount=24,  # 보관할 백업 로그 파일의 최대 개수
        encoding='utf-8'  # 파일 인코딩 설정
    )
    file_handler.setFormatter(formatter)
    mylogger.addHandler(file_handler)

    return mylogger
