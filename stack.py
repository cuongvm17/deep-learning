class Stack:
    def __init__(self):
        self.stack = []

    def push(self, elem):
        self.stack.push(elem)
    
    def pop(self):
        if len(self.stack) > 0:
            self.stack.pop()

        else:
            print('Stack is empty')

    def printAllElems(self):
        if len(self.stack) > 0:
            for elem in self.stack:
                print(elem)
        else:
            print("Stack is empty")
        
def isValid(s: str) -> bool:
    stack = []
    mapping = {")" : "(", "]" : "[", "}" : "{"}

    for letter in s:
        if letter not in mapping:
            stack.append(letter)
        else:
            if len(stack) > 0 and stack[-1] == mapping[letter]:
                stack.pop()
            else:
                return False
        
    return len(stack) == 0
        
print(isValid("()()()"))
print(isValid("{[("))