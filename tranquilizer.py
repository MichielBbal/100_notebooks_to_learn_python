from tranquilizer import tranquilize

@tranquilize()
def order(cheese):
    '''I'd like to buy some cheese!'''
    return "I'm afraid we're fresh out of {}, Sir.".format(cheese)