#include <stdio.h>
void BinInsertSort(int a[],int n) {
	int i,j,low,high,mid;
	for(i=2; i<=n; i++) {
		a[0]=a[i];     //��a[i]�ݴ浽a[0]
		low=1;
		high=i-1;
		while(low<=high) {
			mid=(low+high)/2;
			if(a[mid]>a[0])    //���Ҫ����������м���С ������߿�ʼ����
				high=mid-1;
			else
				low=mid+1;         //��Ȼ�ʹ��ұ߿�ʼ��
		}
		for(j=i-1; j>=high+1; --j) {
			a[j+1]=a[j];
		}
		a[high+1]=a[0];
	}
}

void Fun(int &a);
int main() {

	struct s {
		int a,b,c;
	}st;
	
	printf("%d",sizeof(struct s));

}

