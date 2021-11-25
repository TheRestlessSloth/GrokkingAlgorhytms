function [less,greater] = lessGreater(arr, a)
%support function. selects all digits in array that lower and higher 
%than selected element

%todo: from 1 to i-1, from i+1 to end
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

