#include<stdio.h>
#include<stdlib.h>

int compare(const void *a, const void *b){
	int n1 = *(int *)a;
	int n2 = *(int *)b;
	if(n1 > n2) return 1;
	else if(n1 < n2) return -1;
	else return 0;
}

int pos(int *distance, int n, int c, int dis){
	int tmp = 0;
	int stack = 0;
	for(int i=0; i<n; i++){
		stack += distance[i];
		if(stack >= dis){
			tmp++;
			stack = 0;
		}
		if(tmp >= c-1)
			return 1;
	}
	return 0;
}




int binary_search(int *house, int n, int c, int *distance){
	int left = 1;
	int right = (house[n-1] - house[0]) / (c-1);
	int ans = 0;
	int mid;
	while(left <= right){
		mid = (left + right) / 2;
		if(pos(distance, n-1, c, mid) == 1){
			ans = mid;
			left = mid+1;
		}
		else
			right = mid-1;
	}
	return ans;
}




int main(){
	int n, c;
	scanf("%d", &n);
	scanf("%d", &c);
	int *house = (int *)malloc(sizeof(int) * n);
	for(int i=0; i<n; i++)
		scanf("%d", &house[i]);
	qsort(&house[0], n, sizeof(int), compare);

	int *distance = (int *)malloc(sizeof(int) * (n-1));
	for(int i=0; i<n-1; i++)
		distance[i] = house[i+1] - house[i];

	int ans = binary_search(house, n, c, distance);
	printf("%d", ans);



	free(house);
	free(distance);
	return 0;
}
