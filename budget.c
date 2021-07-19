#include<stdio.h>
#include<stdlib.h>

int compare(const void *a, const void *b){
	int n1 = *(int *)a;
	int n2 = *(int *)b;
	if(n1 > n2) return 1;
	else if(n1 < n2) return -1;
	else return 0;
}

int calc(int *budget, int n, int m, int limit){
	int sum = 0;
	for(int i=0; i<n; i++){
		if(budget[i] > limit)
			sum += limit;
		else
			sum += budget[i];
	}
	if(m >= sum)
		return 1;
	else return 0;
}

int binary_search(int *budget, int n, int m){
	int left = 0;
	int right = budget[n-1];
	int mid;
	int limit;
	while(left <= right){
		mid = (left + right) / 2;
		if(calc(budget, n, m, mid) == 1){
			limit = mid;
	//		printf("limit = %d\n", limit);
			left = mid+1;
		}
		else
			right = mid-1;
	}
	return limit;
}

int main(){
	int n, m;
	scanf("%d", &n);
	int *budget = (int *)malloc(sizeof(int) * n);
	for(int i=0; i<n; i++)
		scanf("%d", &budget[i]);
	scanf("%d", &m);

	qsort(&budget[0], n, sizeof(int), compare);
	int ans = binary_search(budget, n, m);
	printf("%d", ans);


	free(budget);
	return 0;
}
