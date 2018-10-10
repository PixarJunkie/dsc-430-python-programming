#Last letter count function 
def last_letter_count():
    boy_dict = {}
    girl_dict = {}
    with open('namesBoys.txt') as f_1, open('namesGirls.txt') as f_2: 
        #for x, y in intertool.izip(f_1, f_2):
        boys = [x.strip() for x in f_1]
        girls = [y.strip() for y in f_2]
        for boy in boys:
            last_boy = list(boy)[-1]
        if last_boy in boy_dict:
            boy_dict[last_boy] += 1
        else: 
            boy_dict[last_boy] = 1
        for girl in girls:
            last_girl = list(girl)[-1]
        if last_girl in girl_dict: 
            girl_dict[last_girl] += 1
        else:
            girl_dict[last_girl] = 1
        
        print(boy_dict)
        print(girl_dict)
        return boy_dict, girl_dict
    
last_letter_count()