##Unviersidad del Valle de Guatmemala
##Inteligencia Artificial
##Autor: Michelle Bloomfield Fong 16803

def graph_search(problem):
  
    frontier = []
    explored = []
    path = []
    estado = problem.initial
    path.append(estado)
    frontier.append(estado)
    
    while True:
        if len(frontier):
            path = problem.heuristica(frontier)
            s = path.end
            explored.append(path)
            
            if problem.goaltest(s):
                return path
            
            for a in problem.actions(s):
                result = problem.results(s,a)
                
                if not is_explored(path, result, explored):
                    new_path = Path([])
                    naw_path.extendFrom(path)
                    new_path.addStep(problem.result(s,a))
                    frontier.append(new_path)
        else:
            return False