from graph import GRAPH


get_edge_weight = lambda g, n1, n2: g.get_edge_data(n1, n2).get("weight")


def dijkstra_sort_nodes(graph, current, excludes=[]):
  avaliables = [n for n in list(graph.neighbors(current)) if n not in excludes]

  for i in range(len(avaliables)):
    i_weight = get_edge_weight(graph, current, avaliables[i])
    for j in range(len(avaliables)):
      if i_weight < get_edge_weight(graph, current, avaliables[j]):
        temp = avaliables[i]
        avaliables[i] = avaliables[j]
        avaliables[j] = temp

  return avaliables


def dijkstra_get_path(graph, current, end, queue=[], paths=[{}]):
  if paths == [{}]:
    return dijkstra_get_path(graph, current, end, [current], [{'path':[current], 'adder':0}])
  
  if current == end:
    paths[-1]['adder'] += get_edge_weight(graph, paths[-1]['path'][-1], current)
    paths[-1]['path'].append(current)
    paths = [p for p in paths if p['path'][-1] == end]

    for i in range(len(paths)):
      for j in range(len(paths)):
        if paths[i]['adder'] < paths[j]['adder']:
          temp = paths[i]
          paths[i] = paths[j]
          paths[j] = temp

    return paths[0]

  for n in dijkstra_sort_nodes(graph, current, queue):
    queue.append(n)
    for p, a in [i.items() for i in paths]:
      if p[1][-1] == current:
        paths.append({
          'path': [*p[1], n],
          'adder': a[1] + get_edge_weight(graph, p[1][-1], n)
        })

  return dijkstra_get_path(graph, *queue[:1], end, queue[1:], paths)


print('\nAll hail Lord Dijkstra!')
print(dijkstra_get_path(GRAPH, 3, 21))