import utils as Utils

class State:
    def __init__(self, header:str, command_list):
        self.__header = header
        self.__command_list = command_list
        
    def __str__(self):
        string_command_list = ''
        
        for command in self.__command_list:
             string_command_list += command.to_string() + '\n'
            
        return f'{self.__header}\n{string_command_list}'
    
    def to_string(self):
        return self


class StateManager:
    def __init__(self, start_state:State):
        self.__current_state = start_state
        
    def change_state(self, state:State):
        self.__current_state = state
        Utils.ConsolUtilit.ClearConsole()
        
class States:
    Main = State(f'Сейчас в библиотеке {Library.main().count} книг.', 
                        [Command(Utils.Actions.Exit, "выхода"),
                         Command(Utils.Actions.AddBook, "добавления книги"),
                         Command(Utils.Actions.PrintAll, "вывода всех книг")
                         ])