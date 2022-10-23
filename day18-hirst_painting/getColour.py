import colorgram;

colours = colorgram.extract("image.jpg", 30);

rgb_colours = [];

for colour in colours:
    r = colour.rgb.r;
    g = colour.rgb.g ;
    b = colour.rgb.b;
    
    new_colour = (r, g, b);
    rgb_colours.append(new_colour);
    
del rgb_colours[0:4];
print(rgb_colours);