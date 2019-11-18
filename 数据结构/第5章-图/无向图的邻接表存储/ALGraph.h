#ifndef ALGRAPH_G
#define ALGRAPH_G

#include <iostream>
#include "VNode.h"
#include "ArcNode.h"
#include "ALGQueue.h"
#include "ALGStack.h"

using namespace std;


//�ڽӱ�
class ALGraph {
	private:
		//��������
		VNode *vnode;
		//���ĸ���
		int arcNum;
		//�������
		int vexNum;
	public:
		//BFS��������㷨
		//�������Ĳ�α���
		void BFSTraverse() {
			bool isVisted[this->vexNum] = {false};
			VNode *p = vnode;
			ALGQueue queque(this->vexNum);
			queque.enQueue(vnode[0]);
			isVisted[0] = true;
			p = queque.deQueue();
			//��������ΪpΪ��
			while(p) {
				cout<<p->data<<endl;

				ArcNode *arcnode =  p->first;
				while(arcnode) {
					//���δ�����ʼ��������
					if(!isVisted[arcnode->adjvex]) {
						queque.enQueue(vnode[arcnode->adjvex]);
						isVisted[arcnode->adjvex] = true;
					}
					arcnode = arcnode->next;
				}

				p = queque.deQueue();
			}

		}

		//DFS��������㷨
		void DFSTraverse() {
			bool isVisted[this->vexNum] = {false};

			for(int i = 0 ; i < this->vexNum ; ++i) {
				if(!isVisted[i]) {
					DFS(i,isVisted);
				}
			}
		}

		//index = ���ʽ�����
		//isVisted = ��־����
		void DFS(int index,bool *isVisted) {

			cout<<vnode[index].data<<endl;
			isVisted[index] = true;

			ArcNode *arcnode =  vnode[index].first;
			while(arcnode) {
				//���δ�����ʼ��������
				if(!isVisted[arcnode->adjvex]) {

					DFS(arcnode->adjvex,isVisted);
				}
				arcnode = arcnode->next;
			}

		}

		//�������ת���
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

		//��ʼ������һ��ʵ������ͼ
		void genExampleGraph() {
			vnode = new VNode[5];
			arcNum = 5;
			vexNum = 5;

			//��ʼ������Ӧ������
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
