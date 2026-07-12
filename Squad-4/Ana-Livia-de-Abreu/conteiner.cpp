#include <stdio.h>
#include <string.h>

void ordenarLong(long long arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - 1 - i; j++) {
            if (arr[j] > arr[j + 1]) {
                long long tmp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = tmp;
            }
        }
    }
}

void organizingContainers(long long containers[][100], int n, char* resultado) {
    long long capacidadeContainer[100] = {0};
    long long totalPorTipo[100] = {0};

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            capacidadeContainer[i] += containers[i][j];
            totalPorTipo[j] += containers[i][j];
        }
    }

    ordenarLong(capacidadeContainer, n);
    ordenarLong(totalPorTipo, n);

    int igual = 1;
    for (int i = 0; i < n; i++) {
        if (capacidadeContainer[i] != totalPorTipo[i]) {
            igual = 0;
            break;
        }
    }

    strcpy(resultado, igual ? "Possible" : "Impossible");
}

int main() {
    int q;
    scanf("%d", &q);

    while (q--) {
        int n;
        scanf("%d", &n);

        long long containers[100][100];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                scanf("%lld", &containers[i][j]);

        char resultado[20];
        organizingContainers(containers, n, resultado);
        printf("%s\n", resultado);
    }

    return 0;
}