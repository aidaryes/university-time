/*
 ============================================================================
 Name        : osFirstLab.c
 Author      : Aidar Yes
 Version     :
 Copyright   : Your copyright notice
 Description : Hello World in C, Ansi-style
 ============================================================================
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>


#define MAX_LINES 10
#define BUFSZ 128

void reverse(char **stri){
	char* str = *stri;
	int len = strlen(str);
	char *anStr = (char *) malloc(strlen(str));

	int i;
	for(i = 0; i<len; i++){
		anStr[i] = str[len - i - 1];
	}

	anStr[i] = '\0';
	free(*stri);
	*stri = anStr;
}

int main(void) {

	int	i = 0, count = 0;
	char *lines[MAX_LINES];
	char buf[BUFSZ];
	FILE *fp;

	if ((fp = fopen("test.txt", "rw")) == NULL){
		exit( -1 );
	}

	while(fgets(buf, BUFSZ-1, fp) != NULL && i < MAX_LINES) {
		lines[i] = (char *) malloc(strlen(buf) + 1);
		strcpy(lines[i], buf);
		i++;
		count++;
	}

	int j;
	for(j = 0; j < i; j++){
		reverse(&lines[j]);
	}

	int len = 0;
	int counter = 0;
	int k;

	char *swap;

	for(k = 0; k<i; k++){
		for(j = k; j < i; j++){
			if(strlen(lines[j]) > len){
				len = strlen(lines[j]);
				counter = j;
			}
		}
		swap = lines[k];
		lines[k] = lines[counter];
		lines[counter] = swap;
	}

	for(j = 0; j < i; j++){
		printf("%s", lines[j]);
	}

	while (i > 0) {
	    free(lines[--i]);
	}

	return 0;
}
