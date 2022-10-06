import os # Импортируем библиотку для работы с ОС
import enum as Enum

class ConsolUtilit:
    def ClearConsole():
        clear = lambda: os.system('cls' if os.name=='nt' else 'clear') 
        clear()
  
class Actions:
    Exit = 0
    AddBook = 1
    RemoveBook = 2
    FindBook = 3
    PrintAll = 4
    PrtintAt = 5