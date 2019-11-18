#include <iostream>
#include "ALGraph.h"
#include "ALGQueue.h"
using namespace std;

int main(int argc, char** argv) {

	ALGraph graph;
	//示例无向图
	graph.genExampleGraph();
	//BFS遍历
	cout<<"---- BFS 广度优先遍历 -----"<<endl;
	graph.BFSTraverse();
	cout<<"---- ---- -----"<<endl<<endl;
	//DFS遍历
	cout<<"---- DFS 深度优先遍历 -----"<<endl;
	graph.DFSTraverse();
	cout<<"---- ---- -----"<<endl<<endl;

//测试循环队列是否可以用
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
