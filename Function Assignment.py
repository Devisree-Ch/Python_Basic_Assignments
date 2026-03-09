# Topic: Function Arguments
# Create a Python program that demonstrates the use of:
# ● Positional Arguments
# ● Default Arguments
# ● Keyword Arguments
# ● Variable Length Positional Arguments (*args)
# ● Variable Length Keyword Arguments (**kwargs)
def pos_arg(a,b):
	c=a+b
	print("positional arguments",c)
pos_arg(5,7)

def key_arg(b,a):
	c=a+b
	print("keyword arguments",c)
key_arg(a=5,b=7)

def defa_arg(b,c,a=90):
	d=a+b+c
	print("default arguments",d)
defa_arg(20,30)

def varpos_args(*args):
	print(*args)
varpos_args(10,20,30)

def varkey_args(**kwargs):
	print(kwargs)
varkey_args(a=90, b=90)

