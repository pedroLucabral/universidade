#include <stdio.h>
#include <math.h>

int ResolveEquacao2Grau(float a, float b, float c, float *x1, float *x2) {
    float del;
    
    if (a == 0) {
        return -1;
    }

    del = b*b - 4*a*c;

    if (del < 0) {
        return -2;
    }

    *x1 = (-b + sqrt(del)) / (2*a);
    *x2 = (-b - sqrt(del)) / (2*a);

    return 0;
}

int main() {
    float a, b, c, r1, r2;
    int resultado;

    printf("Digite os valores das variaveis:\n");
    scanf("%f %f %f", &a, &b, &c);

    resultado = ResolveEquacao2Grau(a, b, c, &r1, &r2);

    switch (resultado)
    {
    case -1:
        printf("Nao eh equacao de segundo grau");
        break;
    case -2:
        printf("A equacao nao tem raizes reais");
        break;
    case 0:
        printf("Raiz 1: %.2f\nRaiz 2: %.2f\n", r1, r2);
        break;
    default:
    printf("Algo inesperado aconteceu");
        break;
    }
    
    return resultado;
}