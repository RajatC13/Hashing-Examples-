# Consistent and HRW hashing
A Restful key-value datastore to demonstrate Consistent and Rendezvous(HRW) hashing using Flask Restful.


#### Running the servers
```bash
$ python3 api.py 5000
```
```bash
$ python3 api.py 5001
```
```bash
$ python3 api.py 5002
```
```bash
$ python3 api.py 5003
```

#### Running the consistent hash client
```bash
$ python3 consitent_hash.py cause-of-death.csv
```

#### Running the HRW hash client
```bash
$ python3 hrw_hash.py cause-of-death.csv
```
