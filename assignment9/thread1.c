#include<stdio.h>
#include<pthread.h>
#include<unistd.h>

void *Myfunction(void *arg) {
	
	while(1) {
		printf("Hello\n");
		sleep(1);
	}
	
	return NULL;
}

int main() {

	pthread_t thread_id;
	pthread_create(&thread_id, NULL, Myfunction, NULL);
	pthread_join(thread_id, NULL);
	
	return 0;
}
