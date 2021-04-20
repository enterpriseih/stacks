# cpp

## vim

```cpp
:%y+
"+gp
```

## template

```cpp
#include <iostream>
#include <queue>
#include <vector>
#include <set>
#include <algorithm>
#include <assert.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> solve(vector<vector<int>>& input) {
        return ans;
    }
};

int main() {
    Solution s;
    vector<vector<int>> input {{0,5,2},{2,5,3}};
    assert(s.solve(input) == ...)
    return 0;
}

```

## acm template

```cpp
#include<iostream>
using namespace std;
int main(){
    int N;
    while(cin >> N){
        while(N--){

        }
    }
    return 0;
}
```

## io

```cpp
// get line
string s;
getline(cin,s);

// return boolean 'true' / 'false'
cout << boolalpha<< ans;
```

## array

fixed-length

```cpp
// init
int a[128] = {0};

// init multidimensional with zero
int a[5][10][10];
memset(a,0,sizeof(a));

// copy(start,end, new start)
copy(&a[4][0][0],&a[4][0][0]+10*10, &a[5][0][0])
```

## vector

```cpp
// print
for(const int& k : ks){

    cout << k << " ";
}

// concat
b.insert(b.end(), a.begin(), a.end());

// slice
v2 = vector<int>(v1.begin() + 1, v1.end());

//  iterate
for(const auto& v: values) {
    std::cout << v << "\n";
}
for(int i=0;i<v3.size();i++){
    cout<<v3[i]<<' ';
}
for(int num : v){

}

//  delete
v.erase(v.begin()+1);
v.erase(v.begin()+2,v.begin()+5);

//  init
vector<int> vect{ 10, 20, 30 };
vector<double> v3(10,0) // 10 zeros

//  access
v3[2]= 1

//  insert
v.push_back(9);
v.insert(v.begin()+2,1);

//  sort
sort(v.begin(), v.end());

bool cmp(int & l, int & r)
{
    return l > r; // desc
}
sort(v.begin(), v.end(), cmp);
```

## set

```cpp
//  init
set<int> s;

//  insert
s.insert(5);

//  loop
set<int>::iterator it;
for(it=s1.begin();it!=s1.end();it++)
    cout<<*it<<endl;

//  delete
s.erase(5);

//  exits
s.find(element) != s.end();
```

## stack

```cpp
stack<int> s;
s.push(ele)
s.pop()
s.top()
s.size()
```

## queue

```cpp
bool q.empty()
q.size()
q.front()
q.back()
q.push(ele)
q.pop()
```

## priority_queue

```cpp
#include<queue>

// max-heap
priority_queue<int> q;

// min-heap
priority_queue <int, vector<int>, greater<int> > q;

q.push(2);
q.pop()
q.size()
q.empty()

// custom compare
struct compare
{
    bool operator()(const ListNode* n1, const ListNode* n2)
    {
        return n1->val > n2->val; // sim. greater
    }
};
priority_queue<ListNode*, vector<ListNode*>,compare> pq; // sim. min-heap
```

## set / multiset

search, insert, erase is O(log n)

```cpp
multiset <int, greater <int> > s;
ultiset <int, greater <int> > s (s1.begin(),s1.begin()+t);
s.insert(1);
s.erase(1);
s.erase(s.equal_range(1).first);
auto search = s.find(2);
```

## struct

```cpp
// init
struct subject {
    string name;
    int marks;
    int credits;
};
vector<subject> sub;
sub.push_back(subject());
```

## map

internally red-black tree

```cpp
// init
map<int,int> map;
map<int,int> map = {{1,1},{2,2}};

// assign
map[key] = value;

// check key exist
iter = mapStudent.find("123");
if(iter != mapStudent.end())
cout<<"Find, the value is"<<iter->second<<endl;
else
cout<<"Do not Find"<<endl;

if(map[key]){
...
}

// iterate
for(auto it=m.begin();it!=m.end();++it){
    cout << it->first << ':' <<it->second << endl;
}

// delete key
m.erase("Jack");

// clear all keys
m.clear();
```

## unordered_map

hash map

```cpp

```

## string

```cpp
// slice
s.substr(pos,len)

// length
s.length()
strlen(s);

// string to vector<int>
#include <sstream>

stringstream linestream(str);
vector<int> v;
int num;
while (linestream >> num) v.push_back(num);
```

## char

```cpp
// to int
ch - '0'
(int)ch

// to string
string s = ch
```

## int

```cpp
// to char
i + '0'
```

## math

```cpp
// ceil
(x+y-1)/y

max(7,7);
pow(base, e);
round(1.2) // 四舍五入
```

## binary search

```cpp
int low=0;
int hight =n;
while(low< high){
    int mid = (low+high)/2;
    if(condition(mid)){
        high = mid;
    }else{
        low = mid+1;
    }
}
return low // min(number) s.t. condition(number) is True
```

## backtrack / dfs

```cpp
void backtrack(candidate, state):
    if done;
        collect candidate to answer
    return;
    for c in candidates:
        make next_candidate
        backtrack(next_candidate, next_state)
        unmake
```
