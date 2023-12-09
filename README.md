# FastDatasetMaker (FDM)
Remove vocals from YouTube video
I'm noob at this

# How to install

Ffirst of all you have to install FFMPEG

win>(type) system > system properties > environment variables > (click) PATH > edit > new > (type) ```C:\Program Files\ffmpeg\bin```

VIDEO HOW TO CREATE ENVIRONMENT VARIABLE: 

https://www.editframe.com/guides/how-to-install-and-start-using-ffmpeg-in-under-10-minutes/Create_Environment_Variable.mp4
___
download repository or ```git clone https://github.com/Mika4334/FDM_FastDatasetMaker.git```

User **Terminal** for:

check if repository in folder ```dir FDM_FastDatasetMaker```

open foledr ```cd .\FDM_FastDatasetMaker\```
___
**Inside** **_FDM_FastDatasetMaker_** folder:

create venv ```python -m venv venv```

activate
 ```.\venv\Scripts\activate```

 {_optional (not recomended)_} upgrade pip ```python.exe -m pip install --upgrade pip```

check if venv is activated
![image](https://github.com/Mika4334/FDM_FastDatasetMaker/assets/44061554/1629db92-fee9-41cc-b928-d3b520f048a9)

install some reqs ```pip install -r requirements.txt```  wait until all runnning setup.py **done** and everything **Successfully installed**

after install torch ```pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118```



open ```py .\FastDatasetMaker.py```

enter any yt link FOR EXAMPLE: 

[eng]
 ```https://www.youtube.com/watch?v=M7FIvfx5J10```
[rus]
 ```https://www.youtube.com/watch?v=RL7wMoH6cvA```

enjoy :)

# P.S.
Названия моделей отсечения вокала которые скачиваются автоматом тут ```model_name_mapper.json```
Пока заменяются модели только в коде

# Real Autors 
Anjok07 /ultimatevocalremovergui
https://github.com/Anjok07/ultimatevocalremovergui

karaokenerds /python-audio-separator
https://github.com/karaokenerds/python-audio-separator

TRvlvr/model_repo
https://github.com/TRvlvr/model_repo/releases/

# Get models from here
https://github.com/TRvlvr/model_repo/releases/

