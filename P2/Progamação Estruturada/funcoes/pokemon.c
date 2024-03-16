#include <stdio.h>

int ValorGolpe(int bonus, int ataque, int defesa, int level) {
    if (level % 2 == 0) {
        return (ataque + defesa) / 2 + bonus;
    } else {
        return (ataque + defesa) / 2;
    }
}  

int main() {
    int n, bonus;
    int atk1, def1, lvl1;
    int atk2, def2, lvl2;
    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        scanf("%d", &bonus);

        scanf("%d %d %d", &atk1, &def1, &lvl1);
        scanf("%d %d %d", &atk2, &def2, &lvl2);
        
        if (ValorGolpe(bonus, atk1, def1, lvl1) > ValorGolpe(bonus, atk2, def2, lvl2)) {
            printf("Dabriel\n");
        } else if (ValorGolpe(bonus, atk1, def1, lvl1) < ValorGolpe(bonus, atk2, def2, lvl2)) {
            printf("Guarte\n");
        } else {
            printf("Empate\n");
        }
        
    }

    
    
    return 0;
}
