function [out] = quick_sort(arr)
%QUICK_SORT Summary of this function goes here
%   Detailed explanation goes here
    if length(arr) < 2
        out = arr;
    elseif length(arr) == 2
        if arr(1) > arr(2)
            arr = fliplr(arr);
        end
        out = arr;
    else
        piv = arr(int16((length(arr)-1)/2)); %pivot
        [less,greater] = lessGreater(arr,piv);
        out = [quick_sort(less) piv quick_sort(greater)];
    end
end

