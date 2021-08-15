function [smallest] = findSmallest(array)
global smallest_index;
smallest = array(1);
smallest_index = 1;
for i = 1:length(array)
   if array(i) > smallest
       smallest = array(i);
       smallest_index = i;
   end
end
end

