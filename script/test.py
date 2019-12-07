# Запуск скрипта: python test.py
from urllib.request import urlopen	#для url
import re	#для regexp
import os	#для получения пути к файлам
import subprocess	#для запуска ffmpeg.exe
ffmpeg='X://Program//ffmpeg-20191204-d5274f8-win64-static//bin//ffmpeg.exe -i'	#get from https://www.ffmpeg.org/download.html

# константы
NOTFOUNDERR = 'notFound'
ENV='dv-h' #ev-h,dv-h
ROOTURL = 'https://'+ENV+ \
'.test.com/videos/25/21.mp4.urlset/'

#DV-H:
TTL='1'
L='0'
HASH='z11z1z1z1z1z1'
#EV-H:
VALIDFROM='1'
VALIDTO='2'
HDL='3'

def GetEndName(prefix=ENV):
	if prefix == 'ev-h':
		return "?validfrom="+VALIDFROM+'&validto='+VALIDTO+'&hdl='+HDL+'&hash='+HASH
	if prefix == 'dv-h':
		return "?ttl="+TTL+'&l='+L+'&hash='+HASH
	raise ValueError('Проблема с префиксом. Такого нет.')

def GetMasterFile():
	fileName = ROOTURL+'master.m3u8'+GetEndName()
	print('URL: '+fileName)
	f = urlopen(fileName)
	
	#качаем результат запроса как байт-поток:
	myfile = f.read()
	print(myfile)
	byteAsString = str(myfile, 'utf-8')
	if 'index.m3u8' in byteAsString:
		return 'index.m3u8'
	else:
		return NOTFOUNDERR

def GetListFromIndex(targetFilename):
	fileName = ROOTURL+targetFilename+GetEndName() #'index.m3u8'
	print('URL: '+fileName)
	f = urlopen(fileName)
	myfile = f.read()
	print(myfile)
	byteAsString = str(myfile, 'utf-8')
	tsParsedArray = re.findall('seg-\w.+\.ts', byteAsString)
	return tsParsedArray

def LoadTsAsPart(element, indx):
	fileName = ROOTURL+element+GetEndName() #'seg-2.ts'
	print('URL: '+fileName)
	f = urlopen(fileName)
	myfile = f.read()
	with open(f'{indx}.ts', "wb") as tsFile:	#запись в режиме байт-поток
		tsFile.write(myfile)
	print(indx, ' OK');
	return f'/{indx}.ts|'

#Получаем мастер-файл с индексами:
indexFilename = GetMasterFile()
print(indexFilename)
if indexFilename in NOTFOUNDERR:
	raise ValueError('Ненайден константный файл.')
#Получаем по индексу список .ts файлов:
tsList = GetListFromIndex(indexFilename)	#example tsList = ['seg-9.ts']
print('Файлов ts: ', len(tsList))
#Скачиваем все ts файлы, сборка строки из имен .ts файлов:
concateFileStr = ' "concat:'
for indx, item in enumerate(tsList):
	concateFileStr += os.getcwd()+LoadTsAsPart(item, indx)
print(concateFileStr.strip('|'))

# локальная сборка строки из имен .ts файлов:
# for x in range(15):
	# concateFileStr += os.getcwd()+f'/{x}.ts|'
# print(concateFileStr)

#собираем в один output.mp4 файл:
subprocess.call(ffmpeg+concateFileStr.strip('|')+'" -c copy output.mp4')
