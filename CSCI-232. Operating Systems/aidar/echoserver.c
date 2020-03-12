#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <sys/time.h>
#include <netinet/in.h>

#include <sys/wait.h>
#include <fcntl.h>

#include <pthread.h>

#define	QLEN 5
#define	BUFSIZE	4096
#define NUMCHAR 2048
#define MAXQUES 256
#define MAXLINES 1024

pthread_t tid;

pthread_mutex_t firstMutex;
pthread_mutex_t secMutex;
pthread_mutex_t thirdMutex;
pthread_mutex_t forthMutex;
pthread_mutex_t forAll;
pthread_mutex_t us;
pthread_mutex_t usa;
pthread_mutex_t last;

//copied from the book
int done = 0;

pthread_cond_t c = PTHREAD_COND_INITIALIZER;
pthread_mutex_t m = PTHREAD_MUTEX_INITIALIZER;

pthread_cond_t k = PTHREAD_COND_INITIALIZER;
pthread_mutex_t r = PTHREAD_MUTEX_INITIALIZER;
//

char *winName[NUMCHAR];
int winScore[NUMCHAR];

int numClients = 0, maxClients = 0, howMany = 0;
int checker = 0, count = 0;

char *allLines[MAXLINES];
char *ans[MAXQUES];
char *ques[MAXQUES];

char winner[NUMCHAR];

int passivesock(char *service, char *protocol, int qlen, int *rport);

