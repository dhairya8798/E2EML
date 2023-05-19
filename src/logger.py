import logging
import os
from datetime import datetime

logfile = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logspath = os.path.join(os.getcwd(), "logs", logfile)
os.makedirs(logspath, exist_ok=True)

logfilepath = os.path.join(logspath, logfile)

logging.basicConfig(
    filename = logfilepath,
    format = "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO,
)