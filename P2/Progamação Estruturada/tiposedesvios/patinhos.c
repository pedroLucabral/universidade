#include <stdio.h>

int main() {
    unsigned long long int num, result;

    scanf("%llu", &num);
    while (num != -1) {
        if (num == 0) {
            printf("0\n");
            scanf("%llu", &num);
            continue;
        }
        result = (num - 1);
        printf("%llu\n", result);

        scanf("%llu", &num);
    }

    
    return 0;
}
