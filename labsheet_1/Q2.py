# Q2. Implement Queue using NumPy array.
print("\n")
import numpy as np
# QUEUE
queue = np.array([], dtype=int)
# ENQ
for item in [10, 20, 30]:
    queue = np.append(queue, item)
    print("After ENQ", item, ":", queue)
# DEQ
while len(queue) > 0:
    print("Dequeued:", queue[0])
    queue = np.delete(queue, 0)
    print("Queue:", queue)
print("\n")