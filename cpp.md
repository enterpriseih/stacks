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
#include <limits.h>

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

// split line with custom separator
#include<sstream>
string tmp,s;
getline(cin, s);
for(int i=0;i<tmp.size();++i){
    if(tmp[i] == ';'){
        tmp[i] =' ';
    }
}
stringstream ss(s);
while(ss >> t) {
    ...
}

// read line by line
string s;
while(getline(cin,s)){
    ...
}

// read line by custom separator
getline(cin, s)
stringstream ss(s);
string a;
while(getline(ss,a,',')){
}

// read 1/2
int a,b;
char ch;
cin >> a >> ch >> b;

// output float with precision
#include<iomanip>
cout << fixed <<setprecision(1) << 1.22; // 小数点后一位，输出 1.2
cout << setprecision(1) << 1.22; // 保留一位，输出 1

```

## class

```cpp
class Node
{
private:
    int val {0};
    Node* left {NULL};
    Nodd* right {NULL};

public:
    Node(){};
    Node(int val): val(val), left(NULL), right(NULL){}
    Node(int val, Node* left, Node* right): val(val), left(left), right(right){}
}

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

// ListNode
struct ListNode
{
    int       m_nKey;
    ListNode* m_pNext;
};

ListNode *head = new ListNode;
ListNode *node = new ListNode;
node->m_nKey = v;
head->m_pNext = node;
```

## array

fixed-length

```cpp
// init
int a[128] = {0};

// init multidimensional with zero bit
int a[5][10][10];
memset(a,0,sizeof(a)); // old c function

// fill 1d list with number
int a[10];
fill(a, a+10,100);

// fill 2d list with number
int a[10][10];
fill(a[0], a[0]+100,100);

// copy 1d
int b[128];
copy(a,a+128, b);

// copy multidimensional
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

## multiset

search, insert, erase is O(log n)

```cpp
multiset <int, greater <int> > s;
multiset <int, greater <int> > s (s1.begin(),s1.begin()+t);
s.insert(1);
s.erase(1);
s.erase(s.equal_range(1).first);
auto search = s.find(2);
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

## pair

```cpp
pair<int,int> p(1,1);

pair<int, int> p;
p = make_pair(1, 1);

p.first = 2;
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
// init
unordered_map<string, string>umap = {{"12", "234"}};

// delete key
umap.erase("12");

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

stringstream ss(str);
vector<int> v;
int num;
while (ss >> num) v.push_back(num);

// to int, aggresively from start, if cannot throw error
stoi(s)
stoi(s, nullptr, 16) // hex string to int

// dict sort
a.compare(b)<0;

// find substr
string s = "1234"
s.find("123")
s.find("3",1) // find from "2"
s.find("5") == s.npos
```

## char

```cpp
// to int
ch - '0'
(int)ch

// check is num
(int)ch >= 48 && (int)ch <= 57

// to string
string s = ch
```

## bitset

```cpp
#include<bitset>
// from string
string a = "0101"
bitset<8> a2(a); // [0,0,0,0,0,1,0,1]

// from unsigned long
unsigned long  b = 123;
bitset<8> b2(b);

// to string
a2.to_string() // "00000101"

// to int
(int)(a2.to_ulong())

```

## int

```cpp
// to char
i + '0'

// to string
to_string(i)

// to bit
#include <bitset>
bitset<8> b(836);
cout << b << endl;
b.to_string(); // to bit string
```

## math

```cpp
(x+y-1)/y // ceil
max(7,7);
pow(base, e);
round(1.2) // 四舍五入
```

## binary search

```cpp
// template
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

//lower_bound: first element >= target
int s[10]
auto pos = lower_bound(s,s+10, target) - s;

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