void *doAction(void *ptr){

    char buf[BUFSIZE], *token;
    int	cc, ssock = *(int*)ptr, increm = 0, score = 0;
    char *rgv[24];
    
    int points = 0;
    
    for(int i = 0; i < 24; i++){
        rgv[i] = '\0';
    }

    pthread_mutex_lock(&firstMutex);
    numClients++;
    pthread_mutex_unlock(&firstMutex);
    
    if (numClients == 1){
        
        write(ssock, "QS|ADMIN\n", 9);
        read(ssock, buf, BUFSIZE);
        
	    buf[strcspn(buf, "\n")] = '\0';
		buf[strcspn(buf, "\r")] = '\0';
		
		pthread_mutex_lock(&secMutex);
		token = strtok(buf, "|");
		
		while(token != NULL) {
		    rgv[increm] = (char *) malloc(strlen(token));
		    strcpy(rgv[increm], token);
		    increm++;
            token = strtok(NULL, "|");
	    }
	    increm--;
	    
	    maxClients = atoi(rgv[2]);
	    pthread_mutex_unlock(&secMutex);
	    
	    write(ssock, "WAIT\n", 5);
	    
	    pthread_mutex_lock(&m);
	    if(maxClients != 1){
	        pthread_cond_wait(&c, &m);
        }
		pthread_mutex_unlock(&m);
	    
	    //QUESTIONS
	    int u = 0, h = 0, step = 0;
	    while(ques[u] != NULL) {
	    
	        write(ssock, "QUES|", 5);
	        char si[strlen(ques[u])];
	        sprintf(si, "%i", strlen(ques[u]));
	        write(ssock, si, strlen(si));
	        write(ssock, "|", 1);
	        
	        for(; h < howMany; h++) {
	            if(strcmp(allLines[h], ans[u]) == 0){
	                break;
	            } else {
	                write(ssock, allLines[h], strlen(allLines[h]));
	                write(ssock, "\n", 1);
	            }
	        }
	        h++;
	        step = u + 1;
	        
	        cc = read(ssock, buf, BUFSIZE);
	        pthread_mutex_lock(&us);
	        done++;
	        pthread_mutex_unlock(&us);
	        
	        buf[strcspn(buf, "\n")]= '\0';
	        buf[strcspn(buf, "\r")]= '\0';
	        
	        pthread_mutex_lock(&forAll);
		    token = strtok(buf, "|");
		    
	        if(strcmp(token, "NOANS") == 0) {
                points += 0;
	        }
	        else if(strcmp(token, ans[u]) == 0) {
	            pthread_mutex_lock(&usa);
	            checker++;
	            pthread_mutex_unlock(&usa);
	            
	            if(checker == 1) {
	                strcpy(winner, rgv[1]);
	                points++;
	            }
	            
	            points++;
	        }
	        else if(strcmp(token, ans[u]) != 0) {
	            points--;
	        }
	        pthread_mutex_unlock(&forAll);
	        
	        pthread_mutex_lock(&r);
		    if(done != numClients * step){
			    pthread_cond_wait(&k, &r);
		    } else {
		        pthread_cond_broadcast(&k);
		    }
		    pthread_mutex_unlock(&r); 
            
            write(ssock, "WIN", 3);
            write(ssock, "|", 1);
            write(ssock, winner, strlen(winner));
            write(ssock, "\n", 1);
            
            checker = 0;
	        u++;
	    }
	    printf("Name %s Points %d.\n", rgv[1], points);
	    close(ssock);
    }
    else if (maxClients < numClients){
        
        pthread_mutex_lock(&thirdMutex);
        numClients--;
        pthread_mutex_unlock(&thirdMutex);
        
        write(ssock, "QS|FULL\n", 8);
		close(ssock);    
    }
    else {
        write(ssock, "QS|JOIN\n", 8);
        read(ssock, buf, BUFSIZE);
        
        buf[strcspn(buf, "\n")] = '\0';
		buf[strcspn(buf, "\r")] = '\0';
		
		pthread_mutex_lock(&forthMutex);
		token = strtok(buf, "|");
		
		while(token != NULL) {
		    rgv[increm] = (char *) malloc(strlen(token));
		    strcpy(rgv[increm], token);
		    increm++;
            token = strtok(NULL, "|");
	    }
	    increm--;

	    pthread_mutex_unlock(&forthMutex);
	    
	    write(ssock, "WAIT\n", 5);
	    
	    pthread_mutex_lock(&m);
	    
		if(numClients == maxClients){
			pthread_cond_broadcast(&c);
		} else {
		    pthread_cond_wait(&c, &m);
		}
		
		pthread_mutex_unlock(&m);
		
	    //QUESTIONS
	    int u = 0, h = 0, step = 0;
	    while(ques[u] != NULL) {
	    
	        write(ssock, "QUES|", 5);
	        char si[strlen(ques[u])];
	        sprintf(si, "%i", strlen(ques[u]));
	        write(ssock, si, strlen(si));
	        write(ssock, "|", 1);
	        
	        for(; h < howMany; h++) {
	            if(strcmp(allLines[h], ans[u]) == 0){
	                break;
	            } else {
	                write(ssock, allLines[h], strlen(allLines[h]));
	                write(ssock, "\n", 1);
	            }
	        }
	        h++;
	        step = u + 1;
	       
	        cc = read(ssock, buf, BUFSIZE);
	        pthread_mutex_lock(&us);
	        done++;
	        pthread_mutex_unlock(&us);
	        
	        buf[strcspn(buf, "\n")]= '\0';
	        buf[strcspn(buf, "\r")]= '\0';
	        
	        pthread_mutex_lock(&forAll);
		    token = strtok(buf, "|");
		    
	        if(strcmp(token, "NOANS") == 0) {
                points += 0;
	        }        
	        else if(strcmp(token, ans[u]) == 0) {
	        	pthread_mutex_lock(&usa);
	            checker++;
	            pthread_mutex_unlock(&usa);
	            
	            if(checker == 1) {
	                strcpy(winner, rgv[1]);
	                points++;
	            }
	            
	            points++;

	        }
	        else if(strcmp(token, ans[u]) != 0) {
	            points--;
	        }
	        pthread_mutex_unlock(&forAll);
	        
	        pthread_mutex_lock(&r);
		    if(done != numClients * step){
			    pthread_cond_wait(&k, &r);
		    } else {
		        pthread_cond_broadcast(&k);
		    }
		    pthread_mutex_unlock(&r); 
		    
            write(ssock, "WIN", 3);
            write(ssock, "|", 1);
            write(ssock, winner, strlen(winner));
            write(ssock, "\n", 1);
            
            checker = 0;
	        u++;
	        
	    }
        printf("Name %s Points %d.\n", rgv[1], points);
	    close(ssock);
    } 
}

