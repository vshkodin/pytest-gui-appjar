import logging
from datetime import datetime


log = logging
log.basicConfig(format='%(asctime)s %(message)s',filename='guiLog.log', level=logging.INFO)
#logmessage=log.getLogger(__name__)
now = datetime.now()