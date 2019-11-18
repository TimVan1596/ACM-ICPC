#ifndef ARCNODE_H
#define ARCNODE_H

//弧结点（顶点结点后面跟着）
class ArcNode {
	private:

	public:
		//此弧通向的结点序号
		int adjvex;
		//此弧通向的下一个弧结点
		ArcNode* next;
		ArcNode() {
		}


		ArcNode(int _adjvex):
			adjvex(_adjvex) {
			next = NULL;
		}
};

#endif
