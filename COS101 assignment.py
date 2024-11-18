def math_operations_option():
    print('\nMaths and physics operations option:')
    print('a. Volume of a rectangular prism')
    print('b. Volume of a cylinder')
    print('c. Perimeter of a rectangle')
    print('d. Circumference of a a circle')
    print('e. Surface area of a sphere')
    print('f. Finishing ')

math_operations_option()

options = input('pick an option from a to f  ')
print(options)

if options == 'a':
    length = int(input('Enter length of prism  '))
    height = int(input('enter height of prism  '))
    width = int(input('Enter width of prism'))
    volume_of_a_rectangular_prism = width * length * height
    print(volume_of_a_rectangular_prism)

elif options == 'b':
    radius = int(input('Enter number  '))
    height = int(input('Enter number  '))
    volume_of_a_cylinder = 22/7 * (radius ** 2) * height
    print(volume_of_a_cylinder)

elif options == 'c':
    length = int(input('Enter number  '))
    breadth = int(input('Enter number  '))
    perimeter_of_a_rectangle = 2 * (length + breadth)
    print(perimeter_of_a_rectangle)

elif options == 'd':
    radius = int(input('Enter number radius of circle  '))
    circumference_of_a_circle = 2 * 22/7 * radius
    print(circumference_of_a_circle)

elif options == 'e':
    radius = int(input('Enter value for radius  '))
    surface_area_of_a_sphere = 4 * 22/7 * (radius ** 2)
    print(surface_area_of_a_sphere)

elif options == 'f':
    name = 'ELUMA DANIEL  '
    matric = 'BHU/24/04/05/0115  '
    end = name + matric
    print(end)

else:
    print("PLEASE CHOOSE AN OPTION FROM a TO f")