import turtle

alice = turtle.Turtle()
bob = turtle.Turtle()
other = turtle.Turtle()

alice.speed(15)
bob.speed(15)

def square(t, lgt):
	for i in range(4):
		t.fd(lgt)
		t.lt(90)

def two_square(t, T):
	t.lt(90)
	T.lt(90)
	for i in range(4):
		t.fd(100)
		T.fd(100)
		t.lt(90)
		T.lt(90)

def polygon(t, n, lgt):
	angle = 360.0 / n
	for i in range(n):
		t.fd(lgt)
		t.lt(angle)

def par_polygon(t, T, n, lgt):
	T.lt(90)
	t.lt(180)
	ang = 360.0 / n
	for i in range(n):
		t.fd(lgt)
		T.fd(lgt)
		t.lt(ang)
		T.lt(ang)

def primer_mosaico(t, T, n, l, r):
	t.lt(30)
	T.lt(45)
	msc = 360.0 / r
	ang = 360.0 / n
	for i in range(r):
		t.lt(msc)
		T.lt(msc)
		for i in range(n):
			t.fd(l)
			T.fd(l)
			t.lt(ang)
			T.lt(ang)

def second_mosaico(t, T, n, l, r):
	t.lt(90)
	T.lt(45)
	msc = 360.0 / r
	ang = 360.0 / n
	for i in range(r):
		t.lt(msc)
		T.lt(msc)
		for i in range(n):
			t.fd(l)
			T.fd(l)
			t.lt(ang)
			T.lt(ang)

def third_mosaico(t, T, n, l, r):
	t.lt(180)
	msc = (360.0 * r) / n
	ang = 360.0 / n
	for i in range(r):
		t.lt(msc)
		T.lt(msc)
		for i in range(n):
			t.fd(l)
			T.fd(l)
			t.lt(ang)
			T.rt(ang)

def ft_mosaico(t, T, n, l, r):
	for i in range(4):
		t.lt(90)
		T.lt(90)
		third_mosaico(t, T, n, l, r)

def fth_mosaico(t, T, n, l, r):
	t.lt(180)
	msc = (360.0 * r) / n
	ang = 360.0 / n
	for i in range(r):
		t.lt(msc)
		T.rt(msc)
		for i in range(n):
			t.fd(l)
			T.fd(l)
			t.lt(ang)
			T.rt(ang)

def sxt_mosaico(t, T, n, l, r):
	t.lt(180)
	msc = (360.0 * r) / n
	ang = 360.0 / n
	for i in range(r):
		t.lt(msc)
		T.rt(msc)
		for i in range(n):
			t.fd(l)
			T.fd(l)
			t.lt(ang)
			T.lt(ang)
