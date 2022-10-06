import untils as Utils

class State:
    def __init__(self, header:str, command_list):
        self.__header = header
        self.__command_list = command_list
        
    def __str__(self):
        return f'{self.__header}\n{self.__command_list}'


class StateManager:
    def __init__(self, start_state:State):
        self.__current_state = start_state
        
    def change_state(self, state:State):
        self.__current_state = state
        Utils.ConsolUtilit.ClearConsole()