function [newArr] = Sort(arr)
global smallest_index
newArr = [];
for i = 1:length(arr)
   small = findSmallest(arr);
   newArr = [newArr small];
   arr(smallest_index) = [];
end
end

