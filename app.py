from model.book import Book
from model.library import Library
import ui.ui as ui
from model.state import StateManager, States


class App:
    @staticmethod
    def run():
        ui.clear()

        library = Library()
        library.add(Book('asd',12,'asd'))
        state_manager = StateManager(library)
        state_manager.state_changed.add_listener(ui.draw_ui)
        state_manager.change_state(States.Main)

        while state_manager.is_work:
            state_manager.current_state.handle_input(state_manager)
