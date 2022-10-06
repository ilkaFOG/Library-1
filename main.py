from library import Library
from state import State, StateManager 
import utils as Utils

library = Library()
# state_manager = StateManager()

class Command:
    def __init__(self, action,description):
        self.__action = action
        self.__description = description
        
    def __str__(self):
        return f'Введите {self.__action} для {self.__description}'
        # return f'{self.__description} - {self.__action}'
        
    def to_string(self):
        return f'Введите {self.__action} для {self.__description}'
          
    @property
    def action(self):
        return self.__action
  

library_commands = [Command(Utils.Actions.Exit, "выхода"),
                    Command(Utils.Actions.AddBook, "добавления книги"),
                    Command(Utils.Actions.PrintAll, "вывода всех книг")
                    ]      


start_state = State(f'Сейчас в библиотеке {library.count} книг.', 
                    library_commands)

print(start_state)

while False:
    pass