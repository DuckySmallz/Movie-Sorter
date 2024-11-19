import os
import shutil

# Set the destination folder
dst_folder = 'input'
directory_path = str('stripper')
video_extensions = ['.mp4', '.mov', '.avi', '.mkv', '.webm']
for root, dirs, files in os.walk(directory_path):
    for file in files:
        if os.path.splitext(file)[1].lower() in video_extensions:
            src_path = os.path.join(root, file)
            dst_path = os.path.join(dst_folder, file)
            shutil.move(src_path, dst_path)

shutil.rmtree('stripper')
os.mkdir('stripper')