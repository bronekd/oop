# použití mojich errorů
class MyCustomError(Exception):
    def __int__(self, message):
        self.message = message

    def __str__(self):
        return f"MyCustomError: {self.message}"



