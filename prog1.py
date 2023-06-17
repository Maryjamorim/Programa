def lin():
    print("-=" * 10)
    
lin()
num = int(input("Digite um número: "))
lin()
print("Tabuada de ", num)
lin()

def op_aritmeticas():
    sinal = input("Qual operação matemática você deseja? ")
    lin()
    if(sinal == "+"):
        print("A tabuada escolhida foi soma!")
        for i in range(1, 11):
            tab_s = num + i 
            print(num, "+", i, "=", tab_s)
    elif(sinal == "-"):
        print("A tabuada escolhida foi subtração!")
        for i in range(1, 11):
            tab_sub = num + i
            print(num, "-", i, "=", tab_sub)
    elif(sinal == "*"):
        print("A tabuada escolhida foi multiplicação!")
        for i in range(1, 11):
            tab_m = num * i
            print(num, "*", i, "=", tab_m)
    elif(sinal == "/" ):
        print("A tabuada escolhida foi divisão!")
        for i in range(1, 11):
            tab_d = num / i
            print(num, "/", i, "=", tab_d)
            
op_aritmeticas()
        
        
        
    



lin()