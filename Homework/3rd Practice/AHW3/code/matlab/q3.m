function q3()
rngx = 50;
rngh = 100;
n = linspace(-rngx, rngx, 2 * rngx + 1);
nh = linspace(-rngh, rngh, 2 * rngh + 1);
% a
x = u(n);
a = 0.5;
h = a .^ nh .* u(nh);
figure(1);
convp(x, h);
% b
x = u(n) - u(n - 3);
h = u(nh) - u(nh - 2);
figure(2);
convp(x, h);
% c
x = u(n - 5) - 2 * u(n);
h = u(nh - 3) - u(nh + 1);
figure(3);
convp(x, h);
% d
x = u(n - 3) - 2 * u(n + 2);
h = u(nh - 3) - u(nh + 1);
figure(4);
convp(x, h);
end

function y = u(n)
nu = n;
nu(nu == 0) = 1;
y = heaviside(nu);
end

function convp(x, h)
rngy = (size(x, 2) - 1) / 2;
ny = linspace(-rngy, rngy, 2 * rngy + 1);
y = zeros(1, size(ny, 2));
fh = h(end : -1 : 1);
for i = ny
    y(i + rngy + 1) = dot(x, fh(i + rngy + 1 : 1 : i + rngy + size(x, 2)));
end
y = y(end : -1 : 1);
subplot(3, 1, 1);
stem(ny, x);
title('x[n]');
subplot(3, 1, 2);
stem(ny, h(rngy + 1 : 1 : 3 * rngy + 1));
title('h[n]');
subplot(3, 1, 3);
stem(ny, y);
title('y[n] = x[n] * h[n]');
end