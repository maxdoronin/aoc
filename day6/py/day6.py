max_timer = 8
timer_reset_value = 6

def read_input(file_name):
    with open(file_name) as f:
        lines = f.readlines()
        raw_population = []
        for line in lines:
            raw_population = [int(fish) for fish in line.split(',')]
        return(raw_population)

def aggregate_raw_population(raw_population):
    population = [0]*(max_timer+1)
    for i in range(len(population)):
        population[i] = sum([fish==i for fish in raw_population])
    return(population)

def process_day(population):
    new_population = [0]*(max_timer+1)
    popping_today = population[0]
    for i in range (max_timer):
        new_population[i] = population[i+1]
    new_population[max_timer] = popping_today
    new_population[timer_reset_value] += popping_today
    return(new_population)

def process_epoch(population, epoch_length):
    for i in range(epoch_length):
        population = process_day(population)
    return(sum(population))

print('Part 1')
raw_population = read_input('testinput.txt')
population = aggregate_raw_population(raw_population)
print(process_epoch(population, 80))
raw_population = read_input('input.txt')
population = aggregate_raw_population(raw_population)
print(process_epoch(population, 80))

print('Part 2')
raw_population = read_input('testinput.txt')
population = aggregate_raw_population(raw_population)
print(process_epoch(population, 256))
raw_population = read_input('input.txt')
population = aggregate_raw_population(raw_population)
print(process_epoch(population, 256))