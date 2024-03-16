#include <stdio.h>
#include <math.h>

int EhPrimo(int n) {
    long long int ehPrimo = 1;

    for (int i = 2; i <= sqrt(n); i++) {
        if (!(n % i)) {
            ehPrimo = 0;
            break;
        }
    }

    return ehPrimo;
}

int main() {
    int n;
    long long int number;

    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%lld", &number);
        if (EhPrimo(number)) {
            printf("Prime\n");
        } else {
            printf("Not Prime\n");
        }
    }

    return 0;
}
