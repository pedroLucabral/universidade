#include <stdio.h>

unsigned long long int FibonacciEmVetor(int n){
    unsigned long long int first=0, second=1, new;
    
    if (n == 0){
        return 0;
        
    } else if (n == 1){
        return 1;
        
    } else {
        for (int i = 2; i <= n; i++){
            new = first + second;
            first = second;
            second = new;
        }
    }
    
    return second;
}

int main(){
    int casosTeste, num;
    unsigned long long int fib;

    scanf("%d", &casosTeste);

    for (;casosTeste--;){
        scanf("%d", &num);

        fib = FibonacciEmVetor(num);
        printf("Fib(%d) = %llu\n", num, fib);
    }

    return 0;
}