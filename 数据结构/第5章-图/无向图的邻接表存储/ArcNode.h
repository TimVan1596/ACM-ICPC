#ifndef ARCNODE_H
#define ARCNODE_H

//����㣨�����������ţ�
class ArcNode {
	private:

	public:
		//�˻�ͨ��Ľ�����
		int adjvex;
		//�˻�ͨ�����һ�������
		ArcNode* next;
		ArcNode() {
		}


		ArcNode(int _adjvex):
			adjvex(_adjvex) {
			next = NULL;
		}
};

#endif
