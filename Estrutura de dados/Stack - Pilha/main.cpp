#include <iostream>
#include "Stack.h"

void PrintTopCountSize(Stack& stack)
{
	char top = stack.Top();
	if (top == '\0')
		std::cout << "Topo: Pilha vazia.\n";
	else
		std::cout << "Topo: " << top << '\n';
	std::cout << "Elementos na pilha: " << stack.Count() << '/' << stack.Size()
		<< ", a pilha " << (stack.IsEmpty() ? "está vazia" : "contém elementos") << ".\n";
}

int main()
{
	setlocale(LC_CTYPE, "Portuguese");

	Stack stack;
	PrintTopCountSize(stack);

	std::cout << "--------------------\n";
	std::string str = "Hello, World!";
	for (int i = 0; i < str.length(); ++i)
	{
		stack.Push(str[i]);
		PrintTopCountSize(stack);
	}

	std::cout << "--------------------\n";
	char top;
	while (!stack.IsEmpty())
	{
		top = stack.Pop();
		std::cout << "Pop retornou: " << top << '\n';
		PrintTopCountSize(stack);
	}

	std::cout << "--------------------\n";
	for (const char& c : str)
		stack.Push(c);
	PrintTopCountSize(stack);

	std::cout << "--------------------\n";
	stack.Clear();
	PrintTopCountSize(stack);
}
