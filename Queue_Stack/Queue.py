import queue as qu

aa = qu.Queue()

for i in range(1, 101):
    aa.put(i)

while aa.qsize():
    print(aa.get())

if aa.empty():
    print('aa in empty')