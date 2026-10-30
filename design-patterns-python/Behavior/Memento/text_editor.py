from text_memento import TextMemento

class TextEditor:
    def __init__(self):
        self.__text = ""
    
    def write(self, text):
        self.__text += text
    
    def get_text(self) -> str:
        return self.__text
    
    def save(self) -> TextMemento:
        return TextMemento(self.__text)
    
    def restore(self, memento: TextMemento):
        self.__text = memento.get_saved_text()