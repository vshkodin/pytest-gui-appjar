import logging
from datetime import datetime

GUI=True
Allure_GUI=False
log = logging
log.basicConfig(filename='myapp.log', level=logging.INFO)
now = datetime.now()