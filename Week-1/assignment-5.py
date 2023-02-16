pi = 3.142
#surface area of a cylinder (4*pi*r^2)+(2*pi*r*h)
r = input("Enter the radius of the cylinder:  ")
h = input("Enter the height of the cylinder:  ")
surface_area_cylinder = (2*pi*int(r)*int(r))+(2*pi*int(r)*int(h))
print(surface_area_cylinder)

#volume of a sphere (4/3*pi*r^3)
s = input ("Enter the radious of the sphere: ")
volume_sphere = 4/3*pi*int(s)*int(s)*int(s)
print(volume_sphere)

#volume of a cylinder (pi*r^2*h)
a = input("Enter the radius of the cylinder: ")
b = input("Enter the height of the cylinder: ")
volume_cylinder = pi*int(a)*int(a)*int(b)
print(volume_cylinder)
