/*
FABIO DOMINGUES PEREIRA SABINO - TIA: 32154429
LUIZ OCTAVIO TASSINARI SARAIVA - TIA: 32030411
LEONARDO PINHEIRO DE SOUZA - TIA: 32127391
MATHEUS FARIAS DE OLIVEIRA MATSUMOTO - TIA: 32138271
*/

#include "menu.h"
#include <codecvt>
#include <iostream>
#include <sstream>
#include <windows.h>
#include <map>


#pragma execution_character_set( "utf-8" )

int Menu()
{
    SetConsoleOutputCP(65001);

    int opcao;

    cout << "\n\n***** MENU DE OP��ES *****\n\n";
    cout << "1. Ler dados\n2. Exibir dados\n3. An�lise de dados A\n4. An�lise de dados B\n5. An�lise de dados C\n6. An�lise de dados D\n7. An�lise de dados E\n8. Encerrar";
    cout << "\nEscolha uma op��o: ";
    cin >> opcao;

    return opcao;
}

bool verificaVetor(string var, string vetor[])
{
    for (int i = 0; i < 40; i++)
    {
        if (vetor[i] == var) { return true; }
    }
    return false;
}

void analiseA(const LinkedList* list)
{
    cout << "\n\nANALISE A";
    cout << "\n__\n";
    cout << "\nQuantos livros foram publicados por editoras brasileiras, quantos livros foram publicados por editoras estrangeiras e suas respectivas porcentagens";
    cout << "\n__\n";
    int Internacional = 0;
    int Nacional = 0;
    int Total = 0;
    float InternacionalP, NacionalP;
    Node* atual = nullptr;
    atual = list->head;

    for (int i = 0; i < Count(list); i++) {
        if ((atual->ISBN)[4] == '8' && (atual->ISBN)[5] == '5')
            Nacional++;
        else
            Internacional++;
        atual = atual->next;
    }
    Total = Internacional + Nacional;
    InternacionalP = (float)Internacional * 100 / (float)Total;
    NacionalP = (float)Nacional * 100 / (float)Total;

    cout << "\nAs editoras brasileiras publicaram " << Nacional << " livros, o que representa " << NacionalP << "%";
    cout << "\nAs editoras internacionais publicaram " << Internacional << " livros, o que representa " << InternacionalP << "%";
}

void analiseB(const LinkedList* list)
{
    cout << "\n\nANALISE B";
    cout << "\n__\n";
    cout << "\nQuais s�o os nomes dos autores que publicaram seus livros em 'New York'";
    cout << "\n__\n";
    string nomes[40];
    int contador = 0;
    Node* atual;
    atual = list->head;
    for (int i = 0; i < Count(list); i++) {
        if (atual->Cidade == "New York") {
            nomes[contador] = atual->Autor;
            contador++;
        }
        atual = atual->next;
    }

    for (int i = 0; i < 30; i++) {
        if (nomes[i] != "") {
            cout << "\n" << nomes[i];
        }
    }
}

void analiseC(const LinkedList* list)
{
    cout << "\n\nANALISE C";
    cout << "\n\n";
    cout << "\nT�tulo dos livros que lan�aram antes de 2010 e seus respectivos autores";
    cout << "\n\n";

    string nomes[40];
    int contador = 0;
    Node* atual;
    atual = list->head;

    for (int i = 0; i < Count(list); i++) {
        if (atual->Ano < 2010) {
            nomes[contador] = atual->Titulo + " - " + atual->Autor;
            contador++;
        }
        atual = atual->next;
    }

    for (int i = 0; i < 30; i++) {
        if (nomes[i] != "") {
            cout << "\n" << nomes[i];
        }
    }
}

void analiseD(const LinkedList* list)
{
    cout << "\n\nANALISE D";
    cout << "\n\n";
    cout << "\nQuais s�o os livros que est�o no plano de ensino de mais de uma disciplina e quais s�o essas disciplinas?";
    cout << "\n\n";
    string vetor[40];
    int count = 0;
    for (Node* node = list->head; node != nullptr; node = node->next)
    {
        for (Node* aux = list->head->next; aux != nullptr; aux = aux->next)
        {
            if (node->Disciplina != aux->Disciplina && node->ISBN == aux->ISBN && verificaVetor(node->Titulo, vetor) == false)
            {
                cout << "\nDisciplinas:\n" << node->Disciplina << "\n" << aux->Disciplina;
                cout << "\nLivro:\n" << node->Titulo;
                vetor[count] = node->Titulo;
                count++;
            }
        }
    }
}

void analiseE(const LinkedList* list)
{
    cout << "\n\nANALISE E";
    cout << "\n\n";
    cout << "\nQuantidade de livros complementares de cada mat�ria";
    cout << "\n\n";

    int count = 0;
    int aux = 0;
    string disciplina[40];
    int nComplementar[40];

    disciplina[count] = list->head->Disciplina;
    for (Node* node = list->head; node != nullptr; node = node->next)
    {
        if (node->Disciplina != disciplina[count])
        {
            cout << "\n" << disciplina[count] << " possui " << nComplementar[count] << " livros complementares";
            ++count;
            aux = 0;
            disciplina[count] = node->Disciplina;
        }
        if (node->Complementar == true)
        {
            ++aux;
            nComplementar[count] = aux;
        }
    }
    cout << "\n" << disciplina[count] << " possui " << nComplementar[count] << " livros complementares";
}