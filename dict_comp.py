def dict_comp(stop, step):
  stop= int(stop)
  step=int(step)
  plac_holder = []
  dict_set = {}
  dupl_steps = []
  guess_stop = stop // step
  stop2 = step * guess_stop
  # print(stop2)
  i = 1
  j = 1
  while i <= stop2:
      plac_holder.append(i)
      i += 1
  while j <= step:
      dupl_steps.append(j)
      j += 1
  # print(hold_steps)
  data_new = [plac_holder[i:i + step] for i in range(0, len(plac_holder), step)]
  dict_set = {f'items-{dupl_steps[i]}': data_new[i] for i in range(len(data_new))}
  print(dict_set)


dict_comp(stop= input('Enter Number Range: '), step= input('Enter Number: '))
