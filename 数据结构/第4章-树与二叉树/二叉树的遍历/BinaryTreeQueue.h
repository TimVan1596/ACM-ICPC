#ifndef BINARYTREEQUEUE_H
#define BINARYTREEQUEUE_H

#include "BinaryTreeNode.h"
using namespace std;

//������ר�ö���
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

		//��ͷβ���ĵ�����
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
				node = NULL;
				tail = head;
			} else {
				node = head->next->data;
				head->next = head->next->next;
			}


			return node;
		}

		bool isEmpty() {
			return head->next == NULL;
		}


};

#endif
