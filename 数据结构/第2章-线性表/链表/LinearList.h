#ifndef LINEARLIST_H
#define LINEARLIST_H

template<typename T>
class LinearList {
	protected:
		//当前长度
		int currLength;
	public:
		//查找
		virtual bool select (int i, T& element) const = 0;
		//插入
		virtual bool insert (int i, T element) = 0;
		//删除
		virtual bool deleteByIndex (int i, T &element)= 0;
		//更新
		virtual bool update (int i, T element) = 0;

};

#endif
