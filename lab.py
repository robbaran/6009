def step(gas):
  # Put your solution here.  Good luck!  
  #gas is a dict 
  width = gas['width']
  height = gas['height']
  state = gas['state']
  rev_dict = {'l':'r','r':'l','u':'d','d':'u','w':'w'}
  state2 = [[] for i in range(0,len(state))]
  ud_pair = ['u','d']
  lr_pair = ['l','r']
  ud_set = set(ud_pair)
  lr_set = set(lr_pair)
  #1. resolve any collisions w walls
  for idx, cell in enumerate(state):
    if 'w' in cell:
      cell[:] = [rev_dict[i] for i in cell]	#mutates entire cell into wall-resolved version
    #2. resolve any collisions among particles
    # only if exactly two colliding particles		
    part_set = set([x for x in cell if x != 'w'])
    if ud_set == part_set:
      cell.remove('u')
      cell.remove('d')
      cell.extend(lr_pair)
    if lr_set == part_set:
      print('b4',cell)
      cell.remove('l')
      cell.remove('r')
      cell.extend(ud_pair)
      print(cell)
    #3. Propagate particles along their new direction of motion  
    for part in cell:
        #add particle to new_state in correct position, moving same direction
      if part =='w':
        state2[idx].append('w')
      elif part == 'l':
        state2[idx-1].append('l')
      elif part == 'r':
        state2[idx+1].append('r')
      elif part == 'u':
        state2[idx-width].append('u')
      elif part == 'd':
        state2[idx+width].append('d')
  gas['state'][:] = state2
  return gas

