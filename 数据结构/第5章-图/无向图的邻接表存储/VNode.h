#ifndef VNDOE_H
#define VNDOE_H

#include "ArcNode.h"

//������
class VNode {
	private:

	public:
		//�����������
		char data;
		//�˶��㻡�����׸������
		ArcNode *first;
		
		VNode(){
		}
		
		VNode(char _data){
			data = _data;
		}
};

#endif
