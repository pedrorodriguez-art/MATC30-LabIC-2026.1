/*
Atividade 3 -> Intermediária = 1 ponto
A ordem lexicográfica é frequentemente conhecida como ordem alfabética quando estamos trabalhando com strings. Uma string é maior que outra string se ela aparece depois em uma lista ordenada lexicograficamente.

Dada uma palavra, crie uma nova palavra trocando alguns ou todos os seus caracteres. Essa nova palavra deve atender a dois critérios:

Deve ser maior que a palavra original.

Deve ser a menor palavra que atende à primeira condição.

Exemplo
w = abcd

A próxima maior palavra é abdc.

Construa uma função para criar e retornar a nova string que atende aos critérios. Se não for possível, retorne "no answer".

Descrição da função
A função possui o seguinte parâmetro:

string w: uma palavra

Retorno
string: a menor string lexicograficamente maior possível ou no answer

Formato de entrada
A primeira linha da entrada contém T, o número de casos de teste.

Cada uma das próximas T linhas contém w.

Restrições
1 ≤ T ≤ 10⁵

1 ≤ length of w ≤ 100

w conterá apenas letras no intervalo ascii [a..z].

Entrada de exemplo 0
5
ab
bb
hefg
dhck
dkhc
Saída de exemplo 0
ba
no answer
hegf
dhkc
hcdk
Explicação 0
Caso de teste 1:

ba é a única string que pode ser formada reorganizando ab. Ela é maior.

Caso de teste 2:

Não é possível reorganizar bb e obter uma string maior.

Caso de teste 3:

hegf é a próxima string maior que hefg.

Caso de teste 4:

dhkc é a próxima string maior que dhck.

Caso de teste 5:

hcdk é a próxima string maior que dkhc.

Entrada de exemplo 1
6
lmno
dcba
dcbb
abdc
abcd
fedcbabcd
Saída de exemplo 1
lmon
no answer
no answer
acbd
abdc
fedcbabdc
*/

#include <iostream>
using namespace std;

int nextPermutation(string &w) {
    int n = w.size();
    int i = n - 2;

    while (i >= 0 && w[i] >= w[i + 1]) {
        i--;
    }

    if (i < 0) return 0;

    int j = n - 1;
    while (w[j] <= w[i]) {
        j--;
    }

    char temp = w[i];
    w[i] = w[j];
    w[j] = temp;

    int l = i + 1;
    int r = n - 1;

    while (l < r) {
        char aux = w[l];
        w[l] = w[r];
        w[r] = aux;
        l++;
        r--;
    }

    return 1;
}

int main() {
    int T;
    cin >> T;

    string respostas[100000];

    for (int i = 0; i < T; i++) {
        string w;
        cin >> w;

        if (nextPermutation(w)) {
            respostas[i] = w;
        } else {
            respostas[i] = "no answer";
        }
    }
    for (int i = 0; i < T; i++) {
        cout << respostas[i] << endl;
    }

    return 0;
}