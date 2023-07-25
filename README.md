## Table of contents
* [General Information](#general-information)
* [Step of using](#step-of-using)
* [Installation](#installation)
* [Room for Improvement](#room-for-improvementlimitation)
* [remark](#remark)


# General Information
This project is created for media transfer across different folders, despite the change of the file name, this program can identify whether the items from source folders are already migrated to destination folder by comparing the content inside, if not exists, the files will be automatically transfer to source folder. Multiple Source path and destination path is allowed for each run.

# Step of Using
1. Execute main.py
```
python main.py
```
2. a Tkinter UI pop up
3. input the source path(s) and desintation path(s)
4. Press "Submit" for run
5. new files will be identified and transfered


# Installation
```
pip install -r requirements.txt
```
 

# Room for Improvement/Limitation
- limited file type
- speed of scanning file
- folder path have to input manually


# Remark
1. file type accepted:
- image: '*.jpg', '*.jpeg', '*.png', '*.bmp' , '*.gif'
- video: '*.mp4', '*.avi', '*.mkv', '*.mov'
2. if more than 1 destination path, new file will be automatically copied to first path
