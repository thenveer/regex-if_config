import subprocess
import re
import sys

def get_interfaces(filename): 
  with open(filename, 'w+') as f:
    ip = subprocess.run('ifconfig', stdout=f, stderr=subprocess.DEVNULL)


def get_ip(fname):
    get_interfaces(fname)
    with open(fname) as f:
        d={}
        for i in f:
            pattern1 = re.compile('^([A-Za-z0-9]+).*')
            if pattern1.match(i):
                 interface = pattern1.match(i).groups()[0]

            pattern2=re.compile('^[\s]+inet+\s([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)')
            if pattern2.match(i):
                address = pattern2.match(i).groups()[0]
                d[interface] = address
        return d



def main():
    a=get_ip(sys.argv[1])
    print(a)
if __name__ == "__main__":
    main()
