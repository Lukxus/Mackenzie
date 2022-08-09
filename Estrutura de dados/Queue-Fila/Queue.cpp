#include "Queue.h"

Queue Create()
{
	Queue queue = { 0, 0, 0, { } };
	return queue;
}

bool Enqueue(Queue& queue, char value)
{
	if (queue.count == QUEUE_CAPACITY)
		return false;

	queue.values[queue.rear] = value;
	queue.rear = (queue.rear + 1) % QUEUE_CAPACITY;
	++queue.count;

	return true;
}

char Dequeue(Queue& queue)
{
	if (IsEmpty(queue))
		return '\0';

	char front = queue.values[queue.front];
	queue.front = (queue.front + 1) % QUEUE_CAPACITY;
	--queue.count;

	return front;
}

char Front(const Queue& queue)
{
	return IsEmpty(queue) ? '\0' : queue.values[queue.front];
}

int Size(const Queue& queue)
{
	return sizeof(queue.values) / sizeof(queue.values[0]);
}

int Count(const Queue& queue)
{
	return queue.count;
}

bool IsEmpty(const Queue& queue)
{
	return queue.count == 0;
}

void Clear(Queue& queue)
{
	while (!IsEmpty(queue))
	{
		Dequeue(queue);
	}
}
