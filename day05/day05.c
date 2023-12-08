#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>


int main(){

    FILE *fptr;

    //char filename[10] = "input.txt";
    char filename[10] = "test.txt";

    char first_line[300];
    long long* seed_values = malloc(0);
    int seed_values_len = 0;
    char line[100];

    fptr = fopen(filename, "r");

    if(fptr != NULL) {

        // getting seed values
        fgets(first_line, 300, fptr);
        char *number_str = malloc(sizeof(char) * 20);
        long long number;

        for (int i = 0; i < strlen(first_line); i++){
            if (first_line[i] == '\n'){
                if (strlen(number_str) != 0){
                    number = atoll(number_str);
                    strcpy(number_str, "");
                    seed_values = realloc(seed_values, sizeof(number) * (seed_values_len + 1));
                    seed_values[seed_values_len++] = number;
                }
                continue;
            }

            if (isdigit(first_line[i])){
                // append digit
                int len = strlen(number_str);
                number_str[len] = first_line[i];
                number_str[len + 1] = '\0';
            }

            if (first_line[i] == ' ' && strlen(number_str) != 0){
                number = atol(number_str);
                strcpy(number_str, "");
                seed_values = realloc(seed_values, sizeof(number) * (seed_values_len + 1));
                seed_values[seed_values_len++] = number;
            }

        }


        // parse the rest of the file
        while(fgets(line, 100, fptr)) {

            if (*line == '\n'){ // empty line
                // next line is a map definition
                fgets(line, 100, fptr);                 

                char source[20];
                char to[2];
                char destination[20];
                //char source_to_destination[3][20];

                char curr[20];
                int curr_len = 0;
                for (int i = 0; i < strlen(line); i++){
                    //printf("%s\n", line[i]);
                    if (line[i] == '-' || line[i] == ' '){
                        if (strlen(source) == 0){
                            strcpy(source, curr);
                        } else if(strlen(to) == 0){
                            strcpy(to, curr);
                        }else{
                            strcpy(destination, curr);
                        }
                        curr[0] = '\0';
                    } else{
                        // append char
                        curr[curr_len] = first_line[i];
                        curr[curr_len + 1] = '\0';
                        curr_len++;
                    }
                }
                printf("map: %s %s %s\n", source, to, destination);


                continue;
            }



            //printf("%s", line);
        }

    } else {
        printf("[ERROR] Not able to open file.");
        fclose(fptr); 
        return -1;
    }

    free(seed_values);
    fclose(fptr); 



    return 0;
}