from math import log2
import numpy as np
packet = 0
offet = 0

def getField(fieldWidth):
    global packet
    global offset
    offset -= fieldWidth
    return packet >> offset & ((1 << fieldWidth) - 1)

def parseBITS():
    version = getField(3)
    type = getField(3)
    if type == 4:
        number = parseImmediateValue()
        #print('immediate', number)
        return number
        #print(f'packet: V:{version} T:{type} N:{number}')
    else:
        packetResults = list()
        lengthID = getField(1)
        if lengthID:
            #lengthID is 1
            #the next 11 bits is the number of sub-packets
            numSubPackets = getField(11)
            #print(f'packet: V:{version} T:{type} S:{numSubPackets}')
            for i in range(numSubPackets):
                #print(' ', end='')
                packetResults.append(parseBITS())

        else:
            #lengthID is 0
            #the next 15 bits is the number of bits in the rest of the packet
            lengthOfSubPackets = getField(15)
            #print(f'packet: V:{version} T:{type} L:{lengthOfSubPackets}')
            global offset
            endOffset = offset - lengthOfSubPackets
            while offset > endOffset:
                #print(' ', end='')
                packetResults.append(parseBITS())
            assert offset == endOffset
        #print(packetResults, end='       ')
        if type == 0:
            #print('sum', np.sum(packetResults))
            return sum(packetResults)
        elif type == 1:
            acc = 1
            #print(packetResults, end='       ')
            for n in packetResults:
                acc *= n
            #print('product', acc, np.product(packetResults))
            return acc
        elif type == 2:
            #print('min', np.min(packetResults))
            return np.min(packetResults)
        elif type == 3:
            #print('max',  np.max(packetResults))
            return np.max(packetResults)
        elif type == 5:
            #print('greater', 1 if packetResults[0] > packetResults[1] else 0)
            return (1 if packetResults[0] > packetResults[1] else 0)
        elif type == 6:
            #print('less', 1 if packetResults[0] < packetResults[1] else 0)
            return (1 if packetResults[0] < packetResults[1] else 0)
        elif type == 7:
            #print('equal', 1 if packetResults[0] == packetResults[1] else 0)
            return (1 if packetResults[0] == packetResults[1] else 0)


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
        #print(line.strip())#, end=' ')
        packet = int(line.strip(),16)
        #print((int(log2(packet)/4)+1)*4)
        offset = len(line.strip())*4
        #print(offset)
        print(parseBITS())
        
#00111000000000000110111101000101001010010001001000000000
