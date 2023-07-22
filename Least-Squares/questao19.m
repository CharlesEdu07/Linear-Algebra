clc
clear

t = [10, 20, 30, 40, 50]';
Nb = [150000, 215000, 335000, 480000, 770000]';

A = [t ones(size(t))];

b = log(Nb);

x = inv(A' * A) * A' * b

f = x(1) * t + x(2);

plot(t, Nb, 'o')
hold on
plot(t, exp(f), 'r-', 'LineWidth', 2);
xlabel('Time (minutes)');
ylabel('Number of Bacteria');
title('Exponential Fit of Bacteria Growth');
legend('Exponential Fit');
grid on;

f = @(t) exp(x(1) * t + x(2))

f(60)

