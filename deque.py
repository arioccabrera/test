from collections import deque

dep = deque('geek')
print(dep)

dep.append('y')
print(dep)

dep.appendleft('K')
print(dep)

print(dep.pop())
print(dep)

print(dep.popleft())
print(dep)