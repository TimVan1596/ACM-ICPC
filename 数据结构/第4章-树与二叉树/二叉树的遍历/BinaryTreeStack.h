#ifndef BINARYTREESTACK_H
#define BINARYTREESTACK_H

#include "BinaryTreeNode.h"
using namespace std;

//¶þ²æÊ÷×¨ÓÃÕ»
class BinaryTreeStack {
	public:

		BinaryTreeStack(BinaryTreeNode<char>* _node) {
			head = new Node(_node);
			tail = head;
		}

		void push(BinaryTreeNode<char>* _node) {
			Node *node = new Node(_node);
			tail->next = node;
			node->previous = tail;
			tail = node;
		}

		BinaryTreeNode<char>* pop() {
			BinaryTreeNode<char>* ret = tail->data;
			Node *p = tail;
			if(tail->previous != NULL) {
				tail = tail->previous;
			} else {
				tail = head;
			}
			delete p;
			return ret;

		}

		BinaryTreeNode<char>* top() {

//			cout<<"int top"<<endl;
//			cout<<"tail ->"<<tail->data->data<<endl;
//			cout<<"tail->previous ->"<<tail->previous->data->data<<endl;

			return tail->data;
		}
	private:

		class Node {
			public:
				BinaryTreeNode<char>* data;
				Node* next;
				Node* previous;

				Node(BinaryTreeNode<char>* _data) {
					data = _data;
					next = NULL;
					previous = NULL;
				}
		};


		Node *head;
		Node *tail;
};

#endif

