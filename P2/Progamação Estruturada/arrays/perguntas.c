#include <stdio.h>

int main() {
    int n, k, x;

    scanf("%d %d", &n, &k);
    while (n != 0 && k != 0) {
        int vetor[100] = {0}, cont = 0;

        for (int i = 0; i < n; i++) {
        
            scanf("%d", &x);
            vetor[x-1]++;
        }
        for (int i = 0; i < 100; i++) {
            if (vetor[i] >= k) {
                cont++;
            }
        }
        printf("%d\n", cont);
    
        scanf("%d %d", &n, &k);
    } 
    return 0;
}