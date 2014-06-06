
#!/usr/bin/env python

infile = open("olympic.in", "r") 

_ = (infile.readline().strip())
participants = {}
record = [0, 0, 0]
win_country = ""
top_three =[] 

def fill_dict(infile, participants):
    for winners in infile:
        first, second, third = winners.strip().split()
        
        for participant, index in zip((first, second, third), (0, 1, 2)):
            
            if participant not in participants:
            
                participants[participant] = [0, 0, 0]
            
            participants[participant][index] += 1
            ##print participants
            
    top_three = sorted(list(participants.keys()))
    
    return top_three

def find_winner (top_three, win_country, record):

    for score in top_three:
    
        if participants[score] > record:
    
            record = participants[score]
    
            win_country = score
    
    return win_country


top_three = fill_dict (infile, participants)
win_country = find_winner(top_three, win_country,record)

outfile = open("olympic.out", "w")
outfile.write(win_country + "\n")
outfile.close()