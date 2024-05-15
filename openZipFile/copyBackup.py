import os
import shutil
import logging
from dotenv import load_dotenv
import time

log_dir = "./logs"
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, f"copy_backup_{time.strftime('%Y%m%d_%H%M%S')}.log")
logging.basicConfig(filename=log_file, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

load_dotenv()

# 計測開始
logging.info("Copy Job Start!")
logging.info("Start Time: %s", time.strftime("%Y/%m/%d %H:%M:%S"))
start_time = time.time()

original_file_path = os.getenv("ORIGINAL_FILE_PATH")
destination_file_path = os.getenv("DESTINATION_FILE_PATH")

def get_latest_directory(path):
    dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    dirs.sort(key=lambda x: os.path.getmtime(os.path.join(path, x)), reverse=True)
    if dirs:
        return dirs[0]
    return None

latest_dir = get_latest_directory(original_file_path)

if latest_dir:
    logging.info("Latest directory to copy: %s", latest_dir)

    logging.info("Copy Start!")

    for filename in os.listdir(os.path.join(original_file_path, latest_dir)):
        if filename.endswith(".zip"):
            zip_file_path = os.path.join(original_file_path, latest_dir, filename)
            destination_zip_path = os.path.join(destination_file_path, filename)

            shutil.copy2(zip_file_path, destination_zip_path)
            logging.info("Copied ZIP file to: %s", destination_zip_path)
else:
    logging.warning("No directories found to copy.")

# 計測終了
end_time = time.time()
execution_time = end_time - start_time
logging.info("Script execution time: %.2f seconds", execution_time)
logging.info("End Time: %s", time.strftime("%Y/%m/%d %H:%M:%S"))
logging.info("Copy Job Finished!")
