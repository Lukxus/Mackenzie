#ifndef __STACK_H__
#define __STACK_H__

const int STACK_CAPACITY = 4096;

class Stack
{
public:
	Stack(); //Stack Create();
	
	bool Push(char value);
	char Pop();
	
	char Top();
	
	int Size();
	int Count();
	bool IsEmpty();
	void Clear();

private:
	int m_Count;
	char m_Values[STACK_CAPACITY];
	bool dummy;
};

#endif
