# cpp

## vim

```
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

## vector

### print

```cpp
for(const int& k : ks){
    cout << k << " ";
}
```

### concat

```cpp
b.insert(b.end(), a.begin(), a.end());
```

### slice

```cpp
v2 = vector<int>(v1.begin() + 1, v1.end());
```

### iterate

```cpp
for(const auto& v: values) {
    std::cout << v << "\n";
}
for(int i=0;i<v3.size();i++){
    cout<<v3[i]<<' ';
}
```

### delete

```cpp
v.erase(v.begin()+1);
v.erase(v.begin()+2,v.begin()+5);
```

### init

```cpp
vector<int> vect{ 10, 20, 30 };
vector<double> v3(10,0) // 10 zeros

```

### access

```cpp
v3[2]= 1
```

### insert

```cpp
v.push_back(9);
v.insert(v.begin()+2,1);
```

### sort

```cpp
sort(v.begin(), v.end());

bool cmp(const int &l, const int &r)
{
    return l > r; // desc
}
sort(v.begin(), v.end(), cmp);
```

## set

### init

```cpp
set<int> s;
```

### insert

```cpp
s.insert(5);
```

### loop

```cpp
set<int>::iterator it;
for(it=s1.begin();it!=s1.end();it++)
    cout<<*it<<endl;
```

### delete

```cpp
s.erase(5);
```

### exits

```cpp
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

### init

```cpp
struct subject {
    string name;
    int marks;
    int credits;
};
vector<subject> sub;
sub.push_back(subject());
```

## map

### init

```cpp
map<int,int> map;
map<int,int> map = {{1,1},{2,2}};
```

### assign

```cpp
map[key] = value;
```

### check key exist

```cpp
iter = mapStudent.find("123");
if(iter != mapStudent.end())
    cout<<"Find, the value is"<<iter->second<<endl;
else
    cout<<"Do not Find"<<endl;

if(map[key]){
    ...
}
```

### iterate

```cpp
map<string,double>::iterator it;
    for(it=m.begin();it!=m.end();it++)
        cout<<(*it).first<<":"<<(*it).second<<endl;
```

### delete key

```cpp
m.erase("Jack");
```

### clear all keys

```cpp
m.clear();
```

## string

```cpp

```

### slice

```cpp
s.substr(pos,len)
```

### length

```cpp
s.length()
```

## char

### to int

```cpp
ch - '0'
```

### to string

```cpp
string s = ch
```

## int

### to char

```cpp
i + '0'
```

## math

### ceil

```cpp
(x+y-1)/y
```

### max

```cpp
std::max(7,7);
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

## backtrack

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
