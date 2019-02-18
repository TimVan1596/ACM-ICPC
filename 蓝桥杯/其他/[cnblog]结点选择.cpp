#include <iostream>
#include <cstring>
#define N 100000

#define MAX(x, y) ((x)>(y)?(x):(y))

struct edge {
	int to;
	int next;
};
int tree[N];

int weight[N];

edge edges[2*N];

int d[N][2];

int len = 0;

void add(int x, int y) {
	edges[len].to = y;
	edges[len].next = tree[x];
	tree[x] = len++;
}

void dp(int root, int p) {
	if(tree[root] == -1) {
		d[root][0] = 0;
		d[root][1] = weight[root];
		return;
	}
	for(int i = tree[root]; i != -1; i = edges[i].next) {
		int child = edges[i].to;
		if(child == p)
			continue;
		if(!d[child][1])
			dp(child, root);
		d[root][0] += MAX(d[child][1], d[child][0]);
		d[root][1] += d[child][0];
	}
	d[root][1] += weight[root];
}

int main() {
	memset(tree, -1, sizeof(tree));
	int n;
	std::cin >> n;
	for(int i = 1; i <= n; i++)
		std::cin >> weight[i];
	int x, y;
	for(int i = 0; i < n-1; i++) {
		std::cin >> x >> y;
		add(x, y);
		add(y, x);
	}

	dp(1, -1);

	int max = MAX(d[1][0], d[1][1]);

	std::cout << max << std::endl;
}
