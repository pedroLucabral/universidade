#include <stdio.h>

int main() {

    int i, j, m, n, a, b, qtd;

    qtd = 0;

    scanf("%d%d\n%d\n%d", &m, &n, &a, &b);

    for (i=m; i<=n; i+=a) {
        for (j=m; j<=n; j+=b) {
            if (i==j) {
                qtd++;

            }

        }

    }

    printf("%d\n", qtd);



    return 0;
}
