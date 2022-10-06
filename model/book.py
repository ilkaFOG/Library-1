class Book:
    def __init__(self, title:str, year:int, author:str):
        self.title = title
        self.year = year
        self.author = author
        
    def __str__(self):
        return f'{self.title}'
    
    def to_string(self):
        return f'{self.title},{self.year},{self.author}'
        
    @property
    def author (self):
        return self.__author
        
    @author.setter 
    def author (self,author:str):
        assert isinstance(author, str), "заголовок должен быть строкой"
        self.__author = author
        
    @property
    def year (self):
        return self.__year
            
    @year.setter 
    def year (self,year:int):
        assert isinstance(year, int), "год должен быть целочисленным"
        self.__year = year
        
    @property
    def title (self):
        return self.__title
        
    @title.setter 
    def title (self,title:str):
        assert isinstance(title, str), "заголовок должен быть строкой"
        self.__title = title