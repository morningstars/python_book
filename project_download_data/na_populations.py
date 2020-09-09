import pygal_maps_world.maps

wm = pygal_maps_world.maps.World()
wm.title = 'North Central and South America'
wm.add('North America', {'ca': 4129000, 'us': 34129000, 'mx': 34129000})


wm.render_to_file('na_populations.svg')
