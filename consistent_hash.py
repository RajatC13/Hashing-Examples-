import csv, sys, requests, json


class ConsistantHash:
    def __init__(self, servers, filename):
        self.servers = servers
        self.filename = filename
        cnt = len(self.servers)
        x = 10000/cnt
        intv = 0
        self.interval = []
        self.interval.append(0)
        for i in range(cnt):
            intv = intv + x
            self.interval.append(abs(intv))


    def send(self, key, value, port):
        address = 'http://localhost:'+str(port)+'/api/v1/entries'
        resp1 = requests.post(address, json={str(key) : value})

    def find_server(self, key):
        for i in range(len(self.interval) - 1):
            if (key > self.interval[i]) and (key <= self.interval[i+1]):
                return i
        return 0


    def key_maker(self, hstring, v):
        key = abs(hash(hstring)) % (10 ** 4)
        value = v
        server_number = self.find_server(key)
        port = str(self.servers[server_number])
        self.send(key,value,port)

    def print_stats(self):
        stat = []
        for s in self.servers:
            address = 'http://localhost:'+str(s)+'/api/v1/entries'
            lists = requests.get(address)
            a = lists.json()
            count = a["num_entries"]
            stat.append(count)
            print(lists.json())
        i = 0
        for i in stat:
            print(i)

    def consitent_hash(self):
        with open('cause-of-death.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            print('Uploading Started')
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    h = row[0]+":"+row[2]+":"+row[3]
                    v=row[0]+", "+row[1]+", "+row[2]+", "+row[1]+", "+row[3]+", "+row[4]+", "+row[5]
                    print(line_count)
                    self.key_maker(h, v)
                    line_count += 1
            print('Uploading copleted')
            self.print_stats()


if __name__ == '__main__':
    serv_length = len(sys.argv)
    servers = ['5000','5001','5002','5003']
    """
    for i in range(1, serv_length,1):
        servers.append(sys.argv[i])
    """
    filename = sys.argv[1]
    c = ConsistantHash(servers,filename)
    c.consitent_hash()
