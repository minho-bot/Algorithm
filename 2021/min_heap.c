#include<stdio.h>

int is_Empty(int *size){
	if(*size <= 0)
		return 1;
	else
		return 0;
}

void swap(int heap[], int a, int b){
	int tmp;
	tmp = heap[a];
	heap[a] = heap[b];
	heap[b] = tmp;
	return;
}

int delete_Node(int heap[], int *size){
	if((*size) == 1){
		(*size)--;
		return heap[1];
	}

	int tmp = heap[1];
	int cursor = (*size);
	swap(heap, cursor, 1);//마지막 노드를 루프로 올림
	(*size)--;
	cursor = 1;
	while(1){
		if((*size) >= (cursor * 2) + 1){//양쪽 자식이 모두 있을 경우
			if(heap[cursor*2] < heap[cursor]){
				if(heap[cursor*2] < heap[cursor*2 + 1]){
					swap(heap, cursor, cursor*2);
					cursor = cursor * 2;
				}
				else{
					swap(heap, cursor, cursor*2 + 1);
					cursor = cursor * 2 + 1;
				}
			}
			else{
				if(heap[cursor*2+1] < heap[cursor]){
					swap(heap, cursor, cursor*2+1);
					cursor = cursor*2+1;
				}
				else
					break;
			}
		}
		else if((*size) == cursor*2){//왼쪽 자식만 있을 경우
			if(heap[cursor*2] < heap[cursor]){
				swap(heap, cursor, cursor*2);
				break;
			}
			break;
		}
		else if((*size) < cursor*2){//자식이 없을 경우
			break;
		}
	}
	return tmp;
}

void add_Node(int heap[], int *size, int target){
	int cursor = (*size) + 1;
	heap[cursor] = target;//끝에 추가
	(*size)++;

	while(cursor > 1){
		if(heap[cursor] < heap[cursor/2]){//부모보다 작으면 자리 바꿈
			swap(heap, cursor, cursor/2);
			cursor /= 2;
		}
		else
			return;
	}
	return;
}

int main(){
	int n;
	scanf("%d", &n);
	int heap[100002];
	int size = 0;
	int target;
	int tmp;
	for(int i=0; i<n; i++){
		scanf("%d", &target);
		if(target == 0){
		//	printf("출력해야해\n");
			if(is_Empty(&size) == 1)//비어있을 경우
				printf("0\n");
			else{//가장 작은 값 출력
				tmp = delete_Node(heap, &size);
				printf("%d\n", tmp);
			}
		}
		else{
		//	printf("추가해야해\n");
			add_Node(heap, &size, target);
		//	printf("target = %d, size = %d\n", target, size);
		}
	}
	return 0;
}
