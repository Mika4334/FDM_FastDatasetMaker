# FastDatasetMaker (FDM)
Remove vocals from YouTube video
I'm noob at this

# How to install
First of all you have to install FFMPEG:

Download here 
https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip 

or check some .zip here
https://ffmpeg.org/download.html

unzip in ```C:\Program Files\``` and rename folder as **_ffmpeg_** ```C:\Program Files\ffmpeg```

after that create environment variable

**_win > (type) system > system properties > environment variables > (click) PATH > edit > new > (type)_** 

```C:\Program Files\ffmpeg\bin```


![image](https://github.com/Mika4334/FDM_FastDatasetMaker/assets/44061554/665c0b1a-9a9c-46f4-b372-b1c9a095bd56)

IF STRUGGLE CHECK VIDEO HOW TO CREATE ENVIRONMENT VARIABLE: 
https://www.editframe.com/guides/how-to-install-and-start-using-ffmpeg-in-under-10-minutes/Create_Environment_Variable.mp4
___
download **FDM_FastDatasetMaker** repository as .zip https://github.com/Mika4334/FDM_FastDatasetMaker/archive/refs/heads/main.zip 

or simply clone it ```git clone https://github.com/Mika4334/FDM_FastDatasetMaker.git```

User **Terminal** for:

check if repository in folder ```dir FDM_FastDatasetMaker```

open foledr ```cd .\FDM_FastDatasetMaker\```
___
**Inside** **_FDM_FastDatasetMaker_** folder:

create venv ```python -m venv venv```

activate
 ```.\venv\Scripts\activate```

 {_optional_} upgrade pip ```python.exe -m pip install --upgrade pip```

check if venv is activated
![image](https://github.com/Mika4334/FDM_FastDatasetMaker/assets/44061554/1629db92-fee9-41cc-b928-d3b520f048a9)

install some reqs ```pip install -r requirements.txt```  

wait until all runnning setup.py **done** and everything **Successfully installed**

after install torch ```pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118```

**_Done!_**

# Run
open ```py .\FastDatasetMaker.py```

enter any yt link FOR EXAMPLE: 

[eng]
 ```https://www.youtube.com/watch?v=M7FIvfx5J10```
[rus]
 ```https://www.youtube.com/watch?v=RL7wMoH6cvA```

enjoy :)

audio files will be saved in ```cutted`` folder, also ```.json``` have time and text of the video

# P.S.
Name of the models that will download automatically here ```model_name_mapper.json```
or download it from **Get models**

```[ ]``` Maybe soon you will be able to use another models

```[ ]``` Also going to release some features soon or you could suggest anythin

# Get models
https://github.com/TRvlvr/model_repo/releases/

# Real Autors 
Anjok07 /ultimatevocalremovergui
https://github.com/Anjok07/ultimatevocalremovergui

karaokenerds /python-audio-separator
https://github.com/karaokenerds/python-audio-separator

TRvlvr/model_repo
https://github.com/TRvlvr/model_repo/releases/
