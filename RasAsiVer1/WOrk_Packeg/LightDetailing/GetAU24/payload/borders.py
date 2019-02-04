def bordersForm(R, G, B, stule=None):
    if stule == None: stule = 'SOLID_MEDIUM'
    boardersPayload = {
        'bottom': {
            'style': stule,
            'color': {
                'red': R,
                'green': G,
                'blue': B
            }
        },
        'left': {
            'style': stule,
            'color': {
                'red': R,
                'green': G,
                'blue': B
            }
        },
        'right': {
            'style': stule,
            'color': {
                'red': R,
                'green': G,
                'blue': B
            }
        },
        'top': {
            'style': stule,
            'color': {
                'red': R,
                'green': G,
                'blue': B
            }
        },
    }
    return boardersPayload
