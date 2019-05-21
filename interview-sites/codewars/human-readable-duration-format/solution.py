# https://www.codewars.com/kata/human-readable-duration-format/train/python

def format_duration(seconds):
    # Years
    years, seconds = divmod( seconds, 31536000 )
    
    # Days
    days, seconds = divmod( seconds, 86400 )
    
    # Hours
    hours, seconds = divmod( seconds, 3600 )
    
    # Minutes
    minutes, seconds = divmod( seconds, 60 )
    
    result = []
    
    # Formatting
    for i in [i for i in (years, " year"), (days, " day"), (hours, " hour"), (minutes, " minute"), (seconds, " second") if i[0] > 0]:
        if len(result) != 0:
            result.append(", ")
            
        result.append(str(i[0]))
        result.append(i[1]) if i[0] == 1 else result.append(i[1] + "s")
     
    if len(result) == 0:
        return "now"
    
    result = ''.join(result)
    result = result[::-1].replace(",", "dna ", 1)
    
    return result[::-1]
