#include <stdio.h>

int  main(void) {

    int qtd, r1, r2, r3;

    scanf("%d", &qtd);

    while (qtd > 0) {

        scanf("%d%d", &r1, &r2);
        printf("%d\n", r1 + r2);
        qtd--;
    }

    return 0;
}
