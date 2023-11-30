if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    def divide(a, b):
        divide = a / b
        return divide
    
    def rest(a, b):
        rest = a // b
        return rest
        
    print(rest(a, b))
    print(divide(a, b))
