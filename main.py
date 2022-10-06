from book import Book
from event import Event

book = Book("asd", 1927, 'author')
print(book.to_string())

def print_string(*args):
    for item in args:
        print(item)

start_event = Event()
start_event.add_listener(print_string)
    
start_event.invoke(1)
