function [g, h] = ConstraintFunc(x)
    s = 1000000;
    r = 20;
    vp = 72;

    g(1) = s - x(1) * sqrt(3)/2 * x(2)^2;
    g(2) = r - x(3);
    g(3) = 2*x(3) - r;
    
    h = pi * x(3) / vp * (1 - ((r / x(2))^2 * 2 * pi / sqrt(3)))^2 - x(4);
    
end