from math import log2

packet = 0
offet = 0

def getField(fieldWidth):
    global packet
    global offset
    offset -= fieldWidth
    return packet >> offset & ((1 << fieldWidth) - 1)

def parseBITS():
    sumVersion = 0
    version = getField(3)
    sumVersion += version
    type = getField(3)
    if type == 4:
        number = parseImmediateValue()
        #print(f'packet: V:{version} T:{type} N:{number}')
    else:
        lengthID = getField(1)
        if lengthID:
            #lengthID is 1
            #the next 11 bits is the number of sub-packets
            numSubPackets = getField(11)
            #print(f'packet: V:{version} T:{type} S:{numSubPackets}')
            for i in range(numSubPackets):
                #print(' ', end='')
                sumVersion += parseBITS()

        else:
            #lengthID is 0
            #the next 15 bits is the number of bits in the rest of the packet
            lengthOfSubPackets = getField(15)
            #print(f'packet: V:{version} T:{type} L:{lengthOfSubPackets}')
            global offset
            endOffset = offset - lengthOfSubPackets
            while offset > endOffset:
                #print(' ', end='')
                sumVersion += parseBITS()
            assert offset == endOffset

    return sumVersion

def parseImmediateValue():
    number = 0
    while True:
        continueBit = getField(1)
        section = getField(4)
        number = number << 4
        number += section
        if not continueBit:
            break
    return number



with open('input.txt','r') as f:
    for line in f:
        #line.strip() is a hex string
        #print(line.strip(), end=' ')
        packet = int(line.strip(),16)
        #print((int(log2(packet)/4)+1)*4)
        offset = len(line.strip())*4
        #print(offset)
        versionSum = parseBITS()
        print(versionSum)
#00111000000000000110111101000101001010010001001000000000
