#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void print_flag(void) {
    char flag[256];
    FILE *flptr = fopen("SECRETO/flag.txt", "r");
    fgets(flag, 256, flptr);
    printf("%s\n", flag);
    exit(0);
}

void vuln(void) {
    int changeme = 0;
    char input[64];

    puts("Solo un 1337 h4xx0r puede tener la flag.");

    // No entiendo porqué me han dicho que use fgets,
    // si gets funciona y es más fácil de usar...
    gets(input); 

    if (changeme!=0) {
        printf("Se ha cambiado la variable: 0x%llX\n", changeme);
        print_flag();
    } else {
        puts("No se ha cambiado la variable");
        exit(0);
    }
}

int main(void) {
    vuln();
    return 0;
}
