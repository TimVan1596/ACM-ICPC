#include "cstdio"
#include "iostream"
#include "queue"
using namespace std;
int a[5][5];
bool visit[5][5];
int dx[4]={1,-1,0,0},dy[4]={0,0,1,-1};
struct Node{
    int x,y;
    int s;///路径长度
    int l[30];///每走一步的方向
};///通过记录方向来记录路径
bool judge(int x,int y)
{
    if(x<0||x>=5||y<0||y>=5)
        return true;
    if(visit[x][y])
        return true;
    if(a[x][y]==1)
        return true;
    return false;
}
Node& bfs()
{
    queue<Node> que;
    Node cur,next;
    cur.x=0;cur.y=0;cur.s=0;
    visit[0][0]=1;
    que.push(cur);
    while(que.size())
    {
        cur=que.front();
        que.pop();
        if(cur.x==4&&cur.y==4)
            return cur;

        int i,nx,ny;
        for(i=0;i<4;i++)
        {
            nx=cur.x+dx[i];
            ny=cur.y+dy[i];
            if(judge(nx,ny))
                continue;
            next=cur;
            next.x=nx;
            next.y=ny;
            next.s=cur.s+1;
            next.l[cur.s]=i;
            visit[nx][ny]=1;
            que.push(next);
        }
    }
    return cur;
}
int main()
{
    for(int i=0;i<5;i++)
    {
        for(int j=0;j<5;j++)
        {
            scanf("%d",&a[i][j]);
        }
    }
    Node ans=bfs();
    printf("(0, 0)\n");
    int x=0,y=0;
    for(int i=0;i<ans.s;i++)
    {
        x+=dx[ans.l[i]];
        y+=dy[ans.l[i]];
        printf("(%d, %d)\n",x,y);
    }
    return 0;
}
