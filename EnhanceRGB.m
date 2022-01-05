function res = EnhanceRGB(img, delta1, delta2)
    %Contrast streching
    for i = 1:3
        temp = nonzeros(img(:, :, i));
        min_in = double(min(temp)) / 255;
        min_in = min_in * delta1;
        max_in = double(max(temp)) / 255;
        min_out = 0;
        max_out = max_in*delta2;
        if(max_out > 1)
            max_out = 1;
        end
        img(:, :, i) = imadjust(img(:, :, i), [min_in max_in], [min_out max_out]);
    end
    res = img;
end