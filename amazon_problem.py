# Write a function to generate all combinations of well performed parenthesis

num = int(input("Enter the number of parenthesis you want to print out : "))

def generate_paranthesis(n):
    result = []
    def set_paranthesis(string, paranthesis_l, paranthesis_r):

        if len(string) == 2 * n:
            result.append(string)
        
        if paranthesis_l < n :
            set_paranthesis( string + "(" , paranthesis_l + 1 , paranthesis_r)
        
        if paranthesis_r < paranthesis_l :
            set_paranthesis( string + ")" , paranthesis_l , paranthesis_r + 1)
        
    set_paranthesis("" , 0 , 0)
    return result 

generated_paranthesis = generate_paranthesis(num)

print(generated_paranthesis)
