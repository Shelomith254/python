def voting_elibility(age):
    if age<18:
        return not "eligible"
    if age>=18:
        return "eligible"
age=int(input("enter your age:")) 
voting=voting_elibility(age) 
print("voting eligibility:",voting)
