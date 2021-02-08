x=-20:0.5:20;
y=-20:0.5:20;
u1 = 0;
u2 = 0;        
sigma1 = 10;
sigma2 = 10;
rou = 0.5;
mu=[0,0];
[X,Y]=meshgrid(x,y);
p = 1/(2*pi*sigma1*sigma2*sqrt(1-rou*rou)).*exp(-1/(2*(1-rou^2)).*[(X-u1).*(X-u1)/(sigma1*sigma1)-2*rou*(X-u1).*(Y-u2)/(sigma1*sigma2)+(Y-u2).*(Y-u2)/(sigma2*sigma2)]);
figure(2)
mesh(X,Y,p)
shading interp
