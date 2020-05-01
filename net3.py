from net import Net
net = Net()

x = net.variable(1)
y = net.variable(2)
z = net.variable(3)
x2 = net.mul(x, x)
y2 = net.mul(y, y)
z2 = net.mul(z, z)
q = net.add(x2,y2)
o  = net.add(q,z2)
'''
print('net.forward()=', net.forward())
print('net.backward()')

net.backward()
print('x=', x, 'y=', y, 'o=', o)
print('gfx = x.g/o.g = ', x.g/o.g, 'gfy = y.g/o.g=', y.g/o.g)
print('x2=', x2, 'y2=', y2)
'''
net.gradient_descendent()
print('x=', x.v, 'y=', y.v,'z=', z.v)
