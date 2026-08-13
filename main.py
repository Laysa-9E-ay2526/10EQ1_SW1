from pyscript import document

# String data type
name = "Dejan"

# Integer data type
age = 14

# Integer data type
height162 = 162

# List data type
countries_visited = ["Japan", "Korea", "US"]

# Boolean data type
student_type = True

# Dictionary data type
personal_info = {
    "color": "Blue",
    "car_brand": "BYD",
    "shoe_size": 8,
    
}

# Set data type
favorite_fruits = {
    "Mango",
    "Apple",
    "Oranges",
    "Grapes",
    "Banana"
}

# Tuple data type
days = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
)

output = document.getElementById("output")

output.innerHTML = f"""
<div class="info">
<h2>My Information</h2>
Name: {name}<br>
Age: {age}<br>
Height: {height162} cm
</div>

<div class="info">
<h2>Countries I Want to Visit</h2>
{countries_visited}
</div>

<div class="info">
<h2>Student Type</h2>
New Student: {student_type}
</div>

<div class="info">
<h2>Personal Information</h2>
Color: {personal_info["color"]}<br>
Car Brand: {personal_info["car_brand"]}<br>
Shoe Size: {personal_info["shoe_size"]}<br>
</div>

<div class="info">
<h2>Favorite Fruits</h2>
{favorite_fruits}
</div>

<div class="info">
<h2>Days of the Week</h2>
{days}
</div>
"""