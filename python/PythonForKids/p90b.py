def moon_weight (start_weight, weight_increase,years):
    weight = start_weight + weight_increase * years
    print('Your weight after %s years : %s' % (years,weight))
    
moon_weight(107, 0.25,10)
