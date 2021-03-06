"""
Created: Thu Jul 25 12:29:27 2019
@author: Christopher Albert <albert@alumni.tugraz.at>
"""

# %% Import, compile and load
from numpy import array, linspace
from fffi import FortranLibrary, FortranModule

libfortmod = FortranLibrary('fortmod')
fortmod = FortranModule(libfortmod, 'fortmod')

# member variable and subroutine definition stub
# TODO: parse fortmod.f90 automatically and strip away implementation
with open('fortmod.f90', 'r') as f:
    code = f.read()
fortmod.fdef(code)

libfortmod.compile()  # only required when Fortran library has changed
fortmod.load()

# %% Try some stuff
print('Before init(): member = {}'.format(fortmod.member))
fortmod.init()
print('After init(): member = {}'.format(fortmod.member))

a = fortmod.member_array  # this is a mutable reference
print('Before side_effects(): member_array = {}'.format(a))
fortmod.side_effects()
print('After side_effects(): member_array = {}'.format(a))

z = linspace(1, 10, 4)
print('Before modify_vector(z, 4): z = {}'.format(z))
fortmod.modify_vector(z, 4)
print('After modify_vector(z, 4): z = {}'.format(z))

A = array([[1, 2], [3, 4]], order='F')
print('Before modify_matrix(A, 1): z = {}'.format(A))
fortmod.modify_matrix(A, 1.0)
print('After modify_matrix(A, 1): z = {}'.format(A))

print('Before allocating array')
fortmod.alloc_member()
print('After allocating array')

print('Before accessing array')
print(fortmod.alloc_array)
print('After accessing array')
