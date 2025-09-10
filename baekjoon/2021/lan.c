#include<stdio.h>
#include<stdlib.h>

int compare(const void *a, const void *b){
	long n1 = *(long *)a;
	long n2 = *(long *)b;
	if(n1 > n2) return 1;
	else if(n1 < n2) return -1;
	else return 0;
}

int cut(long lan[], int k, int n, long size){
	long tmp; // i번 째 인덱스의 랜선을 얼마나 자를 수 있는지
	int pos = 0;
	for(int i=0; i<k; i++){
		tmp = 0;
		for(int j=0; ; j++){
			tmp += size;
		//	printf("tmp = %d\n", tmp);
			if(tmp > lan[i]){
				pos += j;
		//		printf("in lan[%d], pos = %d\n", i, pos);
				if(pos >= n)
					return 1;
				break;
			}
		}
	}
	return 0;
}

long binary(long lan[], int k, int n){
	long left = 0;
	long right = lan[k-1];
	long mid;
	long tmp;
	while(left < right){
		mid = (left + right + 1) / 2;
		tmp = cut(lan, k, n, mid);
		
//		printf("left = %d, right = %d\n", left, right);
//		printf("mid = %d cut = %d\n", mid, tmp);
//		puts("");
		
		if(tmp == 1)
			left = mid;
		else if(tmp == 0)
			right = mid-1;
	}
	return left;
}

int main(){
	int k, n;
	scanf("%d %d", &k, &n);
	long lan[k];

	for(int i=0; i<k; i++){
		scanf("%ld", &lan[i]);
	}

	qsort(lan, sizeof(lan)/sizeof(long), sizeof(long), compare);

//	for(int i=0; i<k; i++)
//		printf("%5d", lan[i]);
//	puts("");


	long ans = binary(lan, k, n);
	printf("%ld", ans);
	return 0;

}
