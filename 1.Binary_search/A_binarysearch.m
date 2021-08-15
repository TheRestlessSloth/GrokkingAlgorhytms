clc; clear;

arr = 1:500;
m = 482;
min = arr(1);
max = length(arr);

while (min <= max)
    mid = round((max + min)/2);
    guess = arr(mid);
    if(guess == m)
       c = "success!";
    end
    if(guess > m)
        max = mid - 1;
    else(guess < m)
        min = mid + 1;
    end
end
guess
m
c