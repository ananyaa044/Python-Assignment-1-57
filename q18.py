#18. Write a program to calculate the volume of a cube and a cuboid.
a=float(input("Enter the side length of the cube: "))
volume_cube=a**3
b=float(input("Enter the length of the cuboid: "))
c=float(input("Enter the breadth of the cuboid: "))
d=float(input("Enter the height of the cuboid: "))
volume_cuboid=b*c*d
print("Volume of the cube is:", volume_cube)
print("Volume of the cuboid is:", volume_cuboid)