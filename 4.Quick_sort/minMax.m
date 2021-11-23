function [minMax, ind] = minMax(arr, polarity)
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here

minMax = arr(1);
ind = 1;

for i = 1:length(arr)
    if polarity>0
        if arr(i)>minMax
            ind = i;
            minMax = arr(i);
        end
    else
        if arr(i)<minMax
            ind = i;
            minMax = arr(i);
        end
    end
end