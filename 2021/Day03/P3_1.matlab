text = strsplit(fileread("input.txt"));
text = transpose(text(1:1000));
arr = char(text);
numArr = arr - '0';
s = size(numArr);
value = sum(numArr,1) >= s(1)./2;
mostCommon = bin2dec(sprintf('%d',value));
leastCommon = bin2dec(sprintf('%d',~value));
mostCommon * leastCommon
