#include<bits/stdc++.h>
using namespace std;
int main()
{	
	double start = clock();
   	for(int i=1;i<=1000000;i++)
   		i = i;
    double end = clock();
    cout<<"Thoi gian chay factorial(n): "<<(double)(end - start) / CLOCKS_PER_SEC<<"\n";
}