#include <stdio.h>

int  main(void) {

    int tests, days;
    float amt;

    scanf("%d", &tests);

    while (tests > 0) {

        scanf("%f", &amt);
        days = 0;
        while (amt > 1.0) {
            days++;
            amt = amt/2;
        }
        printf("%d dias\n", days);
        tests--;
    }

}
