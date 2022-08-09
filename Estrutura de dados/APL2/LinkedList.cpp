/*
FABIO DOMINGUES PEREIRA SABINO - TIA: 32154429
LUIZ OCTAVIO TASSINARI SARAIVA - TIA: 32030411
LEONARDO PINHEIRO DE SOUZA - TIA: 32127391
MATHEUS FARIAS DE OLIVEIRA MATSUMOTO - TIA: 32138271
*/

#include "LinkedList.h"

LinkedList* Create()
{
	LinkedList* list = new LinkedList;
	list->size = 0;
	list->head = nullptr;
	list->tail = nullptr;

	return list;
}

void Destroy(LinkedList* list)
{
	Clear(list);

	delete list;
	list = nullptr;
}

void Insert(LinkedList* list, string nomeDisciplina, string codigoISBN, string nomeLivro, string nomeAutor, int numEdicao, string nomeCidade, string nomeEditora, int numAno, bool complemento)
{
	Node* node = CreateNode(nomeDisciplina, codigoISBN, nomeLivro, nomeAutor, numEdicao, nomeCidade, nomeEditora, numAno, complemento, list->head);

	if (IsEmpty(list))
	{
		list->tail = node;
	}
		
	list->head = node;
	++list->size;
}

void Append(LinkedList* list, string nomeDisciplina, string codigoISBN, string nomeLivro, string nomeAutor, int numEdicao, string nomeCidade, string nomeEditora, int numAno, bool complemento)
{
	Node* node = CreateNode(nomeDisciplina, codigoISBN, nomeLivro, nomeAutor, numEdicao, nomeCidade, nomeEditora, numAno, complemento, nullptr);

	if (IsEmpty(list))
	{
		list->head = node;
	}
	else
	{
		list->tail->next = node;
	}
	list->tail = node;

	++list->size;
}

Node* RemoveHead(LinkedList* list)
{
	if (IsEmpty(list))
	{
		return nullptr;
	}

	Node* toRemove = list->head;

	if (list->head == list->tail)
	{
		list->head = list->tail = nullptr;
	}
	else
	{
		list->head = list->head->next;
	}

	--list->size;

	toRemove->next = nullptr;
	return toRemove;
}

Node* RemoveTail(LinkedList* list)
{
	if (list->head == list->tail)
	{
		return RemoveHead(list);
	}

	Node* toRemove = list->head;
	Node* previous = nullptr;

	while (toRemove != list->tail)
	{
		previous = toRemove;
		toRemove = toRemove->next;
	}

	previous->next = nullptr;
	list->tail = previous;

	--list->size;

	toRemove->next = nullptr;
	return toRemove;
}

Node* GetNode(const LinkedList* list, string codigoISBN)
{
	Node* node = list->head;
	while (node != nullptr)
	{
		if (node->ISBN == codigoISBN)
		{
			return node;
		}
		node = node->next;
	}

	return nullptr;
}

int Count(const LinkedList* list)
{
	return list->size;
}

bool IsEmpty(const LinkedList* list)
{
	return list->head == nullptr && list->tail == nullptr;
}

void Clear(LinkedList* list)
{
	Node* node = list->head;
	Node* next = nullptr;

	while (node != nullptr)
	{
		next = node->next;
		DestroyNode(node);
		node = next;
	}

	list->head = list->tail = nullptr;
	list->size = 0;
}

Node* CreateNode(string nomeDisciplina, string codigoISBN, string nomeLivro, string nomeAutor, int numEdicao, string nomeCidade, string nomeEditora, int numAno, bool complemento, Node* next)
{
	Node* node = new Node;
	node->Disciplina = nomeDisciplina;
	node->ISBN = codigoISBN;
	node->Titulo = nomeLivro;
	node->Autor = nomeAutor;
	node->Edicao = numEdicao;
	node->Cidade = nomeCidade;
	node->Editora = nomeEditora;
	node->Ano = numAno;
	node->Complementar = complemento;
	node->next = next;
	return node;
}

void DestroyNode(Node* node)
{
	delete node;
	node = nullptr;
}