class Stack:
    precedence = {'^': 5, '*': 4, '/': 4, '-': 3, '+': 3, '(': 2, ')': 1}

    def __init__(self):
        self.items = []
        self.size = -1

    def push(self, value):
        self.items.append(value)
        self.size += 1

    def isEmpty(self):
        return self.items == []

    def pop(self):
        if self.isEmpty():
            return 0
        else:
            self.size -= 1
            return self.items.pop()

    def seek(self):
        if self.isEmpty():
            return False
        else:
            return self.items[self.size]

    def isOperand(self, i):
        if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            return True
        else:
            return False

    def infix_to_postfix(self, expr):
        postfix = ""

        for i in expr:
            if len(expr) % 2 == 0:
                print("Invalid Expression")
                return False

            elif self.isOperand(i):
                postfix += i

            elif i in '^*+-/':
                while len(self.items) and self.precedence[i] <= self.precedence[self.seek()]:
                    postfix += self.pop()

                self.push(i)

            elif i in '(':
                self.push(i)

            elif i in ')':
                temp = self.pop()
                while temp != '(':
                    postfix += temp
                    temp = self.pop()
            print(postfix)
        while len(self.items):
            if self.seek() == '(':
                self.pop()

            else:
                postfix += self.pop()
        return postfix


s = Stack()
expr = "(A+B)*C"
result = s.infix_to_postfix(expr)
if result != False:
    print("the postfix of :", expr,  "is", result)


