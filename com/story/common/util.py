import os
import unicodedata


def get_root_path():
    # 현재 파일의 디렉토리 경로
    current_dir = os.path.dirname(os.path.abspath(__file__))
    while True:
        # tor_processes.py 경로 확인
        main_py_path = os.path.join(current_dir, 'requirements.txt')
        if os.path.isfile(main_py_path):
            return os.path.dirname(main_py_path)
        # 상위 폴더로 이동
        parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
        # 더 이상 상위 폴더가 없을 경우 종료
        if current_dir == parent_dir:
            raise FileNotFoundError("requirements.txt 파일을 찾을 수 없습니다.")
        current_dir = parent_dir


# 디렉토리 내 모든 파일 이름을 NFC 형식으로 변환
def normalize_filenames(directory):
    for filename in os.listdir(directory):
        nfc_filename = unicodedata.normalize('NFC', filename)
        if filename != nfc_filename:
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, nfc_filename)
            os.rename(old_path, new_path)
            # print(f'Renamed: {filename} -> {nfc_filename}')
