pets = {
    'Cat': 'Meow',
    'Dog': 'Bark',
    'Bird': 'Tweet'
}

print(pets['Dog'])

print(pets.get('Lizard'))

print(pets.get('Lizard', '<silence>'))

cats = {
    'Pete': {
        'Cheddar': {
            'color': 'orange',
            'enjoys': {
                'sleeping',
                'snuggling',
                'meowing',
                'eating',
                'birdwatching',
            },
        },
        'Cocoa': {
            'color': 'black',
            'enjoys': {
                'eating',
                'sleeping',
                'playing',
                'chewing',
            },
        },
    },
}

print(cats['Pete']['Cocoa']['enjoys'])