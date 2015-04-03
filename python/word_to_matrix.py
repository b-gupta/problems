word =\
'''f x u o i b r r b p u a g h y m o w c z
   a c n e a p o u k u b w v t p b s n i i
   d a o i f v u t h d c j u o u b a v p o
   o o r c d o u u i y o j w r g i e r n h
   j b s q r u n b h n k u e b z w y g z z
   e h i u e c f u h o h i o a f y t j f w
   s w i n e t a e v g l b w l u y v f o t
   e i y t l f u l i e o u z h t g s s f i
   t q e b f t q a i r e e l k u g x g h m
   x p p a v s o x m i d m i g e z a j l i
   a e u y b e y a p q g j s d i v o v n m
   i v y u o t j e g a d l j o i j w e e q
   j y w g m i a t u y g u a v i f p j p c
   f x e j h s f a z b e s n r a f u h w v
   x v e k y y p d c k v e g s h d m j s o
   o g e s p l i v e a i o l d i x a q c v
   o i j c i i n e w j e i r s i l o u z k
   w f d i l i i l h i z o d o o v w r r e
   i j h b h o o x d e m l l y w z i f a z
   h e l l o g t o e c o c u z d q o s k g'''

 # convert this into a matrix
n = 20
matrix = list(list(x * 0 for x in range(n)) for y in range(n))

word = word.replace(' ', '').replace('\n', '').strip()

x,y = 0, 0
for i in range(len(word)):
    matrix[x][y] = word[i]
    y += 1
    if y == n:
        y = 0
        x += 1

def out_matrix(matrix):
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            print matrix[x][y],
        print
print word
print
out_matrix(matrix)
