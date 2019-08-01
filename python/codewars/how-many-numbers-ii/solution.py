# https://www.codewars.com/kata/how-many-numbers-ii/train/python

def max_sumDig(nMax, maxSum):
    
    answers = []

    for i in range(1000, nMax + 1):
        digit_values = map( int, (list(str(i))) )
        
        for start in range(len(digit_values) - 3):
            end = start + 4
            digit_sum = sum(digit_values[start:end])
            if digit_sum > maxSum:
                break
            if start == len(digit_values) - 4:
                answers.append(i)

    
    try:
        average = round(sum(answers)/len(answers))
    except:
        average = 0
        
    average += 0.0000000001
    smallest_distance_from_average = min( [ (abs(answers[i] - average), i) for i in range(len(answers))] )[1]
    closest_answer_to_average = answers[smallest_distance_from_average]
    
    return [len(answers), closest_answer_to_average, sum(answers)]