function f = GoalFunc(x)
    vf = 6.8;
    a = 129.6;
    qcost = 46623000;
    pcost = 10000;
    f = pi * (vf * x(4) + vf^2/(a*2))^2 * qcost + pcost * x(1);
end