# -Framework-Vosk
A framework for your voice assistants in python on the Vosk library || Основа для ваших голосвых помощников на python на библеотеке Vosk

# -Требуеться для работы // Needed for work
**RUS**

Для работы с данным шаблоном у вас должен быть устоновлен python а также - нужно устонавить модель для распознования голоса. 
*https://alphacephei.com/vosk/models*
После чего вам потребуеться: распокавать в удобную для вас место, скопировать расположение папки.
А также откройте командную строку (Win + R, cmd) и пропишите 
```pip install pyaudio, vosk```

**ENG**

To work with this template you must have python installed and also - you need to install a model for voice recognition. 
*https://alphacephei.com/vosk/models*
After that you will need: unpack in a convenient place for you, copy the location of the folder.

Also open a command line (Win + R, cmd) and write 
```pip install pyaudio, vosk```

# -Настройка в фаяле main.py // Customization in main.py
**RUS**

После всех выполненых выше шагов в строчку ```model = Model(r"F:/Vol_Playng/Vol_Praving/vosk-model-small-ru-0.22") # полный путь к модели``` замените путь на ваш!

**ENG**

After all the above steps in the line ```model = Model(r “F:/Vol_Playng/Vol_Praving/vosk-model-small-ru-0.22”) # полный путь к модели ``` replace the path with yours!

**RUS**

В 28 и 29 строке вы можите поменять фразу, если вы хотите можете также поставить туда фразу на других языках, но что бы они работали вам потребуеться устоновить их модель. 
А также при создание других функций пишите фразы с маленькой буквы, иначе могут не работать функции!

**ENG**

In line 28 and 29 you can change the phrase, if you want you can also put there a phrase in other languages, but to make them work you will need to install their model. 
Also, when creating other functions, write phrases with a small letter, otherwise the functions may not work!
