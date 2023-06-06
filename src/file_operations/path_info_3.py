import os
import pathlib
import shutil

os.remove() #removes a file.
os.rmdir() #removes an empty directory.
shutil.rmtree() #deletes a directory and all its contents.

# Path objects from the Python 3.4+ pathlib module also expose these instance methods:

pathlib.Path.unlink() #removes a file or symbolic link.
pathlib.Path.rmdir() #removes an empty directory.

# https://stackoverflow.com/questions/6996603/how-can-i-delete-a-file-or-folder-in-python?rq=1