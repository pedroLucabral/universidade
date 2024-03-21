#include <stdio.h>

int main() {
    int multiplos[4] = {0}, n;

    scanf("%d", &n);
    int vetor[n];

    for (int i = 0; i < n; i++) {
        scanf("%d", &vetor[i]);
    }

    for (int i = 2; i < 6; i++) {
        for (int j = 0; j < n; j++) {
            if (vetor[j] % i == 0) {
                multiplos[i-2]++;
            }
        }
    }

    for (int i = 0; i < 4; i++) {
        printf("%d Multiplo(s) de %d\n", multiplos[i], i+2);
    }
    
    return 0;
}