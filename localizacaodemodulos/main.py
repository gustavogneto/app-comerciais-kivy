from pprint import pprint
from sys import path as lpath
import ferramentas
pprint(lpath)

lpath.insert(10, "C:\\dev\\tmp\\")
"""['C:\\dev\\excript\\app-comerciais-kivy\\aulas\\localizacaodemodulos',
 'C:\\dev\\excript\\app-comerciais-kivy',
 'C:\\dev\\excript\\app-comerciais-kivy\\aulas\\criacaodemodulos',
 'C:\\dev\\excript\\app-comerciais-kivy\\aulas\\localizacaodemodulos',
 'C:\\ProgramData\\Anaconda3\\envs\\k35\\python35.zip',
 'C:\\ProgramData\\Anaconda3\\envs\\k35\\DLLs',
 'C:\\ProgramData\\Anaconda3\\envs\\k35\\lib',
 'C:\\ProgramData\\Anaconda3\\envs\\k35',
 'C:\\ProgramData\\Anaconda3\\envs\\k35\\lib\\site-packages']"""