def nfsmaccepts(current, edges, accepting, visited):
	#basecase
	if current in visited:
		return None
	elif current in accepting:
		return ""
	else:
		newvisited = visited + [current]
		for edge in edges:
			if edge[0] == current:
				for newstate in edges[edge]:
					foo = nfsmaccepts(newstate,edges, accepting, newvisited)
					if foo != None:
						return edge[1] + foo
		return None