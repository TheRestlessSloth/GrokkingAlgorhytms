function [less,greater] = lessGreater(arr, a)
%LESSGREATER Summary of this function goes here
%   Detailed explanation goes here
less = [];
greater = [];
    
    for i = 1:length(arr)
        if arr(i)>a
            greater = [greater arr(i)];
        elseif arr(i)<a
            less = [less arr(i)];
        end
    end
end

