#include <stdio.h>
 
int main() {

    int num1, num2;
    int coelhos = 0, ratos = 0, sapos = 0;
    int total = 0;
    char letter;

    scanf("%d", &num1);

    for (int i = 0; i < num1; i++) {
        scanf("%d %c", &num2, &letter);
        
        total += num2;

            switch (letter) {
                case 'C':
                    coelhos += num2;
                    break;
                case 'R':
                    ratos += num2;
                    break;
                case 'S':
                    sapos += num2;
                    break;
            }
        }


    printf("Total: %d cobaias\n", total);
    printf("Total de coelhos: %d\n", coelhos);
    printf("Total de ratos: %d\n", ratos);
    printf("Total de sapos: %d\n", sapos);
    printf("Percentual de coelhos: %.2f %%\n", coelhos * (100.0 / total));
    printf("Percentual de ratos: %.2f %%\n", ratos * (100.0 / total));
    printf("Percentual de sapos: %.2f %%\n", sapos * (100.0 / total));

    


    return 0;
}

