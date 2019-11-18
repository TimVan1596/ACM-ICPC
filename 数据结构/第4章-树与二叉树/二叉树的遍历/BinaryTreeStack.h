#ifndef BINARYTREESTACK_H
#define BINARYTREESTACK_H

#include "BinaryTreeNode.h"
using namespace std;

//¶þ²æÊ÷×¨ÓÃÕ»
class BinaryTreeStack {
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

	public:

		BinaryTreeStack() {
			BinaryTreeNode<char>* _node = new BinaryTreeNode<char>('0');
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
			if(tail->previous != head) {
				tail = tail->previous;
			} else {
				tail = head;
			}
			delete p;
			return ret;

		}

		BinaryTreeNode<char>* top() {
			return tail->data;
		}

		bool isEmpty() {
			return head == tail;
		}

};

#endif

