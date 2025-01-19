import os
import time
import shutil
import subprocess

# Constants
WATCH_FOLDER = r"C:\Users\PC\Pictures\captured_pictures" 
UPLOADED_FOLDER = r"C:\Users\PC\Pictures\uploaded_pictures" 
UPLOAD_URL = "https://projects.benax.rw/f/o/r/e/a/c/h/p/r/o/j/e/c/t/s/4e8d42b606f70fa9d39741a93ed0356c/iot_testing_202501/upload.php"
UPLOAD_INTERVAL = 30 

SUPPORTED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff"}


os.makedirs(WATCH_FOLDER, exist_ok=True)
os.makedirs(UPLOADED_FOLDER, exist_ok=True)

def upload_picture(file_path):
 
    try:
        response = subprocess.run(
            ["curl", "-X", "POST", "-F", f"imageFile=@{file_path}", UPLOAD_URL],
            capture_output=True,
            text=True
        )
        if response.returncode == 0:
            print(f"Upload successful for: {file_path}")
            return True
        else:
            print(f"Upload failed for: {file_path}\nError: {response.stderr}")
            return False
    except Exception as e:
        print(f"An error occurred while uploading {file_path}: {e}")
        return False

def monitor_folder():
    print(f"Monitoring folder: {WATCH_FOLDER}...")
    while True:
        files = [f for f in os.listdir(WATCH_FOLDER) if os.path.isfile(os.path.join(WATCH_FOLDER, f))]
        
        if files:
            for file_name in files:
                file_path = os.path.join(WATCH_FOLDER, file_name)
            
                _, ext = os.path.splitext(file_name)
                if ext.lower() not in SUPPORTED_EXTENSIONS:
                    print(f"Skipping unsupported file: {file_name}")
                    continue
                
                print(f"Detected new file: {file_name}")
                if upload_picture(file_path):
                    destination = os.path.join(UPLOADED_FOLDER, file_name)
                    shutil.move(file_path, destination)
                    print(f"Moved {file_name} to {UPLOADED_FOLDER}")
                else:
                    print(f"Skipping move for {file_name} due to upload failure.")
        
        time.sleep(UPLOAD_INTERVAL)

if __name__ == "__main__":
    try:
        monitor_folder()
    except KeyboardInterrupt:
        print("\nStopping the script. Goodbye!")
