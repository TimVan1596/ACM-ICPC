#ifndef BINARYTREESTACK_H
#define BINARYTREESTACK_H

#include "VNode.h"
using namespace std;

//邻接表专用栈
class ALGStack {
	private:

		class Node {
			public:
				VNode* data;
				Node* next;
				Node* previous;

				Node(VNode* _data) {
					data = _data;
					next = NULL;
					previous = NULL;
				}
		};


		Node *head;
		Node *tail;

	public:

		ALGStack() {
			VNode* _node = new VNode('0');
			head = new Node(_node);
			tail = head;
		}

		void push(VNode* _node) {
			Node *node = new Node(_node);
			tail->next = node;
			node->previous = tail;
			tail = node;
		}

		VNode* pop() {
			VNode* ret = tail->data;
			Node *p = tail;
			if(tail->previous != head) {
				tail = tail->previous;
			} else {
				tail = head;
			}
			delete p;
			return ret;

		}

		VNode* top() {
			return tail->data;
		}

		bool isEmpty() {
			return head == tail;
		}

};

#endif

