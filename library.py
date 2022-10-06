from book import Book

class Library:
    def __init__(self):
        self.__book_list = []
        
    def add(self, book:Book):
        assert isinstance(book, Book), "object is not Book instance"
        self.__book_list.append(book)
    
    def removeAt(self, index:int):
        assert isinstance(index, int), "object is not Int instance"
        if index >= 0 and index < len(self.__book_list):
            return self.__book_list.pop(index)
        else:
            return None
        
    def getAt(self, index:int):
        assert isinstance(index, int), "object is not Int instance"
        if index >= 0 and index < len(self.__book_list):
            return self.__book_list[index]
        return None 
        
    def get_all(self):
        return self.__book_list.copy()