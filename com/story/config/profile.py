import argparse
import json
import os
from pathlib import Path

from com.story.config.logger_config import get_logger

# 로거 설정
logger = get_logger()
__server_profile = None


def __load_config(profile):
    current_file_path = Path(__file__).resolve().parent
    config_file = f"{current_file_path}/profile-{profile}.json"
    with open(config_file, 'r') as f:
        config = json.load(f)
    return config


def active_profile():
    global __server_profile
    if __server_profile is None:
        parser = argparse.ArgumentParser(description="Example script.")
        # parser.add_argument("param1", type=str, help="First parameter")
        # parser.add_argument("param2", type=int, help="Second parameter")
        parser.add_argument("--profile", type=str, default="local", help="Optional parameter")

        args = parser.parse_args()
        logger.info(f"parameter profile: {args.profile}")

        # 파라미터와 환경 변수로 프로파일 설정
        active_profile = args.profile if args.profile else os.getenv('ACTIVE_PROFILE')

        # 기본 프로파일 설정
        if not active_profile:
            active_profile = 'dev'

        print(f"Active Profile: {active_profile}")
        __server_profile = __load_config(active_profile)
    return __server_profile
