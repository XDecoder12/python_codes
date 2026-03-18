import mlx.core as mx

a = mx.array([1,2,3])
b = mx.array([4,5,6])

c = mx.add(a, b, stream=mx.gpu)
d = mx.multiply(a, b, stream=mx.cpu)

mx.eval(c)
mx.eval(d)

print(c)
print(d)
