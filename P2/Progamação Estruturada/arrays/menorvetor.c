#include <stdio.h>

int main() {
    int n, menor = 999999, posicao;

    scanf("%d", &n);

    int vetor[n];

    for (int i = 0; i < n; i++) {
        scanf("%d", &vetor[i]);
    }

    for (int i = 0; i < n; i++) {
        if (vetor[i] < menor) {
            menor = vetor[i];
            posicao = i;
        }
    
    }

    printf("Menor valor: %d\n", menor);
    printf("Posicao: %d\n", posicao);

    return 0;
}