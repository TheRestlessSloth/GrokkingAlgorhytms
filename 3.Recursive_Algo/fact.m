function [y] = fact(x)
%FACT Summary of this function goes here
%   Detailed explanation goes here
if(x == 1)
    y = 1;
else
    y = x * fact(x-1);
end

end

