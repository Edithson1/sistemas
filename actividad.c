#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Uso: %s <numero>\n", argv[0]);
        return 1;
    }

    int numero = atoi(argv[1]);
    int suma = 0;

    for (int i = 1; i <= numero; i++) {
        suma += i;
    }

    printf("%d\n", suma);

    return 0;
}
