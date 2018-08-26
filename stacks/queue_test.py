from stacks.queue import Queue

print('############################')
print('Testing Queue')
print('############################')

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print('Enqueued 1, 2, 3')
q.stdout()

assert q.dequeue() == 1
assert q.dequeue() == 2

print('Dequeued twice')
q.stdout()

q.enqueue(4)

print('Enqueued 4')
q.stdout()

assert q.dequeue() == 3
assert q.dequeue() == 4

print('Dequeued twice')
q.stdout()

q.enqueue(5)
q.enqueue(6)

print('Enqueued 5,6')
q.stdout()

assert q.dequeue() == 5
print('Dequeued once')
q.stdout()

assert q.dequeue() == 6
print('Dequeued once')
q.stdout()