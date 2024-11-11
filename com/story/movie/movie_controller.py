import os
import shutil
import traceback

from fastapi import APIRouter, FastAPI, Request, UploadFile, File, Form, Query
from starlette.responses import StreamingResponse

from fastapi.responses import HTMLResponse
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates

from com.story.common.util import get_root_path
from com.story.config.profile import active_profile

root_path = '/movie'
profile = active_profile()
templates = Jinja2Templates(directory=profile['template_dir'])
router = APIRouter()


@router.get(f"{root_path}", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("hana/index.html", {"request": request, "name": "FastAPI"})

# @router.post(f"{root_path}", response_class=HTMLResponse)
# def upload_file(request: Request, file: UploadFile = File(...), market: str = Form(...)):
#     file_location = f"{hanaCon.getRootPath()}/resources/upload/{file.filename}"
#     with open(file_location, "wb") as buffer:
#         shutil.copyfileobj(file.file, buffer)
#
#     downloadFile = ''
#     try:
#         if market == 'dome':
#             downloadFile = hanaCon.convertWonHwa(file.filename)
#         else:
#             downloadFile = hanaCon.convertForex(file.filename)
#     except Exception as e:
#         stack_trace = traceback.format_exc()
#         logger.error(f"An error occurred: {e}: {stack_trace}")
#         return f"서버에러 발생. 엑셀 형식을 확인하세요. : {e}"
#     file_name = os.path.basename(downloadFile)
#     return f" <a href='/hana/download?file={file_name}'>'[다운로드] {file_name}'</a> "
