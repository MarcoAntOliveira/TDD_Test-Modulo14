def add_number(n1:int ,  n2:float) -> int:
    if not n1:
        return 0

    return n1 + n2
initial: tuple[str, ...] = ("one", "two")

class Parent:
    def capitalise(self, text:str) -> str:
        return text.upper()

class child(Parent):
    def capitalise(self, text: str) -> str:
        return str(text).upper()
    

