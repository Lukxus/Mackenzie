#include "Stack.h"

Stack::Stack()
	: m_Count(0)
	, dummy(true)
{
	for (int i = 0; i < STACK_CAPACITY; ++i)
		m_Values[i] = '\0';
}

bool Stack::Push(char value)
{
	if (m_Count == STACK_CAPACITY)
		return false;

	m_Values[m_Count] = value;
	++m_Count;

	return true;
}

char Stack::Pop()
{
	if (IsEmpty())
		return '\0';

	--m_Count;
	char top = m_Values[m_Count];
	m_Values[m_Count] = '\0';

	return top;
}

char Stack::Top()
{
	return IsEmpty() ? '\0' : m_Values[m_Count - 1];
}

int Stack::Size()
{
	return sizeof(m_Values) / sizeof(m_Values[0]);
}

int Stack::Count()
{
	return m_Count;
}

bool Stack::IsEmpty()
{
	return m_Count == 0;
}

void Stack::Clear()
{
	while (!IsEmpty())
	{
		Pop();
	}
}
