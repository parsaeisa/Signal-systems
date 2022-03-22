function q5c()
n = linspace(0, 99, 100);
x = u(n);
y1 = conv(ones(1, 5), x);
y2 = conv([1, -1, -1, -1, 1], x);
y = conv(ones(1, 3), y1 + y2);
h = [2, 2, 2, 0, 2, 2, 2];
yp = conv(h, x);
subplot(2, 1, 1);
stem(y);
title('y[n] from question');
subplot(2, 1, 2);
stem(yp);
title('y[n] from solution a');
end

function y = u(n)
nu = n;
nu(nu == 0) = 1;
y = heaviside(nu);
end