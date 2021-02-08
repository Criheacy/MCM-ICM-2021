function f = geo_type(X,Y,Z,x,y)
    f = griddata(X,Y,Z,x,y);
end