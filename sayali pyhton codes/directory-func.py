import os
os.mkdir("NewFolder")
os.rename("NewFolder", "FolderRenamed")
print(os.getcwd())
print(os.listdir())
os.rmdir("FolderRenamed")
os.remove("removing-file.txt") #removing-file.txt should be present in directory else will give error