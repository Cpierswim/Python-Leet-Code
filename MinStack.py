# Leetcode #155

class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
    
# NOTE FROM LEETCODE
# Your MinStack object will be instantiated and called as such:
# MinStack obj = new MinStack();
# obj.Push(val);
# obj.Pop();
# int param_3 = obj.Top();
# int param_4 = obj.GetMin();

obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin()) # Should be -3
obj.pop()
print(obj.top()) # Should be 0
print(obj.getMin()) #Should be -2