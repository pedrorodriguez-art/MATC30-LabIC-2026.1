/*
Atividade 4 -> Avançada = 7 pontos
David possui vários contêineres, cada um com uma quantidade de bolas. Ele possui contêineres suficientes para ordenar cada tipo de bola em seu próprio contêiner. David deseja organizar as bolas usando seu método de ordenação.

David deseja realizar uma quantidade de operações de troca de forma que:

Cada contêiner contenha apenas bolas do mesmo tipo.

Nenhuma bola do mesmo tipo esteja localizada em contêineres diferentes.

Exemplo
containers = [[1, 4], [2, 3]]

image.png


David possui n = 2 contêineres e 2 tipos diferentes de bolas, ambos numerados de 0 até n − 1 = 1. A distribuição dos tipos de bolas por contêiner é mostrada no diagrama do enunciado.

Em uma única operação, David pode trocar duas bolas localizadas em contêineres diferentes.

O diagrama do enunciado representa uma única operação de troca.

image.png
Nesse caso, não há como colocar todas as bolas verdes em um contêiner e todas as bolas vermelhas no outro usando apenas operações de troca. Retorne Impossible.

Você deve executar q consultas, em que cada consulta está na forma de uma matriz, M. Para cada consulta, imprima Possible em uma nova linha se David puder satisfazer as condições acima para a matriz dada. Caso contrário, imprima Impossible.

Descrição da função
Complete a função organizingContainers no editor abaixo.

organizingContainers possui o seguinte parâmetro:

int container[n][m]: um array bidimensional de inteiros que representa o número de bolas de cada cor em cada contêiner

Retorno
string: Possible ou Impossible

Formato de entrada
A primeira linha contém um inteiro q, o número de consultas.

Cada um dos próximos q conjuntos de linhas é apresentado da seguinte forma:

A primeira linha contém um inteiro n, o número de contêineres, ou seja, linhas, e de tipos de bolas, ou seja, colunas.

Cada uma das próximas n linhas contém n inteiros separados por espaço, descrevendo a linha containers[i].

Restrições
1 ≤ q ≤ 10

1 ≤ n ≤ 100

0 ≤ containers[i][j] ≤ 10⁹

Pontuação
Para 33% da pontuação, 1 ≤ n ≤ 10.

Para 100% da pontuação, 1 ≤ n ≤ 100.

Formato de saída
Para cada consulta, imprima Possible em uma nova linha se David puder satisfazer as condições acima para a matriz dada. Caso contrário, imprima Impossible.

Entrada de exemplo 0
2
2
1 1
1 1
2
0 2
1 1
Saída de exemplo 0
Possible
Impossible
Explicação 0
Executamos as seguintes q = 2 consultas:

O diagrama do enunciado representa uma forma possível de satisfazer os requisitos de David para a primeira consulta.

image.png
Assim, imprimimos Possible em uma nova linha.

O diagrama do enunciado representa a matriz da segunda consulta.

image.png
Não importa quantas vezes troquemos bolas do tipo t₀ e t₁ entre os dois contêineres, nunca terminaremos com um contêiner contendo apenas bolas do tipo t₀ e o outro contêiner contendo apenas bolas do tipo t₁. Assim, imprimimos Impossible em uma nova linha.

Entrada de exemplo 1
2
3
1 3 1
2 1 2
3 3 3
3
0 2 1
1 1 1
2 0 0
Saída de exemplo 1
Impossible
Possible
*/

#include <iostream>
using namespace std;

const int MAX = 100;

void ordenar(int v[], int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n - 1; j++) {
            if (v[j] > v[j + 1]) {
                int temp = v[j];
                v[j] = v[j + 1];
                v[j + 1] = temp;
            }
        }
    }
}
string organizingContainers(int n, int container[MAX][MAX]) {
    int somaLinhas[MAX] = {0};
    int somaColunas[MAX] = {0};

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            somaLinhas[i] += container[i][j];
        }
    }
    for (int j = 0; j < n; j++) {
        for (int i = 0; i < n; i++) {
            somaColunas[j] += container[i][j];
        }
    }
    ordenar(somaLinhas, n);
    ordenar(somaColunas, n);

    for (int i = 0; i < n; i++) {
        if (somaLinhas[i] != somaColunas[i]) {
            return "Impossible";
        }
    }
    return "Possible";
}

int main() {
    int q;
    cin >> q;

    string respostas[10];

    for (int k = 0; k < q; k++) {
        int n;
        cin >> n;

        int container[MAX][MAX];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                cin >> container[i][j];
            }
        }
        respostas[k] = organizingContainers(n, container);
    }

    for (int i = 0; i < q; i++) {
        cout << respostas[i] << endl;
    }

    return 0;
}