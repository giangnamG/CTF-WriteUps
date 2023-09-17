#include <stdio.h>
#include <unistd.h>

int main() {
    int secret_num = 123;

    char name[64] = {0};
    read(0, name, 64);
    printf("Hello ");
    printf(name);
    printf("! You'll never get my secret!\n");
    return 0;
}