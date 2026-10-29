from abc import ABC,abstractmethod

class DataParser:
    def _parse(self):
        self._open()
        self._dataparser()
        self._close()
    
    def _open(self):
        print("Opening the file")
    
    def _close(self):
        print("Closing the file")
    
    @abstractmethod
    def _dataparser(self):
        pass
        
class CSVParser(DataParser):
    def _dataparser(self):
        print("Parsing CSV file")
    

csv_parser = CSVParser()
csv_parser.parse()