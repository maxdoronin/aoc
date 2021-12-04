 
def sample_str_to_bit_list(sample_str):
    return [int(char) for char in sample_str]

def sample_int_to_bit_list(sample_int, sample_length):
    format_str = '{{0:>0{}b}}'.format(sample_length)
    bits_str = format_str.format(sample_int)
    return (sample_str_to_bit_list(bits_str))

def sample_bit_list_to_int(sample_bit_list):
    sample_str = '0b'
    for sample_bit in sample_bit_list:
        sample_str += str(sample_bit)
    sample_int = int(sample_str, 2)
    return (sample_int)

def samples_str_to_int(samples_str):
    samples_int = []
    for sample_str in samples_str:
        samples_int.append(int(sample_str.strip(), 2))
    return (samples_int)

# returns true if  bit number <bit_no> in the <sample_int> is set to <bc>
# most significant bit number is number 0
def check_bc(sample_int, sample_length, bit_no, bc):
    # create bit mask with bit number bit_no set to 1 
    mask = 1 << sample_length - bit_no - 1
    # find the bit value in the masked position
    masked_bit = (sample_int & mask) >> sample_length - bit_no - 1
    # return true if the masked bit is the same as bc (bit criteria)
    return masked_bit == bc

# returns subset of the orignal <samples_int> list where <bit_no> equals <bc>
def filter_on_bc(samples_int, sample_length, bit_no, bc):
    return ([sample for sample in samples_int if check_bc(sample, sample_length, bit_no, bc)])

# returns list of the most frequent bit values in each sample position for the list of samples <samples_int>. If count(1) = count (0) then use 1   
def get_1_frequency_list(samples_int, sample_length):
    sample_count = 0
    bit_count = [0]*sample_length

    for sample_int in samples_int:
        sample_bit_list = sample_int_to_bit_list(sample_int, sample_length)
        sample_count += 1
        bit_count = [a + b for a, b in zip(bit_count, sample_bit_list)]

    frequency_list = [int(sample_count - bit <= bit) for bit in bit_count]
    return (frequency_list)

def inverse_frequency_list(frequency_list):
    return ([1 - bit for bit in frequency_list])

def day3_1(lines):
    sample_count = 0
    sample_length = len(lines[0].strip())
    bit_count = [0]*sample_length

    for line in lines:
        sample_count += 1
        bit_count = [a + b for a, b in zip(bit_count, sample_str_to_bit_list(line.strip()))]
    
    gamma_str = '0b'
    epsilon_str = '0b'
    for bit in bit_count:
        gamma_bit = int(sample_count - bit < bit)
        gamma_str += str(gamma_bit)
        epsilon_bit = 1 - gamma_bit
        epsilon_str += str(epsilon_bit)
    print (gamma_str)
    print (epsilon_str)
    gamma_rate = int(gamma_str, 2)
    epsilon_rate = int(epsilon_str, 2)
    energy_consumption = gamma_rate*epsilon_rate
    return (gamma_rate, epsilon_rate, energy_consumption)

def day3_1_new(lines):
    sample_length = len(lines[0].strip())
    samples_int = samples_str_to_int(lines)    
    gamma_frequency_list = get_1_frequency_list(samples_int, sample_length)
    epsilon_frequency_list = inverse_frequency_list(gamma_frequency_list)
    gamma_rate = sample_bit_list_to_int(gamma_frequency_list)
    epsilon_rate = sample_bit_list_to_int(epsilon_frequency_list)
    energy_consumption = gamma_rate*epsilon_rate
    return (gamma_rate, epsilon_rate, energy_consumption)

def day3_2(lines):
    sample_length = len(lines[0].strip())
    samples_int = samples_str_to_int(lines)    
    current_bit = 0
    while (len(samples_int) > 1):
        frequency_vector = get_1_frequency_list(samples_int, sample_length)
        samples_int = filter_on_bc(samples_int, sample_length, current_bit, frequency_vector[current_bit])
        current_bit += 1
    r1 = samples_int[0]

    samples_int = samples_str_to_int(lines)
    current_bit = 0
    while (len(samples_int) > 1):
        frequency_vector = inverse_frequency_list(get_1_frequency_list(samples_int, sample_length))
        samples_int = filter_on_bc(samples_int, sample_length, current_bit, frequency_vector[current_bit])
        current_bit += 1
    r2 = samples_int[0]

    return (r1, r2, r1*r2)

with open('../testinput.txt') as f:
    lines = f.readlines()

    print (day3_1(lines))
    print (day3_1_new(lines))
    print (day3_2(lines))

with open('../input.txt') as f:
    lines = f.readlines()

    print (day3_1(lines))
    print (day3_1_new(lines))
    print (day3_2(lines))