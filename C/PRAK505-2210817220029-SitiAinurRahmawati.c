#include <stdio.h>
void Biodata(int, char[], char[]);
void Biodata(int a, char b[], char c[]){
    int tahun_sekarang = 2020;
    printf("Perkenalkan Nama Saya : %s\n", b);
    printf("Umur saya : %i\n", tahun_sekarang-a);
    printf("Saya adalah angkatan : %i\n", tahun_sekarang);
    printf("Asal saya dari : %s\n", c);
}
int main() {
    int tahunLahir;
    char A[20], B[15];
    scanf(" %d",&tahunLahir);
    scanf(" %[^\n]%*c",&A);
    scanf(" %[^\n]%*c",&B);
    Biodata(tahunLahir, A, B);
    return 0;
}
