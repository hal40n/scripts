import os
import zipfile
import logging
from dotenv import load_dotenv
import time

log_dir = "./logs"
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, f"extract_backup_{time.strftime('%Y%m%d_%H%M%S')}.log")
logging.basicConfig(filename=log_file, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

load_dotenv()

# 計測開始
logging.info("Extraction Job Start!")
logging.info("Start Time: %s", time.strftime("%Y/%m/%d %H:%M:%S"))
start_time = time.time()

destination_file_path = os.getenv("DESTINATION_FILE_PATH")

logging.info("Unzip Start!")

for filename in os.listdir(destination_file_path):
    if filename.endswith(".zip"):
        zip_file_path = os.path.join(destination_file_path, filename)

        with zipfile.ZipFile(zip_file_path, "r") as zf:
            for info in zf.infolist():
                try:
                    info.filename = info.orig_filename.encode('cp437').decode('cp932')
                except UnicodeDecodeError:
                    pass
                if os.sep != "/" and os.sep in info.filename:
                    info.filename = info.filename.replace(os.sep, "/")

                zf.extract(info, path=destination_file_path)

        os.remove(zip_file_path)
        logging.info("Removed copied ZIP file: %s", zip_file_path)

logging.info("Unzip is OK!")

# 計測終了
end_time = time.time()
execution_time = end_time - start_time
logging.info("Script execution time: %.2f seconds", execution_time)
logging.info("End Time: %s", time.strftime("%Y/%m/%d %H:%M:%S"))
logging.info("Extraction Job Finished!")
