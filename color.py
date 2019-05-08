colors = ['1', '2', '3', 'Yellow', 'Black']

states = ['0', '1', '2', '3']

neighbors = {}
neighbors['0'] = ['1', '2']
neighbors['1'] = ['0', '2', '3']
neighbors['2'] = ['0', '1', '3']
neighbors['3'] = ['1', '2']

colors_of_states = {}

def promising(state, color):
    for neighbor in neighbors.get(state): 
        color_of_neighbor = colors_of_states.get(neighbor)
        if color_of_neighbor == color:
            return False

    return True

def get_color_for_state(state):
    for color in colors:
        if promising(state, color):
            return color

def main():
    for state in states:
        colors_of_states[state] = get_color_for_state(state)

    print (colors_of_states)


main()
