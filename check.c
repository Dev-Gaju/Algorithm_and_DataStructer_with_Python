#include <stdio.h>
#include <conio.h>

int main() {
    FILE *fp;
    char in,fn[45],cho;
    printf("\n\t\t\t\t\tNOTEPAD\n");
    printf("\n\t\t\tEnter File Name :");
    gets(fn);
    printf("\n\nWhat can u do write:w/read:r/add:a : ");
    scanf("%c",&cho);
    if(cho == 'r')
    {
        fp=fopen(fn,"r");
        printf("\n\n\n\t\t\tREAD MODE\n\n");

    while((in=getc(fp))!=EOF)
    {
        printf("%c",in);
    }
    fclose(fp);
}
else if(cho=='w') {
        fp = fopen(fn, "w");
        printf("\n\n\n\t\t\tWRITE MODE");
        printf("\n\n\t\t\t For Save File Press Ctrl+C \n\n");
        while ((in = getchar()) != EOF) {
            putc(in, fp);

        }
        fclose(fp);
    }

else if(cho=='a'){
fp=fopen(fn,"a");
printf(" \n\n\n\t\t\tAdd MODE\n\n");
printf("\n\n\t\t\t For Save File press Ctrl+Z \n\n");
while((in=getchar())!=EOF)
{
putc(in,fp);
}
        fclose(fp);
}
getch();

return 0;
}