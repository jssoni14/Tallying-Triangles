def main():
  final_array=[]
  triangle_array = []
  f = open("triangle_inputs.txt", "r")
  for t in f:
    triangle_array.append(t.split())
  for x in triangle_array:
    

    z=[]
    z = [int(x[0]),int(x[1]),int(x[2])]
    z.sort()
   
    a_side = z[0]
    b_side = z[1]
    c_side = z[2]
    
    if ((a_side + b_side > c_side) and (a_side + c_side > b_side) and (b_side + c_side > a_side)):
      final_array.append('True')
   
  print("Number of triangles is: {}".format(len(final_array)))
  
if __name__ == main():
  main()