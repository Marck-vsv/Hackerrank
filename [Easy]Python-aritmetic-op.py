if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    def summ(a, b):
        summ = a + b
        return summ
    
    def subt(a, b):
        subt = a - b
        return subt
        
    def product(a, b):
        product = a * b
        return product
        
    print(summ(a, b))
    print(subt(a, b))
    print(product(a, b))
