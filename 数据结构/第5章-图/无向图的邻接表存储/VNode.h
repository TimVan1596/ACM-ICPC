#ifndef VNDOE_H
#define VNDOE_H

#include "ArcNode.h"

//顶点结点
class VNode {
	private:

	public:
		//顶点结点的数据
		char data;
		//此顶点弧串的首个弧结点
		ArcNode *first;
		
		VNode(){
		}
		
		VNode(char _data){
			data = _data;
		}
};

#endif
