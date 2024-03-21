#include <stdio.h>

int main() {
    int n, vetor[20];

    for (int i = 0; i < 20; i++) {
        scanf("%d", &vetor[i]);
    }

    for (int i = 0; i < 10; i++) {
        n = vetor[i];
        vetor[i] = vetor[19-i];
        vetor[19-i] = n;
    }

    for (int i = 0; i < 20; i++) {
        printf("N[%d] = %d\n", i, vetor[i]);
    }

    return 0;
}