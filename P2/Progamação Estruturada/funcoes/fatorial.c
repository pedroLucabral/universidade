#include <stdio.h>

long long int Fatorial(int n) {
    if (n == 0) {
        return 1;
    } else {
        return n * Fatorial(n - 1);
    }
}

int main() {
    int n1, n2;
    long long int resultado;

    while (scanf("%d %d", &n1, &n2) != EOF)
    {
        resultado = Fatorial(n1) + Fatorial(n2);
        printf("%lld\n", resultado);
    }
    
    return 0;
}
