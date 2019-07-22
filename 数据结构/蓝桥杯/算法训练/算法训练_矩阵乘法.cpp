#include <cstdio>
#include <iostream>
using namespace std;

static int matrix_1[500][500] = {0};
static int matrix_2[500][500] = {0};

//��ӡ����ʽ
void printMatrix(int (*matrix)[1000] , int m , int n) {
	for(int i = 0; i < m ; ++i) {
		for(int j = 0 ; j < n ; ++j) {
			int cache = 0;
			cout<<matrix[i][j]<<" ";
		}
		cout<<endl;
	}

}


//��������ʽ�˷���i�С���j�е�ֵ����ͬ����Ϊs
int getMatrixValue(int m , int n , int s) {
	int sum = 0;
	for(int i = 0; i < s ; ++i) {
		sum += matrix_1[m][i] * matrix_2[i][n];
	}
	return sum;
}


int main() {
	int m = 0, s = 0, n = 0;
	cin>>m>>s>>n;


	int matrix[m][n] = {0};

	int sum = 0;


	//�����׸�����ʽ
	for(int i = 0; i < m ; ++i) {
		for(int j = 0 ; j < s ; ++j) {
			int cache = 0;
			cin>>cache;
			matrix_1[i][j] =cache;
		}
	}

	//����ڶ�������ʽ
	for(int i = 0; i < s ; ++i) {
		for(int j = 0 ; j < n ; ++j) {
			int cache = 0;
			cin>>cache;
			matrix_2[i][j] =cache;
		}
	}

	for(int i = 0 ; i < m ; ++i) {
		for(int j = 0 ; j < n ; ++j) {
			cout<<getMatrixValue(i,j,s)<<" ";
		}
		cout<<endl;
	}



	return 0;
}
