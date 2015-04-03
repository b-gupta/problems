#/bin/python
import random
import pdb

def str_mat_path(matrix, string):
    cache = {} # (x,y) -> [str1, str2...]
    for col in range(0, len(matrix)):
        for row in range(0, len(matrix[0])):
            if matrix[col][row] == string[0]:
                loc = xy_to_loc(col, row)
                visited = empty_copy(matrix)
                visited[col][row] = 1
                path = find_path(matrix, visited, cache, col, row, string[1:])
                if path:
                    return [loc] + path
    return [] # nothing found

def find_path(matrix, visited, cache, col, row, string):
    dests = get_dests(col, row, visited)
    path = []
    for x, y in dests:
        loc = xy_to_loc(x, y)
        if matrix[x][y] == string[0]: # proceed with this path
            if not string[1:]: # last letter
                return [loc]
            if cache.has_key(loc) and cache[loc].has_key(string[1:]):
                continue
            visited[x][y] = 1
            path = find_path(matrix, visited, cache, x, y, string[1:])
            if not path:
                visited[x][y] = 0
            else: # Found a path! Success!
                return [loc] + path

    loc = xy_to_loc(col, row)
    if cache.has_key(loc):
        cache[loc][string] = 1
    else:
        cache[loc] = {string:1}
    return path

def xy_to_loc(x, y):
    return '(%d, %d)' % (x, y)

def get_dests(x, y, visited):
    if x+1 < len(visited) and not visited[x+1][y]:
        yield (x+1, y)
    if x-1 >= 0 and not visited[x-1][y]:
        yield (x-1, y)
    if y+1 < len(visited[0]) and not visited[x][y+1]:
        yield (x, y+1)
    if y-1 >= 0 and not visited[x][y-1]:
        yield (x, y-1)

def empty_copy(matrix):
    # this is how you copy a 2d matrix in python lol
    return list(list(x * 0 for x in range(len(matrix[0]))) for y in range(len(matrix)))

def vowel():
    vowels = ['a', 'e', 'i', 'o', 'u']
    return vowels[random.randint(0,4)]

def gen_random_mat(n):
    r_matrix = list(list(x * 0 for x in range(n)) for y in range(n))
    for x in range(len(r_matrix)):
        for y in range(len(r_matrix[0])):
            if random.randint(0,4) == 1:
                    r_matrix[x][y] = vowel()
            else:
                r_matrix[x][y] = chr(ord('a') + random.randint(0,25))
    return r_matrix

def out_matrix(matrix, capitalize=[]):
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            loc = xy_to_loc(x,y)
            if loc in capitalize:
                print matrix[x][y].upper(),
            else:
                print matrix[x][y],
        print

def sample_mat():
    word =\
    '''f x u o i b r r b p u a g h y m o w c z
       a c n e a p o u k u b w v t p b s n i i
       d a o i f v u t h d c j u o u b a v p o
       o o r c d o m a p y o j w r g i e r n h
       j b s q r u n b h n k u e b z w y g z z
       e h i u e c f u h o h i o a f y t j f w
       s w i n e t a e v g l b w l u y v f o t
       e i y t l f u l i e o u z h t g s s f i
       t q e a t t q a i r e e l k u g x g h m
       x p h a v s o x m i d m i g e z a j l i
       a e u y b e y a p q g j s d i v o v n m
       i v y u o t j e g a d l j o i j w e e q
       j y w g m i a t u y g u a v i f p j p c
       f x e j h s f a z b e s n r a f u h w v
       x v e k y y p d c k v e g s t d m j s o
       o g e s p l i v e a i o l d h x a q c v
       o i j c i i n e w j e i r s g l o u z k
       w f d i l i i l h i z o d o i v w r r e
       i j h b h o o x d e m l l y e z i f a z
       h e l l o g t o e c o c u z h q o s k g'''

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

    return matrix

def test_str_mat_path():
    matrix = sample_mat()
    words = ['heat', 'map', 'hello', 'world', 'boar', 'height', 'hoot', 'boot', 'boob', 'dicipline']
    for word in words:
        path = str_mat_path(matrix, word)
        if path:
            print 'found word:', word
            out_matrix(matrix, path)
            print
        else:
            print 'could not find word:', word

def main():
    test_str_mat_path()

if __name__ == '__main__':
    main()

