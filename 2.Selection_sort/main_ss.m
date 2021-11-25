clc; clear;
n = 100;
arr = (unifrnd(1,n,1,n));
subplot(2,1,1);
plot(arr);
arr = Sort(arr);
subplot(2,1,2);
plot(arr);