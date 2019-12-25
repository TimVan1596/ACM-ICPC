#ifndef BINARYTREEQUEUE_H
#define BINARYTREEQUEUE_H

#include "BinaryTreeNode.h"
using namespace std;

//二叉树专用队列
class BinaryTreeQueue {
	private:
		class Node {
			public:
				BinaryTreeNode<char>* data;
				Node* next;
				Node(BinaryTreeNode<char>* _data) {
					data = _data;
					next = NULL;
				}
		};

		//带头尾结点的单链表
		Node *head;
		Node *tail;
	public:
		BinaryTreeQueue() {
			BinaryTreeNode<char>* _node = new BinaryTreeNode<char>('0');
			head = new Node(_node);
			tail = head;
		}

		void enQueue(BinaryTreeNode<char>* _node) {
			Node *node = new Node(_node);
			tail->next = node;
			tail = node;
		}

		BinaryTreeNode<char>* deQueue() {
			BinaryTreeNode<char>* node;
			if(isEmpty()) {
				return NULL;
			} else {
				Node* p = head->next;
				node = p->data;
				head->next = p->next;
				if(tail = p){
					tail = head;
				}
			}


			return node;
		}

		bool isEmpty() {
			return head == tail;
		}


};

#endif
