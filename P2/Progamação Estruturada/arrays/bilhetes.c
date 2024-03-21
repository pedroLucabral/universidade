#include <stdio.h>

int main() {
    int n, m, x;

    scanf("%d %d", &n, &m);

    while (n != 0 && m != 0) {
        int vetor[10000] = {0}, cont = 0;
        
        for (int i = 0; i < m; i++) {
            scanf("%d", &x);
            vetor[x-1]++;
        }
        for (int i = 0;i < n; i++) {
            if (vetor[i] >= 2) {
                cont++;
            }

        }
        printf("%d\n", cont);
        scanf("%d %d", &n, &m);
    }
    
    return 0;
}