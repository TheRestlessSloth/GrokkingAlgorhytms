function [] = pseudo_look_for_key_2(box)
%LOOK_FOR_KEY Summary of this function goes here
%   Detailed explanation goes here
    for i = 0:len(item)
        if(item == box)
            pseudo_look_for_key_2(item);
        else
            if(item == key)
                disp("found a key!");
            end
        end
    end
end

