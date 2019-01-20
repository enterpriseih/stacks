# mongodb

## basic

```bash
# install on centos
sudo vi /etc/yum.repos.d/mongodb-org-3.4.repo
# add
[mongodb-org-3.4]
name=MongoDB Repository
baseurl=<https://repo.mongodb.org/yum/amazon/2013.03/mongodb-org/3.4/x86_64/>
gpgcheck=1
enabled=1
gpgkey=<https://www.mongodb.org/static/pgp/server-3.4.asc>

sudo yum install -y mongodb-org

# dump
./mongodump --host <host> --port <port> --username <username> --password <password> --out <output_dir> --db <db>

# restore
mongorestore --host <host> --port <port> --username <username> --password <password> <backup_dir>

# start service
sudo service mongod start
```

## shell

### user & role
```js
// create
db.createUser({ user: "new_user", pwd: "new_password", roles:[{role:"dbOwner", db:"my_db"}],mechanisms : ["SCRAM-SHA-1"]})

// create role
db.getSiblingDB('my_db').createUser({ user: "new_user", pwd: "new_password", roles:[{role:"readWrite", db:"my_db"}]})
```

### db
```js
db.copyDatabase("source_db","target_db")
```

### collection
```js
// create collection
db.createCollection('new_collection');

// batch rename collections with prefix
db.getCollectionInfos().forEach( col => db.getCollection(col.name).renameCollection('prefix'+col.name))

// batch delete collection with prefix
db.getCollectionInfos().forEach( col => {if(col.name.startsWith('prefix')){db.getCollection(col.name).drop()}})

// copy from source_collection to target_collection
db.source_collection.find().forEach(function(v){db.target_collection.insert(v)});
```

### document
```js
// distinct
db.my_collection.distinct("key.nested_key",{$find})

view_date:{$gte: ISODate("2018-01-25T00:00:00.000Z"),$lt: ISODate("2018-03-23T00:00:00.000Z")}})

// update nested value
db.my_collection.updateOne({"key.nested_key":"value"},{$set:{"key.nested_key":"new_value"}})

// update new array item
db.my_collection.updateOne({"key":"value"},{$push:{"array_key":"new_item"}})

// update many
db.my_collection.updateMany({'key':'value'},{$set:{'key':'new_value'}});

// rename key
db.my_collection.updateMany({}, {$rename: {"old_key": "new_key"}})

// delete key
db.my_collection.updateMany({}, {$unset: {"key": ""}})
```
### aggregate operation
```js
// count total number of matched documents
db.my_collection.aggregate([
  {
    $match: {
      "time": {
        $gt: 1535760000000,
        $lt: 1538352000000,
      }
    }
  },
  {
    $count: "total"
  }
]).toArray();

// group by $user and accumulate each time
db.my_collection.aggregate([
  {
    $match: {
      "time": {
    		$gt: 1525363200000,
  			$lt: 15260832000000,
      }
    }
  },
  {
    $group: {
      _id: "$user",
      uniqueCount: {$addToSet: "$time"}
    }
  }
]).toArray()

// group by key and formatted time, sort
db.my_collection.aggregate([
  // use regex
  {
    $match: {
      "key":{$regex:/abc.*/,$options:'i'}
    }
  },
  // convert date
  {
    $project: {
      key:"key",
      date: { $add: [new Date(0), "$time"] }
    }
  },
  // formate date
  {
    $project: {
      key: "$key",
      day: {
        $dateToString: { format: " %Y-%m-%d", date: "$date" }
      }
    }
  },
  // group by day and key
  {
    $group: {
        _id: { day:"day", key:"key"},
        count: { $sum: 1 }
    }
  },
  // flatten
  {
    $project: {
      _id: 0,
      key: "$_id.key",
      day: "$_id.day",
      count: "$count"
    }
  },
  // sort
  {
    $sort: {
      "count": -1,
      "key": 1,
      "day": -1
    }
  }
]).toArray()

// lookup other collection
db.collection.aggregate([
  {
    $group:{
      _id: "$key",
      times: {$addToSet:"$time"}
    }
  },
  {
    $lookup:{
      from: "another_collection",
      localField: "_id",
      foreignField: "lookup_key",
      as: "another_key"
    }
  },
  {
    $project: {
      _id: 1,
      total: {$size: "$times"},
      key: {$arrayElemAt:["another_key", 0]},
    }
  }
]).toArray()

// print to csv
var cursor = db.my_collection.aggregate([
  ...
])
if (cursor && cursor.hasNext()) {
  print('key1,key2,key3,key4');
  while (cursor.hasNext()) {
    var item = cursor.next();
    print(tem.key1 + ',' + item.key2 + ',' + item.key3 + ',' + item.key4);
  }
}
```
