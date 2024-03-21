#include <stdio.h>

int main() {
    long int n;
    int t;

    scanf("%d\n%ld", &t, &n);

    int vetor[n][60], tamanhoVetor[n];
    for (int i = 0; i < n; i++) {
        scanf("%d", &tamanhoVetor[i]);
        for (int j = 0; j < tamanhoVetor[i]; j++) {
            scanf("%d", &vetor[i][j]);
        }
        
    }

    long int q;
    int operacao, array1, array2;

    scanf("%ld", &q);

    for (int i = 0; i < q; i++) {
        int intersec = 0, uniao = 0;
        scanf("%d %d %d", &operacao, &array1, &array2);

        if (operacao == 1) {
            for (int j = 0; j < tamanhoVetor[array1 - 1]; j++) {
                for (int k = 0; k < tamanhoVetor[array2 - 1]; k++) {
                    if (vetor[array1 - 1][j] == vetor[array2 - 1][k]) {
                        intersec++;
                        break;
                    }
                }
            }
            printf("%d\n", intersec);
        } else if (operacao == 2) {
            uniao = tamanhoVetor[array1 - 1];
            for (int j = 0; j < tamanhoVetor[array2 - 1]; j++) {
                int naUniao = 0;

                for (int k = 0; k < tamanhoVetor[array1 - 1]; k++) {
                    if (vetor[array2 - 1][j] == vetor[array1 - 1][k]) {
                        naUniao = 1;
                        break;
                    }
                }

            if (!naUniao) {
                uniao++;
            }
            }
            printf("%d\n", uniao);
        }

    }

    return 0;
}