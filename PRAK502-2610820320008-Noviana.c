#include <stdio.h> 
#include <math.h> 

int hitung(int nilai1, int nilai2){ 
    int hasil = nilai1 - nilai2;
    return (hasil < 0) ? -hasil : hasil;
} 
int mutlak(int angka){ 
        return (angka < 0) ? -angka : angka;
    }
int main() 
{
int a,b,c,d; 

    scanf("%d",&a); 
    scanf("%d",&c); 
    scanf("%d",&b); 
    scanf("%d",&d); 

int Hasil = hitung(a,b) + hitung(c,d); 
printf("%d",mutlak(Hasil)); 

return 0; 
}