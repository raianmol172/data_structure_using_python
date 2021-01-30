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
        if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or i in "0123456789":
            return True
        else:
            return False

    def reverse(self, expr):
        rev = ""
        for i in expr:
            if i == '(':
                i = ')'
            elif i == ')':
                i = '('
            rev = i + rev
        return rev

    def infix_to_prefix(self, expr):
        prefix = ""

        for i in expr:
            if len(expr) % 2 == 0:
                print("Invalid Expression")
                return False

            elif self.isOperand(i):
                prefix += i

            elif i in '^*+-/':
                while len(self.items) and self.precedence[i] <= self.precedence[self.seek()]:
                    prefix += self.pop()

                self.push(i)

            elif i in '(':
                self.push(i)

            elif i in ')':
                temp = self.pop()
                while temp != '(':
                    prefix += temp
                    temp = self.pop()
        while len(self.items):
            if self.seek() == '(':
                self.pop()

            else:
                prefix += self.pop()
        return prefix


s = Stack()
expr = "(1+2)*3"
rev = s.reverse(expr)
result = s.infix_to_prefix(expr)
if result != False:
    prefix = s.reverse(result)
    print("the prefix of :", expr,  "is", prefix)


