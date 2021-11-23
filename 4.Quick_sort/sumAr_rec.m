function [out] = sumAr_rec(in)
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
if isempty(in)
    out = 0;
else
    out = in(1) + sumAr_rec(in(2:end));
    in(1) = [];
end

end

