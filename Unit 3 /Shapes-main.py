
import shapes

print("1: Circle")
print("2: Rectangle")
print("3: Triangle")

pick = input("Select a shape: ")

if pick == '1':
    val = float(input("Enter radius: "))
    ans = shapes.area_c(val)
    print(f"Area is: {ans}")

elif pick == '2':
    x = float(input("Enter length: "))
    y = float(input("Enter width: "))
    ans = shapes.area_r(x, y)
    print(f"Area is: {ans}")

elif pick == '3':
    x = float(input("Enter base: "))
    y = float(input("Enter height: "))
    ans = shapes.area_t(x, y)
    print(f"Area is: {ans}")

else:
    print("Invalid selection")
  
