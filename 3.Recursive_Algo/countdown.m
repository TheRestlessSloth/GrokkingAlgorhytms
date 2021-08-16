function [j] = countdown(i)
%COUNTDOWN Summary of this function goes here
%   Detailed explanation goes here
    j = i
    if(i <= 0)
        return
    else
    countdown(i-1);
    end
end

