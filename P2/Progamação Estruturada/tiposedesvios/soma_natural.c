#include <stdio.h>

int main() {
    unsigned long long int start, end, N, result;

    scanf("%llu %llu", &start, &end);

    N = (end - start) + 1;

    result = (N * (start + end)) / 2;
    
    printf("%llu\n", result);
    return 0;
}
