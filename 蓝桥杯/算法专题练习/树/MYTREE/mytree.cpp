#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <stack>
#include <list>
#include <vector>
#include <algorithm>
using namespace std;

#define MAX_NODE_NUM 100005
typedef int DATATYPE;

class TreeNode {

	private:
		//int a;

	public:
		unsigned int index;
		unsigned int parents_index;
		DATATYPE data;
		vector<unsigned int> childTrees;
		TreeNode(unsigned int index,unsigned int parents_index ,DATATYPE data );

};

//TreeNode::TreeNode() {
//	childTrees.clear();
//	data = 0;
//	index = 0;
//	parents_index = 0;
//}

TreeNode::TreeNode(unsigned int index = 0,unsigned int parents_index = 0,DATATYPE data = 0) {
	childTrees.clear();
	this->data = data;
	this->index = index;
	this->parents_index = parents_index;
}


class Trees {
	private:
		vector<TreeNode> treenodes;
		int sum_index;


	public:
		Trees() {
			treenodes.clear();
			sum_index = 0;
		}

		void newTreeNode(unsigned int parents_index ,DATATYPE data ) ;

		int get_sum_index();
		//get treenodes i value
		TreeNode at(int i);
		TreeNode index_at(int i);

		//Root First Search
		void RFS();
		//Root First Search(nested)
		void RFS(TreeNode *root);


};

void Trees::newTreeNode(unsigned int parents_index = 0,DATATYPE data = 0) {
	//build a new TreeNode
	treenodes.push_back(*(new TreeNode((this->sum_index)++,parents_index,data)));
	//add child index in parents
	//this->treenodes.at(parents_index).childTrees.push_back(this->sum_index);
	this->treenodes[parents_index].childTrees.push_back(this->sum_index);

}

//Root First Search
void Trees::RFS() {
	TreeNode *tn = new TreeNode();
	(*tn)= this->treenodes[0];
	if((*tn).childTrees.size() != 0) {
		this->RFS(tn);
		printf("index:%d \tvalue:%d \tchildrens:",(*tn).parents_index,(*tn).data);


	} else {
		printf("index:%d \tvalue:%d \tchildrens:",(*tn).parents_index,(*tn).data);
		vector<unsigned int>::iterator it = (*tn).childTrees.begin();

		while(it != (*tn).childTrees.end()) {
			cout<< (*it);
			it++;
		}
		cout<<endl;
	}
}

void Trees::RFS(TreeNode *tn) {
	if((*tn).childTrees.size() != 0) {
		this->RFS(tn);
		printf("index:%d \tvalue:%d \tchildrens:",(*tn).parents_index,(*tn).data);

	} else {
		printf("index:%d \tvalue:%d \tchildrens:",(*tn).parents_index,(*tn).data);
		vector<unsigned int>::iterator it = (*tn).childTrees.begin();

		while(it != (*tn).childTrees.end()) {
			cout<< (*it);
			it++;
		}
		cout<<endl;
	}
}


int Trees::get_sum_index() {
	return this->sum_index;
}

TreeNode Trees::at(int i) {

	return treenodes[i];
}


TreeNode Trees::index_at(int i) {

	return treenodes[i];
}



int main() {
	Trees mytree;
	mytree.newTreeNode(0,1);
	mytree.newTreeNode(1,2);
	mytree.newTreeNode(1,3);
	mytree.newTreeNode(2,4);
	mytree.newTreeNode(2,5);



//	for(int i = 0 ; i < mytree.get_sum_index() ; ++i ) {
//		printf("index:%d\tvalue:%d\n",mytree.at(i).parents_index,mytree.at(i).data);
//	}
	mytree.RFS();

	return 0;
}
