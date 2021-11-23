clc; clear all; close all;

a = [11 9 15 10 15 19];

lin_sum = sumAr(a);
rec_sum = sumAr_rec(a);

[m,i] = minMax(a,-1);

[less,greater] = lessGreater(a,8);

quick_sort(a)
print_items(a);
print_items2(a);