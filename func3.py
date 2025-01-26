glx = 5
print("glx before the function:", glx)
def newFunc():
    locXXX = 1000
    global glx
    glx = 100
    print("glx inside of the function:", glx)

newFunc()
glx = locXXX
print("glx outside of function", glx)
newFunc()
