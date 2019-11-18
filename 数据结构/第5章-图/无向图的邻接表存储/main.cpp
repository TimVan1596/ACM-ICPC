#include <iostream>
#include "ALGraph.h"
#include "ALGQueue.h"
using namespace std;

int main(int argc, char** argv) {

	ALGraph graph;
	//ʾ������ͼ
	graph.genExampleGraph();
	//BFS����
	cout<<"---- BFS ������ȱ��� -----"<<endl;
	graph.BFSTraverse();
	cout<<"---- ---- -----"<<endl<<endl;
	//DFS����
	cout<<"---- DFS ������ȱ��� -----"<<endl;
	graph.DFSTraverse();
	cout<<"---- ---- -----"<<endl<<endl;

//����ѭ�������Ƿ������
//	const int LEN = 5;
//	ALGQueue queue(LEN);
//
//	cout<<"queue:"<<endl<<"isEmpty = "<< queue.isEmpty()<<endl;
//	cout<<" isFull = "<< queue.isFull()<<endl;
//
//	cout<<"queue.enQueue(2,4,8,16,32,64,128)"<<endl;
//	int arr[LEN] = {'C','D','A','B'};
//	for(int i = 0 ; i < LEN ; ++i) {
//		VNode vnode(arr[i]);
//		queue.enQueue(vnode);
//	}
//
//	VNode vnode;
//	cout<<"*****  deQueueAll ={   *****"<<endl;
//	while(!queue.isEmpty()) {
//		vnode = queue.deQueue();
//		cout<<" deQueue = "<<vnode.data<<endl;
//	}
//	cout<<"*****  }   *****"<<endl<<endl;

	return 0;
}
