#include <stdio.h>

int main() {
    int vetor[10], n;

    for (int i = 0; i < 10; i++) {
        scanf("%d", &n);
        vetor[i] = n;
    }

    for (int j = 0; j < 10; j++) {
        if (vetor[j] <= 0 || vetor[j] == 0) {
            vetor[j] = 1;
        }
        printf("X[%d] = %d\n", j, vetor[j]);
    }
    
    return 0;
}