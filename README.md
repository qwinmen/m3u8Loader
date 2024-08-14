# m3u8Loader
Save and parse m3u8, then extract all ts files and build one a file.
<br>
Проект "выходного дня" на python 3.7 под windows10.<br>
Вводная:<br>
-Имеем тестовый сайт a.test.com, вещающий потоковое видео в открытом доступе.<br>
-Консоль браузера при этом выводит постоянно догружающиеся .ts файлы, это и есть "порционный" видео поток.<br>
<br>Схематика структуры файлов:
<br><img src="https://github.com/qwinmen/m3u8Loader/blob/master/logic.PNG" title="схематика структуры файлов"><br>
Задача:<br>
-получить список с ts файлами<br>
-загрузить ts файлы<br>
-собрать из ts файлов итоговый файл. Пример сборки в файле <a href="https://github.com/qwinmen/m3u8Loader/blob/master/ConcateAll_Ts_to_mp4.txt">ConcateAll_Ts_to_mp4.txt</a><br>
<br>
Понадобится:<br>
-Python3<br>
-<a href="https://www.ffmpeg.org/download.html">ffmpeg.exe</a><br>
<br>
Результат:<br>
-Файл <a href="https://github.com/qwinmen/m3u8Loader/blob/master/script/test.py">\script\test.py</a><br>
<br>
Обновление скрипта:<br>
-Добавлена возможность собирать множество ts файлов в один большой, а конвертировать уже один файл ts, а не множество;

Пример работы скрипта:
![Untitled](https://github.com/user-attachments/assets/e3d9b23d-f17a-4053-bc24-fc30b48af5c4)

