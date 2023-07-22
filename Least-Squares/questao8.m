clc
clear

t = [1960:10:2000]';
P = [12600 14000 16100 19100 23200]';

A = [t.^2 t ones(size(t))];

x = inv(A' * A) * A' * P

plot(t, P, 'o')

f = x(1)*t.^2 + x(2)*t + x(3);

hold on
plot(t, f)

f = @(t) x(1)*t.^2 + x(2)*t + x(3)

f(2010)
