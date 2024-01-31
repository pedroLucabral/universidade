#include <stdio.h>

int  main(void) {

    int qtd, num;

    scanf("%d", &qtd);

    while (qtd > 0) {
        scanf("%d", &num);
        if (num == 0) {
            printf("NULL\n");

        }else if (-num%2 == 0) {
            if (num > 0) {
                printf("EVEN POSITIVE\n");
            } else {
                printf("EVEN NEGATIVE\n");

            }

        }else if (-num%2 != 0) {
            if (num > 0) {
                printf("ODD POSITIVE\n");
            } else {
                printf("ODD NEGATIVE\n");

            }

        }
        qtd--;

    }

    return 0;
}
