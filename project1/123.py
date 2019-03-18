def fun(x,l=[]):
    for i in range(x):
        l.append(i*i)
    print(l)

fun(2)
fun(3,[3,2])
fun(3)