int main(int argc, char *argv[]) {
	
	char buf[BUFSIZE];
	char *service;
	
	struct sockaddr_in fsin;
	
	int	alen, msock, ssock, rport = 0;
	int	cc, status, fEx = 0;
    FILE* fp;
	
	switch (argc) {
		case 1:
			
			rport = 1;
			break;
		case 2:

			rport = 1;
			fEx = 1;
            fp = fopen(argv[1], "r");
            
			break;
		case 3:
		
		    service = argv[2];
		    fEx = 1;
            fp = fopen(argv[1], "r");
            
			break;
		default:
			
			fprintf(stderr, "Usage: server [port]\n");
			exit(-1);
	}

	msock = passivesock(service, "tcp", QLEN, &rport);
	if (rport)
	{

		printf("Server: port %d\n", rport);	
		fflush(stdout);
	}

    pthread_mutex_init(&firstMutex, NULL);
    pthread_mutex_init(&secMutex, NULL);
    pthread_mutex_init(&thirdMutex, NULL);
    pthread_mutex_init(&forthMutex, NULL);
    pthread_mutex_init(&forAll, NULL);
    pthread_mutex_init(&us, NULL);
    pthread_mutex_init(&usa, NULL);
    pthread_mutex_init(&last, NULL);
    
    for(int q = 0; q < MAXLINES; q++){
        allLines[q] = NULL;
    }
    
    for(int r = 0; r < MAXQUES; r++){
        ans[r] = NULL;
        ques[r] = NULL;
    }
    
    int i = 0, j = 0, k = 0;
    int chAns = 0, question = 1;
    char line[NUMCHAR];
    
    if(fEx == 1) {
        while(fgets(line, NUMCHAR, fp) != NULL){
                
            if(strcmp(line,"\n") != 0){
            
                line[strcspn(line, "\n")] = '\0';
		        line[strcspn(line, "\r")] = '\0';
		        
                if(chAns == 0 && question == 1) {
                    ques[k] = (char *) malloc(strlen(line));
                    strcpy(ques[k], line);
                    k++;
                    
                    question = 0;  
                }
                
                if(chAns == 1){
                    ans[j] = (char *) malloc(strlen(line));
                    strcpy(ans[j], line);
                    j++;
                }
                
                allLines[i] = (char *) malloc(strlen(line));
                strcpy(allLines[i], line);
                i++;
                howMany++;
            }
            else {
                if(chAns == 0){
                    chAns = 1;
                    question = 1;
                }
                else {
                    chAns = 0;
                }
            }
        }
    }    

	for (;;) {
		int	ssock;
		alen = sizeof(fsin);
		ssock = accept(msock, (struct sockaddr *)&fsin, &alen);
		
		if (ssock < 0) {
		    fprintf(stderr, "accept: %s\n", strerror(errno));
			exit(-1);
		}
		
		status = pthread_create(&tid, NULL, doAction, &ssock);
		if (status != 0) {
			printf("Pthread_create error %d\n", status);
			exit(-1);
		}
	}
	
	
	pthread_mutex_destroy(&firstMutex);
	pthread_mutex_destroy(&secMutex);
	pthread_mutex_destroy(&thirdMutex);
	pthread_mutex_destroy(&forthMutex);
	pthread_mutex_destroy(&forAll);
	pthread_mutex_destroy(&us);
	pthread_mutex_init(&usa, NULL);
	pthread_mutex_init(&last, NULL);
	
	pthread_exit(0);
	fclose(fp);
    	
	return 0;
}
