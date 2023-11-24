import logging
from src.date_format import currentdatetime_str

file_name = f"my_log_{currentdatetime_str}.log"
file_path_name = f"/Users/demon/Documents/PycharmProjects/CRMbanking/logs/my_log_{currentdatetime_str}.log"
logging.basicConfig(
    filename=file_name, # encoding='utf-8',
    format="%(asctime)s [%(levelname)s]: %(message)s", level=logging.DEBUG
)
logger = logging.getLogger()