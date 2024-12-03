from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
import cv2
import base64
import numpy as np


def home(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('profile')
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            # If form is invalid, render the form with errors
            return render(request, 'register.html', {'form': form})
    else:
        form = UserCreationForm()
    return render(request, 'index.html', {'form': form})

@login_required
@csrf_protect
# Profile view with blood group determination
def profile(request):
    if request.method == 'POST' and request.FILES.get('abo'):
        blood_image = request.FILES['abo'].read()

        np_arr = np.frombuffer(blood_image, np.uint8)
        img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

        # Preprocessing the image
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        enhance_img = cv2.equalizeHist(blur)
        _, bin_img = cv2.threshold(enhance_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        # Morphological operations
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
        bin_img = cv2.morphologyEx(bin_img, cv2.MORPH_OPEN, kernel)
        bin_img = cv2.morphologyEx(bin_img, cv2.MORPH_CLOSE, kernel)

        # Split into regions for A, B, and D
        height, width = bin_img.shape
        region_height = height // 3
        region_A = bin_img[:region_height, :]
        region_B = bin_img[region_height:2 * region_height, :]
        region_D = bin_img[2 * region_height:, :]

        def calculate_agglutination(region):
            num_labels, _, _, _ = cv2.connectedComponentsWithStats(region, connectivity=8)
            return num_labels - 1

        # Calculate agglutination in regions A, B, and D
        num_A = calculate_agglutination(region_A)
        num_B = calculate_agglutination(region_B)
        num_D = calculate_agglutination(region_D)

        # Determine blood group
        blood_group = "Unknown"
        if num_A > 0 and num_B == 0:
            blood_group = "A"
        elif num_A == 0 and num_B > 0:
            blood_group = "B"
        elif num_A > 0 and num_B > 0:
            blood_group = "AB"
        elif num_A == 0 and num_B == 0:
            blood_group = "O"

        if num_D > 0:
            blood_group += " Positive"
        else:
            blood_group += " Negative"

        # Encode original image and processed (morphological) image to Base64 for display
        _, buffer = cv2.imencode('.jpg', img)
        original_img_base64 = base64.b64encode(buffer).decode('utf-8')
        original_img_url = f"data:image/jpeg;base64,{original_img_base64}"

        _, buffer = cv2.imencode('.jpg', bin_img)
        mor_img_base64 = base64.b64encode(buffer).decode('utf-8')
        mor_img_url = f"data:image/jpeg;base64,{mor_img_base64}"

        # Render the result in the profile page
        return render(request, 'result.html', {
            'img': original_img_url,
            'mor_img': mor_img_url,
            'obj': blood_group
        })

    return render(request, 'profile.html')


# Add placeholder views for other pages
def portfolio(request):
    return render(request, 'portfolio.html')

def courses(request):
    return render(request, 'courses.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def result(request):
    # If there's no data to display, redirect back to profile
    if not request.method == 'POST':
        return redirect('profile')
    return render(request, 'result.html')