from train.models import Train


def dfs_path(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        if vertex in graph.keys():
            for next_ in graph[vertex] - set(path):
                if next_ == goal:
                    yield path + [next_]
                else:
                    stack.append((next_, path + [next_]))


def get_graph(qs):
    graph = {}
    for q in qs:
        graph.setdefault(q.from_city_id, set())
        graph[q.from_city_id].add(q.to_city_id)
    return graph


def get_routs(request, form) -> dict:
    context = {'form': form}
    qs = Train.objects.all()
    graph = get_graph(qs)
    data = form.cleaned_data
    from_city = data['from_city']
    to_city = data['to_city']
    cities = data['cities']
    traveling_time = data['travel_time']
    all_ways = list(dfs_path(graph, from_city.id, to_city.id))
    if not len(all_ways):
        raise ValueError("Routs didn't exist as you try to find")
    if cities:
        _cities = [city.id for city in cities]
        right_ways = []
        for rout in all_ways:
            if all(city in rout for city in _cities):
                right_ways.append(rout)
        if not right_ways:
            raise ValueError("Routs throught this contry none")
    else:
        right_ways = all_ways
    routs = []
    all_trains = {}
    for q in qs:
        all_trains.setdefault((q.from_city_id, q.to_city_id), [])
        all_trains[(q.from_city_id, q.to_city_id)].append(q)
    for route in right_ways:
        tmp = {}
        tmp['trains'] = []
        total_time = 0
        for i in range(len(route)-1):
            qs = all_trains[(route[i], route[i+1])]
            q = qs[0]
            total_time += q.travel_time
            tmp['trains'].append(q)
        tmp['total_time'] = total_time
        if total_time <= traveling_time:
            routs.append(tmp)
    if not routs:
        raise ValueError('Time is bigger')
    sorted_routs = []
    if len(routs) == 1:
        sorted_routs = routs
    else:
        times = list(set(r['total_time'] for r in routs))
        times = sorted(times)
        for time in times:
            for rout in routs:
                if time == rout['total_time']:
                    sorted_routs.append(rout)
    context['routs'] = sorted_routs
    context['cites'] = {'from_city': from_city.name, 'to_city': to_city.name}
    return context
