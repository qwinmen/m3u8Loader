# m3u8Loader
Save and parse m3u8, then extract all ts files and build one a file.
<br>
Проект "выходного дня" на python 3.7 под windows10.<br>
Вводная:<br>
-Имеем тестовый сайт a.test.com, вещающий потоковое видео в открытом доступе.<br>
-Консоль браузера при этом выводит постоянно догружающиеся .ts файлы, это и есть "порционный" видео поток.<br>
<br>
Задача:<br>
-получить список с ts файлами<br>
-загрузить ts файлы<br>
-собрать из ts файлов итоговый файл. Пример сборки в файле ConcateAll_Ts_to_mp4.txt<br>
<br>
Понадобится:<br>
-Python3<br>
-ffmpeg.exe<br>
<br>
Результат:<br>
-Файл \script\test.py<br>
