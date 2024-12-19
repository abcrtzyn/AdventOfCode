text = strsplit(fileread("input.txt"));
text = transpose(text(1:1000));
arr = char(text);
numArr = arr - '0';
logArr = logical(numArr);
% begin processing
processingArr = logArr;
for bit = 1:12
    keepBit = sum(processingArr(:,bit),1) >= s(1)./2;
    processingArr = processingArr(processingArr(:,bit) == keepBit,:);
    s = size(processingArr);
    if s(1) == 1
        break
    end
end
mostCommon = bin2dec(sprintf('%d',processingArr));
processingArr = logArr;
for bit = 1:12
    keepBit = sum(processingArr(:,bit),1) < s(1)./2;
    processingArr = processingArr(processingArr(:,bit) == keepBit,:);
    s = size(processingArr);
    if s(1) == 1
        break
    end
end
leastCommon = bin2dec(sprintf('%d',processingArr));
mostCommon * leastCommon