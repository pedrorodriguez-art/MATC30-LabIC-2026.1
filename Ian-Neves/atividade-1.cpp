/*Construa uma função para calcular a soma de dois números inteiros.

Exemplo
a = 7
b = 3

Retorne 10.

Descrição da função
Complete a função com os seguintes parâmetros:

int a: o primeiro valor
int b: o segundo valor

Retorno
int: a soma de a e b

Restrições
1 ≤ a, b ≤ 1000

Entrada de exemplo
a = 2
b = 3
Saída de exemplo
5
Explicação
2 + 3 = 5.
*/

#include <iostream>
using namespace std;

int soma(int a, int b) {
    return a + b;
}

int main() {
    int a, b;

    cin >> a;
    cin >> b;

    cout << soma(a, b) << endl;

    return 0;
}