
#include <stdio.h>
#include <string.h>

void stringsort(char *);

int main(int argc, char **argv) {

    char cube[10000][15];
    char cubedigits[10000][15];

    for(int n = 0; n < 10000; n++) {
      sprintf(cube[n], "%.0f", (double)(n+1)*(double)(n+1)*(double)(n+1));
      strcpy(cubedigits[n], cube[n]);
      stringsort(cubedigits[n]);
    }

    for(int i = 0; i < 10000; i++) {
      int count = 0;
      for(int j = 0; j < 10000; j++) { 
        if(!strcmp(cubedigits[i], cubedigits[j])) {
          count++;
        }
      }
      if(count == 5) {
        for(int j = 0; j < 10000; j++) {
          if(!strcmp(cubedigits[i], cubedigits[j])) {
             printf("%d : %s : %s\n", (j + 1), cube[j], cubedigits[j]);
          }
        }
        printf("\n\n");
        break;
      }
    }
  
    return(0);
}

void stringsort(char *s) {
  for(int i = 0; i < strlen(s) - 1; i++) {
    for(int j = i + 1; j < strlen(s); j++) {
      if(s[i] > s[j]) {
        char tmp = s[i];
        s[i] = s[j];
        s[j] = tmp;
      }
    }
  }
  return;
}