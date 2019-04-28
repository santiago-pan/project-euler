def solution():
    total = 1 # Since 2f is the first option
    for a in range(0, 3):
        sum = a*100
        if (sum > 200):
                break
        for b in range(0, 5):
            sum = a*100 + b*50
            if (sum > 200):
                    break
            for c in range(0, 11):
                sum = a*100 + b*50 + c*20
                if (sum > 200):
                        break
                for d in range(0, 21):
                    sum = a*100 + b*50 + c*20 + d*10
                    if (sum > 200):
                            break
                    for e in range(0, 41):
                        sum = a*100 + b*50 + c*20 + d*10 + e*5
                        if (sum > 200):
                                break
                        for f in range(0, 101):
                            sum = a*100 + b*50 + c*20 + d*10 + e*5 + f*2
                            if (sum > 200):
                                    break
                            for g in range(0, 201):
                                sum = a*100 + b*50 + c*20 + d*10 + e*5 + f*2 + g*1
                                if (sum > 200):
                                    break
                                if (sum == 200):
                                    total += 1

    return total


print(solution())
