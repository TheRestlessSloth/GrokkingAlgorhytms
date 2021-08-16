function [] = pseudo_look_for_key_1(main_box)
%LOOK_FOR_KEY Summary of this function goes here
%   Detailed explanation goes here
pile = main_box.make_a_pile_to_look_trough()
while pile ~= []
    box = pile.grab_a_box()
    for i = 0:items
       if (item == box)
        pile.append(item)
       elif (item == key)
        disp("found a key!")
    end
end

