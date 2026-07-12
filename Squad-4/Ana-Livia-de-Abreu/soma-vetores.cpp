#include <iostream>
#include <vector>


int somaArray(const std::vector<int>& ar) {
    int soma = 0;
    for (int valor : ar) {
        soma += valor;
    }
    return soma;
}

int main() {
    int n;
    
    
    if (!(std::cin >> n)) return 1;

    std::vector<int> ar(n);


    for (int i = 0; i < n; i++) {
        std::cin >> ar[i];
    }

    
    std::cout << somaArray(ar) << "\n";

    return 0;
}
