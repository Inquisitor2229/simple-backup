import os, zipfile, glob
from datetime import datetime

#comment this if you want to store folders in backup.txt
with open('settings.txt') as f:
    for line in f:
        exec(line)

#uncomment this, if want store folders in backup.txt file, one row per folder to backup...
#save = 5
#with open('backup.txt') as f:
#    dir_list = f.readlines()
#backup_folder = 'E:\\downloads\\'
#dir_list = [x.replace('\\', '/').strip() for x in dir_list]
now = datetime.now()
date_time = now.strftime("%Y-%m-%d_%H%M%S")
zip_name = backup_folder + date_time + '.zip'

def zipdir(path, ziph):
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file),
                       os.path.relpath(os.path.join(root, file),
                                       os.path.join(path, '..')))

def zipit(dir_list, zip_name):
    zipf = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED, allowZip64=True, compresslevel=9)
    for dir in dir_list:
        zipdir(dir, zipf)
    zipf.close()

zipit(dir_list, zip_name)

#remove last copies
files = glob.glob(backup_folder + '*.zip')
files.sort()

for f in files[:-save]:
    os.unlink(f)
