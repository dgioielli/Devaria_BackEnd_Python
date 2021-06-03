import json

class BaseDTO:


    def dumps(self):
        return json.dumps(self.__dict__)