# Approximating $\pi$ using Monte Carlo sampling 

The value of $\pi$ can be obtained using the ratio of area of circle and area of square. Let, a circle with radius $a$ is inscribed inside a square (side=2$a$). 

Area of square = $4a^2$ <br />
Area of circle = $\pi r^2$ <br />

$\pi=4\frac{\mathrm{Area\;of\;circle}}{\mathrm{Area\;of\;square}}$

Here, Monte carlo sampling comes handy to approximate the area. We will randomly  throw darts aiming a square board which contains a circle. When, we have enough samples, then the  area will be proportional to  the number of darts on that region. So, $pi$ can be expressed as following, 

$\pi=4\frac{\mathrm{Number\;of\;darts\;inside\;circle}}{\mathrm{Total\;darts}}$


![](pi.gif)
