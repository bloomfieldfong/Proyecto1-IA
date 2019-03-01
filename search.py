##Unviersidad del Valle de Guatmemala
##Inteligencia Artificial
##Autor: Michelle Bloomfield Fong 16803



def graph_search(problem):
  
    frontier = []
    explored = []
    
    path = []
    estado = problem.initial
    path.append(estado)
    frontier.append(path)
    
    while True:
        
        ##Nos indica que camino tomar 
        if len(frontier):
            path = problem.criteria(frontier)
            s = path[len(path)-1]
            explored.append(s)
            ##Si gano nos retorna la ruta tomada   
            if problem.goaltest(s):
                return path
            
            for a in problem.actions(s):
                result = problem.results(s,a)
              
            if result not in explored:
                
                
            
        else:
            return False