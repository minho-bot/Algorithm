#include<stdio.h>
#include<stdlib.h>

int get(long *tree, int n, long k){//고치기
	long h = 0;
	for(int i=0; i<n; i++)
		if(tree[i] > k)
			h+= (tree[i]-k);
	return h;
}

int compare(const void *a, const void *b){
	long n1 = *(long *)a;
	long n2 = *(long *)b;
	if(n1 > n2)
		return 1;
	else if(n2 > n1)
		return -1;
	else
		return 0;
}

long binary(long *tree, int n, long h){//left first zero
	long left = 0;
	long right = tree[n-1];
	long got, mid;
	while(left != right){
		mid = (left + right + 1)/2;
//		printf("left = %d right = %d mid = %d\n", left, right, mid);
		got = get(tree, n, mid);
//		printf("got = %d, h = %d\n", got, h);
		if(h > got){//나무가 모자르다
			right = mid -1;
//			printf("나무가 모자르다, right -> %d\n", right);
		}
		else if(h <= got)//나무가 충분하지만 아껴쓰자
			left = mid;
	}
	return left;

}

int main(){
	int n;
	long h;
	scanf("%d %ld", &n, &h);
	long *tree = (long *)malloc(sizeof(long)*n);
	for(int i=0; i<n; i++)
		scanf("%ld", &tree[i]);
	qsort(tree, n, sizeof(long), compare);
//	printf("answer = %d\n", binary(tree, n, h));
	printf("%ld", binary(tree,n, h));



	free(tree);
	return 0;
}
