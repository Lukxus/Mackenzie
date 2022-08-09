/*
FABIO DOMINGUES PEREIRA SABINO - TIA: 32154429
LUIZ OCTAVIO TASSINARI SARAIVA - TIA: 32030411
LEONARDO PINHEIRO DE SOUZA - TIA: 32127391
MATHEUS FARIAS DE OLIVEIRA MATSUMOTO - TIA: 32138271
*/

#ifndef __LINKED_LIST_H__
#define __LINKED_LIST_H__

#include <string>

using namespace std;

struct Node
{
	string Disciplina;
	string ISBN;
	string Titulo;
	string Autor;
	int Edicao;
	string Cidade;
	string Editora;
	int Ano;
	bool Complementar;
	Node* next;
};

struct LinkedList
{
	int size;
	Node* head;
	Node* tail;
};

LinkedList* Create();
void Destroy(LinkedList* list);
void Insert(LinkedList* list, string nomeDisciplina, string codigoISBN, string nomeLivro, string nomeAutor, int numEdicao, string nomeCidade, string nomeEditora, int numAno, bool complemento);
void Append(LinkedList* list, string nomeDisciplina, string codigoISBN, string nomeLivro, string nomeAutor, int numEdicao, string nomeCidade, string nomeEditora, int numAno, bool complemento);
Node* RemoveHead(LinkedList* list);
Node* RemoveTail(LinkedList* list);
Node* GetNode(const LinkedList* list, string codigoISBN);
int Count(const LinkedList* list);
bool IsEmpty(const LinkedList* list);
void Clear(LinkedList* list);

Node* CreateNode(string nomeDisciplina, string codigoISBN, string nomeLivro, string nomeAutor, int numEdicao, string nomeCidade, string nomeEditora, int numAno, bool complemento, Node* next);
void DestroyNode(Node* node);

#endif