#include <stdio.h>

int main() {
    int vetor[2000] = {0}, n, x;

    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        scanf("%d", &x);
        vetor[x-1]++;
    }

    for (int i = 0; i < 2000; i++) {
        if (vetor[i] != 0) {
            printf("%d aparece %d vez(es)\n", i+1, vetor[i]);
        }
    }

    return 0;
}