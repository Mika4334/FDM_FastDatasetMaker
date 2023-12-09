import os
import json
import time

from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi
from pydub import AudioSegment

from audio_separator import Separator

# Введите ссылку на видео
video_link = input("Введите ссылку на видео: ")

# Извлечение video_id из ссылки
if "youtube.com/watch?v=" in video_link:
    video_id = video_link.split("youtube.com/watch?v=")[-1] 
elif "youtu.be/" in video_link:
    video_id = video_link.split("youtu.be/")[-1]
else:
    video_id = video_link.split("/")[-1].split("?")[0]

# Получение данных о видео
youtube_video = YouTube(video_link)
video_owner = youtube_video.author

# Создание папки с названием владельца видео и обрезанного аудио
folder_name = video_owner
os.makedirs(folder_name, exist_ok=True)
os.makedirs(os.path.join(folder_name, 'cutted'), exist_ok=True)

# Скачивание видео
video_path = youtube_video.streams.get_highest_resolution().download(output_path=folder_name)
print("Видео успешно скачано.")

# Получение транскрипта для видео
transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en', 'ru'])

# Создание списка для хранения транскрипта
transcript_data = []

# Вывод и сохранение данных транскрипта
for caption in transcript:
    start = caption['start']
    text = caption['text']
    transcript_data.append({'start': start, 'text': text})
    print(f"Время: {start} - Текст: {text}")

# Сохранение данных транскрипта как JSON
transcript_filename = f"{folder_name}.json"
transcript_filepath = os.path.join(folder_name, transcript_filename)
with open(transcript_filepath, 'w', encoding='utf-8') as json_file:
    json.dump(transcript_data, json_file, ensure_ascii=False)
print("Файл с транскриптом успешно сохранен.")

# Определение пути к видеофайлу
video_file = os.path.join(folder_name, video_path.split('/')[-1])

# Конвертация видео в аудио
audio = AudioSegment.from_file(video_file) 
audio_file = audio.export(os.path.join(folder_name, 'audio.wav'), format='wav') 
print("Видео успешно конвертировано в аудио формата WAV.")

# ОБРЕЗКА ВОКАЛА 

# Получаем текущую директорию проекта
project_root = os.getcwd()
# Объединяем путь к текущей директории с названием папки
models_directory = os.path.join(project_root, 'audio-separator-models')
# Проверка пути папки с моделями
print(models_directory)

# # for primary
# instrumental_paths=os.path.join(project_root, 'instrumental')
# #for secondary
# vocal_paths=os.path.join(project_root, 'vocal')

audio_file_name=os.path.join(folder_name, 'audio.wav')
output_audio=os.path.join(folder_name, 'output')

# Пока что лучший вариант модели 'UVR-MDX-NET-Voc_FT'
# скачивать тут https://github.com/TRvlvr/model_repo/releases/
separator = Separator(audio_file_path=audio_file_name,
                      output_format='WAV',
                      output_dir=output_audio, 
                      model_name='UVR-MDX-NET-Voc_FT',
                      model_file_dir=models_directory,
                           use_cuda=True, 
                           use_coreml=True,
                           normalization_enabled=True,
                           denoise_enabled=True, 
                           output_single_stem='vocals',
                        #    primary_stem_path=output_audio, 
                        #    secondary_stem_path='instrumental',
                        #    primary_stem_path=instrumental_paths, 
                        #    secondary_stem_path=vocal_paths,
                           )

output_audio_vocals=separator.separate()
print(output_audio_vocals)
audio_file = os.path.join(output_audio, output_audio_vocals[0])
print(audio_file)
print("Успешно отсечён вокал.")

audio_new = AudioSegment.from_file(audio_file) 

# Считывание данных из JSON файла
with open(transcript_filepath, 'r', encoding='utf-8') as json_file: 
    transcript_data = json.load(json_file)

# Обрезка аудио в соответствии с указанными метками начала нового текста в JSON файле
duration_adjustment = 0.1 
# Длительность обрезки 
for index, caption in enumerate(transcript_data): 
    start_time = float(caption['start']) 
    if index != len(transcript_data)-1: 
        end_time = float(transcript_data[index+1]['start']) + duration_adjustment 
    else: 
        end_time = float(audio_new.duration_seconds) 
    caption_audio = audio_new[(int(start_time * 1000)):(int(end_time * 1000))]
    cutted_folder = os.path.join(folder_name, 'cutted') 
    os.makedirs(cutted_folder, exist_ok=True) 
    caption_audio.export(os.path.join(cutted_folder, f"{index+1}.wav"), format='wav') 
print("Аудио успешно обрезано и сохранено в папке 'cutted'.")