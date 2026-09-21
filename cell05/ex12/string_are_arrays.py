import sys

if len(sys.argv) != 2:
    print("none")
else:
    z_count = 0
    for char in sys.argv[1]:
        if char == 'z':
            z_count += 1
            
    if z_count > 0:
        print("z" * z_count)
    else:
        print("none")
