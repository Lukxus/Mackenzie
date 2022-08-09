#ifndef __CIRCULAR_DOUBLE_LINKED_LIST_H__
#define __CIRCULAR_DOUBLE_LINKED_LIST_H__

#include <string>

struct Node
{
	int id;
	std::string name;

	Node* previous;
	Node* next;
};

struct LinkedList
{
	int count;
	Node* head;
	Node* tail;
};

LinkedList* Create();
void Destroy(LinkedList* list);
void Insert(LinkedList* list, int id, std::string name);
void Append(LinkedList* list, int id, std::string name);
Node* RemoveHead(LinkedList* list);
Node* RemoveTail(LinkedList* list);
Node* RemoveNode(LinkedList* list, int id);
Node* GetHead(const LinkedList* list);
Node* GetTail(const LinkedList* list);
Node* GetNode(const LinkedList* list, int id);
int Count(const LinkedList* list);
bool IsEmpty(const LinkedList* list);
void Clear(LinkedList* list);

Node* CreateNode(int id, std::string name, Node* previous, Node* next);
void DestroyNode(Node* node);

#endif //  __CIRCULAR_DOUBLE_LINKED_LIST_H__