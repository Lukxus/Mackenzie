#ifndef __QUEUE_H__
#define __QUEUE_H__

const int QUEUE_CAPACITY = 16;

struct Queue
{
	int front;
	int rear;
	int count;
	char values[QUEUE_CAPACITY];
};

Queue Create();
bool Enqueue(Queue& queue, char value);
char Dequeue(Queue& queue);
char Front(const Queue& queue);
int Size(const Queue& queue);
int Count(const Queue& queue);
bool IsEmpty(const Queue& queue);
void Clear(Queue& queue);

#endif