from lib.tools.log import log
import shutil


def clean_report():
    try:
        shutil.rmtree('reports/')
        log.info(f'reports directory deleted')
    except:
        log.info(f'reports directory folder not found')