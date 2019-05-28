class RedBlackTree:
	class _vertex:
		def __init__(self):
			self.color=None 		#b for black and r for red
			self.key=None			#data
			self.right=None			#right child
			self.left=None			#left child
			self.p=None				#parent

	def __init__(self):
		
		self.root=RedBlackTree._vertex()
		self.root.color='b'

	#need to implement
	def __str__(self):
		return

	#insert generic binary tree insert
	def _insert(self, z):
		y=None						#parent of current point
		x=self.root					#point of insertion
		while (x is not None):		#loop until point of insertion is found
			y=x
			if(z.key<x.key):
				x=x.left
			else:
				x=x.right
		z.p=y
		if(y is None):				#y is only none when the tree is empty
			root=z
		elif(z.key<y.key):
			y.left=z
		else:
			y.right=z
		
	#in the middle of implementing
	def rb_insert(self, key):
		x=RedBlackTree._vertex()
		x.key=key
		_insert(x)
		x.color='r'
		while((x.key != self.root.key) and (x.p.color=='r')):
			if(x.p.data==x.p.p.left.data):
				y=x.p.p.right
				if(y.color=='r'):
					x.p.color='b'
					y.color='b'
					x.p.p.color='r'
				elif(x.key==x.p.right.key):
					x=x.p
					_left_rotate(x)
					x.p.color='b'			#???????
					x.p.p.color='r'			#???????
					_right_rotate(x.p.p):	#???????
				else:
					return

	def _black_height(self):
		return
			
	#need to implement
	def delete(self, key):
		return
		
	def _left_rotate(self, x):
		y=x.right					#make ptr to right child
		x.right=y.left				#change right child of x
		if(y.left is not None):		#make x the parent of y.left if not null
			y.left.p=x
		y.p=x.p						#set y's parent to x's parent
		if(x.p is None):			#check if x's parent is root
			self.root=y
		elif(x==x.p.left):			#check if x was a left vertex
			x.p.left=y
		else:						#x is resolved to be a right child
			x.p.right=y
		y.left=x
		x.p=y
	
	def _right_rotate(self, y):
		x=y.left
		y.left=x.right
		if(x.right is not None):
			x.right.p=y.left
		x.p=y.p
		if(y.p is None):
			self.root=x
		elif(y==y.p.left):
			y.p.left=x
		else:
			y.p.right=x
		x.right=y
		y.p=x
		return

