#include<stdio.h>
int n,nf,in[100],p[50];
int hit=0,i,j,k;
int pgfaultcnt=0;

void getData(){
    printf("\nEnter length of page reference sequence:");
    scanf("%d",&n);
    printf("\nEnter the page reference sequence:");
    for(i=0; i<n; i++)
        scanf("%d",&in[i]);
    printf("\nEnter no of frames:");
    scanf("%d",&nf);
}
void initialize(){
    pgfaultcnt=0;
    for(i=0; i<nf; i++)
        p[i]=9999;}

int isHit(int data){
    hit=0;
    for(j=0; j<nf; j++){
        if(p[j]==data){
            hit=1;
            break;
        }
    }
    return hit;
}

void dispPages(){
    for (k=0; k<nf; k++){
        if(p[k]!=9999)
            printf(" %d",p[k]);
    }
}

void dispPgFaultCnt(){
    printf("\nTotal no of page faults:%d",pgfaultcnt);}

void optimal(){
    initialize();
    printf("OPTIMAL PAGE REPLACEMENT ALGORITHM - SH");
    int near[50];
    for(i=0; i<n; i++){
        printf("\n%d : ",in[i]);
        if(isHit(in[i])==0){
            for(j=0; j<nf; j++){
                int pg=p[j];
                int found=0;
                for(k=i; k<n; k++){
                    if(pg==in[k]){
                        near[j]=k;
                        found=1;
                        break;
                    }
                    else
                        found=0;
                }
                if(!found)
                    near[j]=9999;
            }
            int max=-9999;
            int repindex;
            for(j=0; j<nf; j++){
                if(near[j]>max){
                    max=near[j];
                    repindex=j;
                }
            }
            p[repindex]=in[i];
            pgfaultcnt++;

            printf("Oops!! It's a MISS ");
            dispPages();
        }
        else
            printf("Yay! It's a HIT ");}

    dispPgFaultCnt();
}
int main(){
    getData();
    optimal();
    getData();
    optimal();
}
