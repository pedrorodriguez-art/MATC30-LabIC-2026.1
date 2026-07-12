#include <stdio.h>
#include <string.h>

void swap(char* a, char* b) {
    char tmp = *a;
    *a = *b;
    *b = tmp;
}

void ordenar(char* w, int inicio, int fim) {
    // bubble sort simples do trecho w[inicio..fim]
    for (int i = inicio; i < fim; i++) {
        for (int j = inicio; j < fim - (i - inicio); j++) {
            if (w[j] > w[j + 1]) {
                swap(&w[j], &w[j + 1]);
            }
        }
    }
}

void biggerIsGreater(char* w, char* resultado) {
    int n = strlen(w);
    int i = n - 2;

    while (i >= 0 && w[i] >= w[i + 1]) {
        i--;
    }

    if (i < 0) {
        strcpy(resultado, "no answer");
        return;
    }

    int j = n - 1;
    while (w[j] <= w[i]) {
        j--;
    }

    swap(&w[i], &w[j]);
    ordenar(w, i + 1, n - 1);

    strcpy(resultado, w);
}

int main() {
    int t;
    scanf("%d", &t);

    while (t--) {
        char w[105];
        char resultado[105];
        scanf("%s", w);

        biggerIsGreater(w, resultado);
        printf("%s\n", resultado);
    }

    return 0;
}