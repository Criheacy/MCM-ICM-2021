function [g, h] = ConstraintFunc(x)
    s = 1000;
    g = s - x(1) * sqrt(3)/2 * x(2)^2;
    
    vp = 72;
    r = 20;
    h = pi * r / vp * (1 - ((r / x(2))^2 * 2 * pi / sqrt(3)))^2 - x(4);
end