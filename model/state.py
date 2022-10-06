import ui.ui as ui
from model.command import Command
from model.actions import Actions
from model.event import Event
from model.library import Library


class State:
    def __init__(self, header: str, command_list):
        self.__header = header
        self.__command_list = command_list

    def __str__(self):
        string_command_list = ''

        for command in self.__command_list:
            string_command_list += command.to_string() + '\n'

        return f'{self.__header}\n{string_command_list}'

    def to_string(self):
        string_command_list = ''

        for command in self.__command_list:
            string_command_list += command.to_string() + '\n'

        return f'{self.__header}\n{string_command_list}'

    def handle_input(self, state_manager):
        pass


class MainState(State):
    def handle_input(self, state_manager):
        user_input = ui.get_int()
        if user_input == Actions.Exit.value:
            print('exit')
        elif user_input == Actions.AddBook.value:
            print('AddBook')
        elif user_input == Actions.RemoveBook.value:
            print('RemoveBook')
        elif user_input == Actions.FindBook.value:
            print('FindBook')
        elif user_input == Actions.PrintAt.value:
            print('PrintAt')
        elif user_input == Actions.PrintAll.value:
            state_manager.change_state(States.PrintAll)
        else:
            pass  # TODO incorrect input


class PrintAllState(State):
    def handle_input(self, state_manager):
        book_list = ''
        library = state_manager.library.get_all()
        index = 1
        for book in library:
            book_list += f'{index} - {book}\n'
            index += 1
        ui.draw_ui(book_list)
        ui.get_sting()
        ui.clear()
        state_manager.change_state(States.Main)


class StateManager:
    def __init__(self, library: Library):
        self.state_changed = Event()
        self.__current_state = States.Main
        self.library = library
        self.is_work = True

    @property
    def current_state(self):
        return self.__current_state

    def change_state(self, state: State):
        self.__current_state = state
        ui.clear()
        # Выход для динамики - переписал шаблон с регулярным выражением
        string_state = self.__current_state.to_string() % self.library.count
        self.state_changed.invoke(string_state)


class States:
    Main = MainState(f'Сейчас в библиотеке %s книг.', [
        Command(Actions.Exit, "выхода"),
        Command(Actions.AddBook, "добавления книги"),
        Command(Actions.RemoveBook, "удаления книги"),
        Command(Actions.FindBook, "поиска книги"),
        Command(Actions.PrintAt, "вывода детальной информации о книге"),
        Command(Actions.PrintAll, "вывода всех книг")
    ])

    AddBook = State(f'Сейчас в библиотеке %s книг.', [
        Command(Actions.Exit, "выхода"),
        Command(Actions.Undo, "отмены"),
    ])

    RemoveBook = State(f'Сейчас в библиотеке %s книг.', [
        Command(Actions.Exit, "выхода"),
        Command(Actions.Undo, "отмены"),
    ])

    PrintAll = PrintAllState(f'Сейчас в библиотеке %s книг.', [
        Command(Actions.Return, "отмены")
    ])
