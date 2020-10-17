#this is CO endsem assignment on Cache mapping
#made by SATWIK TIWARI (2019100) .

lol = """press:
'1' for Direct Mapping
'2' for Fully Associative Mapping
'3' for n-way Set Associative Mapping
"""

print(lol)
mapping = int(input())
print("Enter Cache Size :")
csize = int(input())
print("Enter Cache Lines :")
cl = int(input())
x = 0
while(2**x<cl):
    x+=1
line = x #bits req to store the number cache lines
print('Enter Block Size :')
bsize = int(input())
x = 0
while(2**x<bsize):
    x+=1
blockoffset = x #bits req to store block number

if(mapping == 1):
    cache = [[] for i in range(cl)]
    print("Enter number of operations: ")
    t = int(input())
    for p in range(0,t):
        print('Enter "read" or "write" in lowercase as shown: ')
        s = input()
        if(s=='read'):
            addr = input()
            blocknumber = int(addr,2)//bsize
            cacheline = blocknumber%cl
            address = addr[:len(addr) - (line+ blockoffset)] #tag of given address
            tagsize = len(addr) - (line+blockoffset)

            if(cache[cacheline] == []):
                print('Cache Miss : ' , 'B'+str(blocknumber)+' is loaded in line no. '+str(cacheline))
                cache[cacheline] = [address,'null']
            else:
                temp = cache[cacheline][0]
                if(address == temp):
                    print('Cache Hit: ' + cache[cacheline][1])
                else:
                    cache[cacheline] = [address,'null']
                    print('Cache miss: '+ 'B'+str(blocknumber)+' is placed in line no. '+str(cacheline))
        else:
            addr = input()
            data = input()
            blocknumber = int(addr,2)//bsize
            cacheline = blocknumber%cl
            address = addr[:len(addr) - (line+ blockoffset)] #tag of given address
            tagsize = len(addr) - (line+blockoffset)
            cache[cacheline] = [address,data]

        #disadvantage - conflict miss. that it is we have extra space
        # still we will put B1,B5,B9 at same pos and then
        # if B1 is called again it will again give miss. this is called conflict miss
        print(cache)

if(mapping == 2):
    cache = [[] for i in range(cl)]
    print('Enter number of operations: ')
    t = int(input())
    for p in range(0,t):
        #using FIFO

        print('Enter "read" or "write" in lowercase as shown: ')
        s = input()
        if(s == 'read'):
            adr = input()
            blocknumber = int(adr,2) // bsize
            tag = adr[:len(adr) - blockoffset]
            tagsize = len(tag)
            f = True
            for i in range(0,len(cache)):
                if(cache[i] == []):
                    print('Cache miss: '+ 'B'+str(blocknumber)+' is placed in line no. '+ str(i))
                    cache[i] = [tag,'null']
                    f = False
                    break
                elif(cache[i][0] == tag):
                    print('Cache Hit : '+ cache[i][1])
                    f = False
                    break
            if(f):
                print('Cache miss: According to FIFO , B'+ str(blocknumber)+ ' is placed removing first inserted')
                cache.remove(cache[0])
                cache.append([tag,'null'])
        else:
            adr = input()
            data = input()
            blocknumber = int(adr,2) // bsize
            tag = adr[:len(adr) - blockoffset]
            tagsize = len(tag)
            f = True
            for i in range(0,len(cache)):
                if(cache[i] == []):
                    cache[i] = [tag,data]
                    f = False
                    break
                elif(cache[i][0] == tag):
                    cache[i][1] = data
                    f = False
         

        

        print(cache)


if(mapping == 3):
    cache = [[] for i in range(cl)]
    print('enter the value of k: ')
    k = int(input())
    print('Enter number of operations: ')
    t = int(input())
    for p in range(0,t):
        print('Enter "read" or "write" in lowercase as shown: ')
        s = input()
        if(s=='read'):
            adr = input()
            blocknumber = int(adr,2) // bsize
            numberofsets = cl//k
            set = blocknumber%numberofsets
            temp = k*set
            #for bits req to represent set
            x=0
            while(2**x<numberofsets):
                x+=1
            tag = adr[:len(adr) - (x+blockoffset)]
            f = True
            for i in range(temp,temp+k):
                if(cache[i] == []):
                    print('Cache miss: '+ 'B'+str(blocknumber)+' is placed in line no. '+ str(i) +' in setno. '+str(set))
                    cache[i] = [tag,'null']
                    f = False
                    break
                elif(cache[i][0] == tag):
                    print('Cache Hit : '+ cache[i][1])
                    f = False
                    break
            if(f):
                print('Cache miss: According to FIFO , B'+ str(blocknumber)+ ' is placed removing first inserted in setno. '+ str(set))
                aisehi = cache[temp:temp+k]
                aisehi.remove(aisehi[0])
                aisehi.append([tag,'null'])
                cache = cache[:temp] + aisehi + cache[temp+k:]
        else:
            adr = input()
            data = input()
            blocknumber = int(adr,2) // bsize
            numberofsets = cl//k
            set = blocknumber%numberofsets
            temp = k*set #index in cache where this associative starts.
            #for bits req to represent set
            x=0
            while(2**x<numberofsets):
                x+=1

            tag = adr[:len(adr) - (x+blockoffset)]
            f = True
            for i in range(temp,temp+k):
                if(cache[i] == []):
                    cache[i] = [tag,data]
                    f = False
                    break
                elif(cache[i][0] == tag):
                    cache[i][1] = data
                    f = False
                    break
            if(f):
                aisehi = cache[temp:temp+k]
                aisehi.remove(aisehi[0])
                aisehi.append([tag,data])
                cache = cache[:temp] + aisehi + cache[temp+k:]

        print(cache)




