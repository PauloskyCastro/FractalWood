import fractal
import random
import numpy as np
from PIL import Image

def generate_fractal_wood():
    # Create a fractal object with random parameters
    f = fractal.Fractal(random.randint(3, 6), random.uniform(0.1, 0.9), random.uniform(0.1, 0.9))
    # Generate the fractal shape
    wood = f.generate()
    # Convert the fractal shape to an image
    img = Image.fromarray(np.uint8(wood * 255))
    # Return the fractal image
    return img

# Generate 10 fractal wood images
for i in range(10):
    wood = generate_fractal_wood()
    wood.save("fractal_wood_{}.png".format(i))
