!pip install cadquery
from  cadquery import func as cf

# Step 1: Create a rectangular plate
plate = cf.box(80, 50, 10)

# Step 2: Create a cylindrical hole
hole = cf.cylinder(d=20, h=10)

# Step 3: Move the hole 20 mm to the right
hole = hole.moved(x=20)

# Step 4: Subtract the hole from the plate
part = plate - hole

# Step 5: Check validity and calculate volume
print(part.isValid(), round(part.Volume(), 1))

# Step 6: Export the model as an STL file
part.exportStl("plate.stl")

from google.colab import files 
files.download("plate.stl")
