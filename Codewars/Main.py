def human_years_cat_years_dog_years(human_years):
    # Your code here
    human_years = 0
    cat_years = 0
    dog_years = 0
    if human_years >=1:
        return [human_years, cat_years+15, dog_years+15]
    elif human_years>=2: 
        return [human_years, cat_years+15+9, dog_years+15+9]
    else:
        [(human_years), cat_years+15+9*4, dog_years+15+9*5]
                    
        
print(human_years_cat_years_dog_years(10))        
        
        