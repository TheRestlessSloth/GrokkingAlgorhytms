clc;clear all; close all;
%Euclidian algo

a = 161;
b = 28;

while (a~=0) & (b ~= 0)
    if a>b
        a = mod(a,b);
    else
        b = mod(b,a);
    end
end
a+b