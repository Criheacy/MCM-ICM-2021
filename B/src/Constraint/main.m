options = optimset;
[x, y] = fmincon('GoalFunc', rand(4,1), [], [], [], [], ...
    zeros(4,1), [], 'ConstraintFunc', options);