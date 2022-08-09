/*
FABIO DOMINGUES PEREIRA SABINO - TIA: 32154429
LUIZ OCTAVIO TASSINARI SARAIVA - TIA: 32030411
LEONARDO PINHEIRO DE SOUZA - TIA: 32127391
MATHEUS FARIAS DE OLIVEIRA MATSUMOTO - TIA: 32138271

REFERENCIAS:
https://www.w3schools.in/cplusplus/working-with-files
https://www.youtube.com/watch?v=NFvxA-57LLA&t=400s
https://www.cplusplus.com/reference/string/string/getline/
https://java2blog.com/read-csv-file-in-cpp/#:~:text=To%20read%20a%20CSV%20file%2C,variable%20as%20its%20second%20argument
https://www.geeksforgeeks.org/csv-file-management-using-c/
https://www.w3schools.com/cpp/cpp_files.asp
https://stackoverflow.com/questions/9753887/error-cannot-open-source-file
https://stackoverflow.com/questions/42858539/encoding-error-reading-csv-file-unicode-encoded-c
https://stackoverflow.com/questions/1120140/how-can-i-read-and-parse-csv-files-in-c?page=1&tab=scoredesc#tab-top
https://stackoverflow.com/questions/55749845/adding-a-csv-file-to-a-project-in-visual-studio#:~:text=You%20can%20include%20the%20files,into%20the%20bin%2Fdebug%20folder
https://stackoverflow.com/questions/1371012/how-do-i-print-utf-8-from-c-console-application-on-windows
*/

#include "LinkedList.h"
#include "menu.h"
#include <codecvt>
#include <cstdio>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <locale.h>
#include <windows.h>

#pragma execution_character_set( "utf-8" )

using namespace std;

void Print(const LinkedList* list)
{
	for (Node* node = list->head; node != nullptr; node = node->next)
	{
		cout << "\n" << node->Disciplina << " | " << node->ISBN << " | " << node->Titulo << " | " << node->Autor << " | " << node->Edicao << " | " << node->Cidade << " | " << node->Editora << " | " << node->Ano << " | " << node->Complementar << "\n";
	}
	std::cout << '\n';
}

void readData(LinkedList* list)
{
	string line;
	ifstream file;
	string Disciplina;
	string ISBN;
	string Titulo;
	string Autor;
	int Edicao;
	string Cidade;
	string Editora;
	int Ano;
	bool Complementar;
	string tempString;

	file.open("bibliografia.csv");
	while (getline(file, line))
	{
		stringstream inputString(line);

		getline(inputString, Disciplina, ';');
		getline(inputString, ISBN, ';');
		getline(inputString, Titulo, ';');
		getline(inputString, Autor, ';');

		getline(inputString, tempString, ';');
		Edicao = atoi(tempString.c_str());
		tempString = "";

		getline(inputString, Cidade, ';');
		getline(inputString, Editora, ';');

		getline(inputString, tempString, ';');
		Ano = atoi(tempString.c_str());
		tempString = "";

		getline(inputString, tempString, ';');
		if (tempString == "S") { Complementar = true; }
		else { Complementar = false; }

		line = "";

		Append(list, Disciplina, ISBN, Titulo, Autor, Edicao, Cidade, Editora, Ano, Complementar);
	}
	RemoveHead(list);
	file.close();
}

int main()
{
	SetConsoleOutputCP(65001);

	int opcao = 0;
	LinkedList* list = Create();

	cout << "\n\n***** INICIALIZANDO O PROGRAMA *****\n\n";

	while (opcao != 8)
	{
		opcao = Menu();
		switch (opcao)
		{
		case 1:
			readData(list);
			break;
		case 2:
			Print(list);
			break;
		case 3:
			analiseA(list);
			break;
		case 4:
			analiseB(list);
			break;
		case 5:
			analiseC(list);
			break;
		case 6:
			analiseD(list);
			break;
		case 7:
			analiseE(list);
			break;
		default:
			break;
		}
	}

	cout << "\n\n***** ENCERRANDO O PROGRAMA *****\n\n";

	Destroy(list);
	return 0;
}