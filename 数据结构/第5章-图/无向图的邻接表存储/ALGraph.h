#ifndef ALGRAPH_G
#define ALGRAPH_G

#include <iostream>
#include "VNode.h"
#include "ArcNode.h"
#include "ALGQueue.h"
#include "ALGStack.h"

using namespace std;


//邻接表
class ALGraph {
	private:
		//顶点数组
		VNode *vnode;
		//弧的个数
		int arcNum;
		//顶点个数
		int vexNum;
	public:
		//BFS广度优先算法
		//类似树的层次遍历
		void BFSTraverse() {
			bool isVisted[this->vexNum] = {false};
			VNode *p = vnode;
			ALGQueue queque(this->vexNum);
			queque.enQueue(vnode[0]);
			isVisted[0] = true;
			p = queque.deQueue();
			//结束条件为p为空
			while(p) {
				cout<<p->data<<endl;

				ArcNode *arcnode =  p->first;
				while(arcnode) {
					//如果未被访问即进入队列
					if(!isVisted[arcnode->adjvex]) {
						queque.enQueue(vnode[arcnode->adjvex]);
						isVisted[arcnode->adjvex] = true;
					}
					arcnode = arcnode->next;
				}

				p = queque.deQueue();
			}

		}

		//DFS深度优先算法
		void DFSTraverse() {
			bool isVisted[this->vexNum] = {false};

			for(int i = 0 ; i < this->vexNum ; ++i) {
				if(!isVisted[i]) {
					DFS(i,isVisted);
				}
			}
		}

		//index = 访问结点序号
		//isVisted = 标志数组
		void DFS(int index,bool *isVisted) {

			cout<<vnode[index].data<<endl;
			isVisted[index] = true;

			ArcNode *arcnode =  vnode[index].first;
			while(arcnode) {
				//如果未被访问即进入队列
				if(!isVisted[arcnode->adjvex]) {

					DFS(arcnode->adjvex,isVisted);
				}
				arcnode = arcnode->next;
			}

		}

		//结点数据转序号
		int dataToIndex(char data) {
			int index = 0;
			for(index = 0 ; index < vexNum ; ++index) {
				if(vnode[index].data == data) {
					break;
				}
			}
			if(index == vexNum) {
				index  = -1;
			}
			return index;
		}

		//初始化创建一个实例无向图
		void genExampleGraph() {
			vnode = new VNode[5];
			arcNum = 5;
			vexNum = 5;

			//初始化结点对应的数据
			vnode[0].data = 'C';
			vnode[1].data = 'A';
			vnode[2].data = 'E';
			vnode[3].data = 'B';
			vnode[4].data = 'D';


			ArcNode *node1 = new ArcNode(dataToIndex('A'));
			ArcNode *node2 = new ArcNode(dataToIndex('E'));
			node1->next = node2;
			vnode[0].first = node1;


			node1 = new ArcNode(dataToIndex('B'));
			node2 = new ArcNode(dataToIndex('C'));
			node1->next = node2;
			vnode[1].first = node1;

			node1 = new ArcNode(dataToIndex('B'));
			node2 = new ArcNode(dataToIndex('C'));
			node1->next = node2;
			vnode[2].first = node1;

			node1 = new ArcNode(dataToIndex('A'));
			node2 = new ArcNode(dataToIndex('D'));
			ArcNode *node3 = new ArcNode(dataToIndex('E'));
			node1->next = node2;
			node2->next = node3;
			vnode[3].first = node1;

			node1 = new ArcNode(dataToIndex('B'));
			vnode[4].first = node1;

		}

};

#endif
