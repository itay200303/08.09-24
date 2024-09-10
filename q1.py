# start

friends: int = 4
slices_pizza: int = int(input('how many slices of pizza would you like to have? :'))

slices_per_friend = slices_pizza // friends
slices_left = slices_pizza % friends

print('every friend gets:' ,slices_per_friend)
print('slices left:' ,slices_left)

invited_friends: int = int(input('how many friends got invited?:'))
ordered_slices_pizza: int = int(input('how many slices of pizza got ordered? :'))

slices_per_invited_friends  = ordered_slices_pizza // invited_friends
slices_left_that_ordered = ordered_slices_pizza % invited_friends

print('every friend gets:' ,slices_per_invited_friends)
print('slices left:' ,slices_left_that_ordered)
