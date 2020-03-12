#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX_LINES	25
#define BUFSZ		128

void reverse( char *s );

int main()
{
	int	i = 0, j, count = 0;
	char	*lines[MAX_LINES];
	char	buf[BUFSZ];
	FILE	*fp;

	if ( ( fp = fopen( "something.txt", "rw" )) == NULL )
		exit( -1 );

	while ( fgets( buf, BUFSZ-1, fp ) != NULL && i < MAX_LINES )
	{
		lines[i] = (char *) malloc( strlen(buf) + 1 );
		buf[strlen(buf)-1] = '\0';
		strcpy( lines[i], buf );
		i++;
		count++;
	}
	for ( i = 0; i < count; i++ )
		reverse( lines[i] );
	for ( i = 0; i < count; i++ )
	{
		for ( j = 0; j < count - i - 1; j++ )
		{
			if ( strlen(lines[j]) < strlen(lines[j+1]) )
			{
				char *t = lines[j];
				lines[j] = lines[j+1];
				lines[j+1] = t;
			}
		}
	}
	for ( i = 0; i < count; i++ )
	{
		printf( "%s\n", lines[i] );
	}
}


void reverse( char *s )
{
	int i, j;
	
	for ( i =0, j = strlen(s)-1; i < strlen(s)/2; i++, j-- )
	{
		char t = s[i];
		s[i] = s[j];
		s[j] = t;
	}
}

