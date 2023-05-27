class Author:
    def __init__(self, name):
        self.name = name
        self._tool = None
    
    @property
    def tool(self):
        return self._tool
    
    @tool.setter
    def tool(self, value):
        self._tool = value

class Tool:
    def __init__(self, type):
        self.type = type

    def write(self):
        return f"The {self.type} is writting something"
    
author = Author("Luiz")
pen = Tool("pen")
author.tool = pen
print(author.tool.write())