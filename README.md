# simple-backup
This small script allows you to set up a backup of directories in windows machine to another storage.
### Usage
In settings.txt set the directories you want to archive, the directory in which to save the archive, and how many copies to keep.  
Also you can use network share in settings:
```
backup_folder = '//SERVER/backup/'
```
Then run script with python:
```cmd
python backup.py
```
Or just run backup.exe(don't forget to store settings.txt near), some antiviruses can give a false alarm, ignore them, or compile .exe by yourself.  
You can create task in Windows scheduler to automatic backup, don't forget to set "working path" where script is running.
