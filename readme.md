# This package allows you to add certain tags to tmx files

## How to install on Windows (no admin rights required)

Step 1. Get Python 3 from Microsoft Store

Step 2. Get PowerShell from Microsoft Store

Step 3. Create a new folder in your file system on Windows

Step 4. Right-click on that folder and select Open in Terminal

Step 5. Write the following in the command line of the open Terminal window: 
```
> python3 -m venv .venv
> .\.venv\Scripts\Activate.ps1
> python3 -m pip install tmxtagger
```

## How to use

If you've just finished the installation, just type in in the command line:
```
> python3 -m tmxtagger
```
This will open a Folder Selection dialogue window. Use it to select the folder 
containing your tmx files. After you click on Select, the program will
create a new folder called ```\tmx-trados-style``` within that selected
folder. 

The name of each original tmx file will becomes an attribute 
of each <tu> element so that when you import such tmx files into Trados 
Studio's TM, each imported segment will have a property whose value is 
the name of the tmx file from which that segment originated. It  will also
modify the tmx file header to conform to Trados Studio style. 

If you already closed PowerShell, use Windows Explorer to find the folder
that you created in Step 3 (or simply repeat Steps 3 to 5 if you can't find it). 
Open that folder in PowerShell Terminal. Then type in the following
commands in the PowerShell window:
```
> .\.venv\Scripts\Activate.ps1
> python3 -m tmxtagger
```