import shutil
import os
import time
from tkinter import filedialog


def main(self):
    source = filedialog.askdirectory()
    destination = filedialog.askdirectory()    
    
    

def hours_since_mod(files):
    return (time.time() - os.path.getmtime(files))

def move_Files(self):
        source=self.sourcestr.get()
        destination=self.deststr.get()
        for files in os.listdir(source):
            filepath=os.path.join(source, files)
            if hours_since_mod(filepath) < 86400:
                shutil.move(filepath,destination)
                print (destination + files)

def source_ask_directory(self):
    source=filedialog.askdirectory()
    self.sourcestr.set(source)
    

def dest_ask_directory(self):
    destination=filedialog.askdirectory()
    self.deststr.set(destination)
    


        


if __name__ == "__main__":
    main()
