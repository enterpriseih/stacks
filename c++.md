# c++

## I/O

```c++
// scanf
// reads strings except `\s`, `\t` and `return`(win:\r\n,mac:\r,linux:\n)
int hh,mm,ss;
char ap[3]; // size should be 2+1 to include \0
scanf("%d:%d:%d%s", &hh, &mm, &ss, ap); //char[] don't use &

// printf
printf("%02d:%02d:%02d",hh,mm,ss); // leading zero, fixed length

// sprintf
char buf[3];
sprintf(buf, "%02d", 2); // "02"

// getline
cin.ignore();
getline(cin, s);

// cout
cout << setprecision(6) << float(a) << endl;
```

## string or char[]


```c++
// compare
strcmp(ap,"AP") == 0;

// length, from start to \0 (not include)
strlen(ap);

// find first
str.find();
    
// find last
found = str.rfind(key);

// slice
str.substr(pos, length);

// size
str.size();

// str -> stringstream -> vector<int>
stringstream ss(str);
vector<int> v;
char ch;
int i;
while(ss >> i){
    v.push_back(i);
    ss >> ch;
}
```

## map

```c++
// assign
m[key] = value;

// in
m.count(key) == 1;

```
