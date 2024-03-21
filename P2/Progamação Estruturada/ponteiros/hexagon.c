#include <stdio.h>
#include <math.h>

void CalculaHexagono(float l, float *area, float *perimetro) {
    *area = (3*(l*l)*sqrt(3))/2;
    *perimetro = 6*l;
}

int main() {
    float l, area, perimetro;

    printf("Digite o tamanho do lado do hexagono\n");
    scanf("%f", &l);

    CalculaHexagono(l, &area, &perimetro);

    printf("Area: %.2f\nPerimetro: %.2f", area, perimetro);
    
    return 0;
}