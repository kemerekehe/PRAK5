#include <stdio.h>

//Fungsi MaxBilangan//
int hasil;
int MaxBilangan (int, int, int, int);
int MaxBilangan(int a, int b, int c, int d) {
    if (a>b && a>c && a>d) {
        hasil=a;}
    else if (b>c && b>d && b>a) {
        hasil=b;}
    else if (c>b && c>d && c>a) {
        hasil=c;}
    else if (d>b && d>c && d>a) {
        hasil=d;}
}

int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int hasil = MaxBilangan(a, b, c, d);
    printf("%d", hasil);
    return 0;
}