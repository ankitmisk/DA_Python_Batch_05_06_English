
# 1
def summ(koi_data):
    '''This will sumup all the values of given data'''
    result = 0
    for i in koi_data:
        result += i
        
    return result



# 2
def check_prime(number):
    for i in range(2,number):
        if number % i ==0:
            print(f'{number} Not a Prime Number!!')
            break
    else:
        print(f'{number} a Prime number!!')
    
    
# 3    
# fibonacci series
def give_fibonacci(kitne):
    fibo = [0,1]
    
    for i in range(kitne-2):
        agla_num = fibo[-1]  + fibo[-2]
        
        fibo.append(agla_num)
        
    return fibo

# 4
def area_of_traingle(length, breadth):
    return 0.5*length*breadth



# 5
def give_table(number):
    for i in range(1,11):
        print(f'{number} x {i} = {number*i}')
        
# 6        
def give_perimeter_of(shape = None):
    if shape == None:
        print('No perimeter!!, shape not decided!!')
        
    elif shape == 'rectangle':
        l = float(input('Enter length: '))
        b = float(input('Enter breadth: '))
        
        peri = 2*(l+b)
        
        print(f'Perimeter of rectange is: {peri}')
        
    elif shape == 'square':
        side = float(input('Enter side: '))
        
        peri = 4*side
        print(f'Perimeter of Square is: {peri}')
        
    elif shape == 'triangle':
        s1 = float(input('Enter side 1: '))
        s2 = float(input('Enter side 2: '))
        s3 = float(input('Enter side 3: '))
        
        peri = s1+s2+s3
        print(f'Perimeter of Triangle is: {peri}')
        
    elif shape == 'circle':
        r = float(input('Enter radius: '))
        
        pi = 3.14
        
        peri = 2*pi*r
        print(f'Perimeter of Circle is: {peri}')
        
    else:
        print('Not sure about shape!!')
        
        
        
#7        
def check_anagram(word1,word2):
    word1_list = list(word1.lower().replace(' ',''))
    word2_list = list(word2.lower().replace(' ','')) 
    
    word1_list.sort()
    word2_list.sort()
    
    
    if word1_list == word2_list:
        return 'Anagram words'
    
    else:
        return 'Not an Anagram words'
    
    
    
#8    
def check_armstrong(number):
    power = len(str(number))
    result = 0
    
    
    for i in str(number):
        result += int(i)**power
        
    if result == number:
        return 'Armstrong Number!!'
    else:
        return 'Not an Armstrong Number!!'