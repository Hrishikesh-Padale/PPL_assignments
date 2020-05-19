#include<stdio.h>

fact (int n)  
    {  
       if (n<=1)  
           return 1;  
       else   
           return (n * fact(n-1));  
    }  

int main()
{
	int num;
	num = fact(6);
	printf("%d",num);
	return 0;
} 
