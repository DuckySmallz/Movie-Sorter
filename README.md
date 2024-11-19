HOW TO USE!!!

After downloading please delete the PLACE_HOLDER.txt files from the stripper, input, and upload directory.

For Bulk re-naming:
Move all folders with video files you want to rename into the stripper folder (This process will delete everything that isn't a video file so don't put anything you want to keep in this folder).
Run the .BAT file named 'run.bat'. This batch script will first run stripper.py, which will scan everything in the stripper folder, move any video files to the input folder, then clean itself out.
The script will then launch the main tool main.py
Press the elipses, which will open up a file explorer window (should default to the input folder), select a file, enter its name and verify the year and resolution are correct (should be entered automatically but the
tool sometimes gets it wrong). Then press "Add". When you have named all the files, click write. The tool should close itself and open the upload folder with your files being ready to upload to your media server, backup, or destination folder.

IF RUN.BAT DOESN'T WROK!!
change python to either py, py3, or python3. if this still doesn't work, verify you have the latest version of python installed and that it is added to your computers PATH.
