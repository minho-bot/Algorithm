#include<stdio.h>

int main(){
	int a, b, v;
	scanf("%d %d %d", &a, &b, &v);
	int go = a-b;//하루에 얼마나 올라가는 지
	int must = v-a;//마지막 날은 안미끄러지니깐
	int ans;
	
	if(must % go == 0)
		ans = (must / go) + 1;
	else
		ans = (must / go) + 2;

	printf("%d", ans);
	return 0;
}
