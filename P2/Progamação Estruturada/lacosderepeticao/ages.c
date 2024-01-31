#include <stdio.h>

int main() {

    int idade, qtd = 0;
    float media = 0.0;

    scanf("%d", &idade);

    while (idade >= 0) {

        media += idade;
        qtd++;
        scanf("%d", &idade);
    }

    printf("%.2f\n", media/qtd);

    return 0;
}
