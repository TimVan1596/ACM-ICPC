#include <iostream>

#include "SeqStack.h"
using namespace std;

bool isSeqLegal(string seq);

//������I��O�ֱ��ʾ��ջ�ͳ�ջ������ջ�ĳ�̬����̬��Ϊ�գ�
//��ջ�ͳ�ջ�Ĳ������пɱ�ʾΪ����I��O��ɵ�����
//�ƿ��Բ���������Ϊ�Ϸ����У������Ϊ�Ƿ����С�
//  (1)������ʾ����������Щ�ǺϷ���
//  A��IOIIOIOO  B��IOOIOIIO  C��IIIOIOIO D��IIIOOIOO
//  (2)ͨ����(1)�ķ�����д��һ���㷨���ж������Ĳ��������Ƿ�Ϸ���
//���Ϸ�������true�����򷵻�false(�ٶ����ж��Ĳ��������Ѵ���һά������)��
int main(int argc, char** argv) {

	string seq = "IOIIOIOO";
	cout<<seq<<":";
	isSeqLegal(seq)? cout<<"TRUE" : cout<<"false";
	cout<<endl;

	seq = "IOOIOIIO";
	cout<<seq<<":";
	isSeqLegal(seq)? cout<<"TRUE" : cout<<"false";
	cout<<endl;

	seq = "IIIOIOIO";
	cout<<seq<<":";
	isSeqLegal(seq)? cout<<"TRUE" : cout<<"false";
	cout<<endl;

	seq = "IIIOOIOO";
	cout<<seq<<":";
	isSeqLegal(seq)? cout<<"TRUE" : cout<<"false";
	cout<<endl;


	return 0;
}

bool isSeqLegal(string seq) {
	bool isLegal = true;

	int len = seq.size() , insertCount = 0;
	for(int i = 0 ; i < len ; ++i) {
		if(seq[i] == 'I') {
			insertCount++;
		} else {
			if(--insertCount < 0) {
				isLegal = false;
				break;
			}
		}
	}

	if(insertCount != 0) {
		isLegal = false;
	}

	return isLegal;
}
