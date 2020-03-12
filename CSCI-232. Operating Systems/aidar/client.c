#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <sys/time.h>
#include <netinet/in.h>

#define BUFSIZE		4096

int connectsock( char *host, char *service, char *protocol );

/*
**	Client
*/
int
main( int argc, char *argv[] )
{
	char		buf[BUFSIZE];
	char		correct_incorrect[BUFSIZE];
	char		*service;		
	char		*host = "localhost";
	int		cc;
	int		csock;
	
	
	switch( argc ) 
	{
		case    2:
			service = argv[1];
			break;
		case    3:
			host = argv[1];
			service = argv[2];
			break;
		default:
			fprintf( stderr, "usage: chat [host] port\n" );
			exit(-1);
	}

	/*	Create the socket to the controller  */
	if ( ( csock = connectsock( host, service, "tcp" )) == 0 )
	{
		fprintf( stderr, "Cannot connect to server.\n" );
		exit( -1 );
	}
	
	printf( "The server is ready, please send data to the server.\n" );
	printf( "Type q or Q to quit.\n" );
	fflush( stdout );


	write(csock, "Connected", 9);
	read( csock, buf, BUFSIZE);
	printf("%s.\n", buf);  //Reads status sended from server
	fgets( buf, BUFSIZE, stdin );
	write(csock, buf, BUFSIZE);  //Writes Info about group and name
	read(csock, buf, BUFSIZE); //Reads first question
	printf("%s", buf);
	fgets( buf, BUFSIZE, stdin );  //Write answer
	write(csock, buf, BUFSIZE);



	read( csock, correct_incorrect, BUFSIZE );
	printf( "%s\n", correct_incorrect );

	memset(correct_incorrect, 0, strlen(correct_incorrect));	


	read(csock, buf, BUFSIZE);  //Reads second question
	printf("%s", buf);
	fgets( buf, BUFSIZE, stdin );  //Writes answer
	write(csock, buf, BUFSIZE);



	read( csock, correct_incorrect, BUFSIZE );
	printf( "%s\n", correct_incorrect );
	/*read( csock, buf, BUFSIZE );
	printf( "%s\n", buf );
	if(strcmp(buf, "QS|ADMIN")==0){
	fgets( buf, BUFSIZE, stdin );
	write(csock, buf, BUFSIZE);
	read( csock, buf, BUFSIZE );
	printf( "%s\n", buf );
	fgets( buf, BUFSIZE, stdin );
	write(csock, buf, BUFSIZE);
	read(csock, buf, BUFSIZE);
	printf("%s", buf);*/
	
	
	

}


