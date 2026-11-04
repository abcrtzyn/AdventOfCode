from typing import List
import numpy as np
packet = 0
offet = 0

def getField(fieldWidth: int):
    global packet
    global offset
    offset -= fieldWidth
    return packet >> offset & ((1 << fieldWidth) - 1)

def parseBITS() -> int:
    _version = getField(3)
    typee = getField(3)
    if typee == 4:
        number = parseImmediateValue()
        #print('immediate', number)
        return number
        #print(f'packet: V:{version} T:{type} N:{number}')
    else:
        packetResults: List[int] = []
        lengthID = getField(1)
        if lengthID:
            #lengthID is 1
            #the next 11 bits is the number of sub-packets
            numSubPackets = getField(11)
            #print(f'packet: V:{version} T:{type} S:{numSubPackets}')
            for _ in range(numSubPackets):
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
        if typee == 0:
            #print('sum', np.sum(packetResults))
            return sum(packetResults)
        elif typee == 1:
            acc = 1
            #print(packetResults, end='       ')
            for n in packetResults:
                acc *= n
            #print('product', acc, np.product(packetResults))
            return acc
        elif typee == 2:
            #print('min', np.min(packetResults))
            return int(np.min(packetResults))
        elif typee == 3:
            #print('max',  np.max(packetResults))
            return int(np.max(packetResults))
        elif typee == 5:
            #print('greater', 1 if packetResults[0] > packetResults[1] else 0)
            return (1 if packetResults[0] > packetResults[1] else 0)
        elif typee == 6:
            #print('less', 1 if packetResults[0] < packetResults[1] else 0)
            return (1 if packetResults[0] < packetResults[1] else 0)
        elif typee == 7:
            #print('equal', 1 if packetResults[0] == packetResults[1] else 0)
            return (1 if packetResults[0] == packetResults[1] else 0)
        else:
            assert False, 'unreachable'


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
