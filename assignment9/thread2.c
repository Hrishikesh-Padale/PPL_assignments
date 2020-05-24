#include <pthread.h> 
#include <stdio.h> 
#include <stdlib.h> 
#include <unistd.h> 

pthread_t thread[2]; 
pthread_mutex_t lock; 

void *myFunction(int arg) {

	pthread_mutex_lock(&lock); 
	
	int val = arg;

	if(val == 0) {
		printf("Hello World\n");
	}
	
	else if (val == 1) {
		printf("Goodbye World\n");
	}
	
	pthread_mutex_unlock(&lock); 
	sleep(1);
	

} 

int main() {
 
	int i = 0;  

	while(1) {
		i = 0;
		while (i < 2) { 
			pthread_create(&(thread[i]), NULL, &myFunction, &i); 
			pthread_join(thread[i], NULL); 
			i++; 
		} 
	}
	
	pthread_mutex_destroy(&lock); 

	return 0; 
} 
