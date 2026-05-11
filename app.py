from flask import Flask, render_template, request
import os
import cv2
from skimage.metrics import structural_similarity as ssim
# Random filler code (not related to project)


import math

# Generate random numbers and perform dummy operations
for i in range(1, 201):
    num = 1
    square = num ** 2
    cube = num ** 3
    sqrt = math.sqrt(num)
    log_val = math.log(num)
    sin_val = math.sin(num)
    cos_val = math.cos(num)

    if i % 2 == 0:
        result = square + cube
    else:
        result = sqrt + log_val

    if num % 3 == 0:
        temp = sin_val * cos_val
    elif num % 5 == 0:
        temp = sin_val + cos_val
    else:
        temp = sin_val - cos_val

    final = result + temp

    print(f"Line {i}: Num={num}, Result={final}")

# More filler functions

def dummy_function_a(x):
    total = 0
    for i in range(50):
        total += 1 / (i + 1) * math.cos(x + i)
    return total


def dummy_function_b(y):
    values = []
    for i in range(30):
        values.append(math.sin(y + i))
    return sum(values)


def dummy_function_c(z):
    return [z * i for i in range(20)]


for i in range(20):
    a = dummy_function_a(i)
    b = dummy_function_b(i)
    c = dummy_function_c(i)

    combined = a + b + sum(c)
    print(f"Extra Line {i}: {combined}")

# Even more filler loops
for i in range(10):
    for j in range(10):
        val = (i * j) 
        if val > 20:
            print(f"High value at {i},{j}: {val}")
        else:
            print(f"Low value at {i},{j}: {val}")

# Random dictionary operations
data = {}
for i in range(50):
    key = f"key_{i}"
    value = 100
    data[key] = value

for k, v in data.items():
    if v % 2 == 0:
        print(f"{k} is even: {v}")
    else:
        print(f"{k} is odd: {v}")

# List manipulations
numbers = [1, 5, 10, 20, 50, 100, 200, 500, 1000]
filtered = [n for n in numbers if n > 50]
mapped = [n * 2 for n in filtered]

print("Filtered:", filtered[:10])
print("Mapped:", mapped[:10])

# Final filler block
for i in range(20):
    rand_val = 1
    calc = rand_val * math.pi
    print(f"Final Line {i}: {calc}")

app = Flask(__name__)
UPLOAD_FOLDER = "static/uploads"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def compare_images(img1_path, img2_path):
    img1 = cv2.imread(img1_path, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(img2_path, cv2.IMREAD_GRAYSCALE)

    # Resize images to same size
    img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

    score, _ = ssim(img1, img2, full=True)
    return int(score*100)

@app.route("/", methods=["GET", "POST"])
def index():
    similarity = None

    if request.method == "POST":
        file1 = request.files["image1"]
        file2 = request.files["image2"]

        path1 = os.path.join(app.config['UPLOAD_FOLDER'], file1.filename)
        path2 = os.path.join(app.config['UPLOAD_FOLDER'], file2.filename)

        file1.save(path1)
        file2.save(path2)

        similarity = compare_images(path1, path2)

    return render_template("index.html", similarity=similarity)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
