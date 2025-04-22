import cv2
import numpy as np

def _get_sky_region(image, fraction=0.3):
    height = image.shape[0]
    return image[:int(height * fraction), :]

def _get_brightness(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    return np.mean(hsv[:, :, 2]) / 255.0

def _get_saturation(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    return np.mean(hsv[:, :, 1]) / 255.0

def _get_contrast(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray.std() / 255.0

def _get_edge_density(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)
    return np.sum(edges > 0) / edges.size

def _is_forest(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hue = hsv[:, :, 0]
    green_mask = (hue > 35) & (hue < 85)
    green_ratio = np.sum(green_mask) / (image.shape[0] * image.shape[1])
    return green_ratio > 0.25

def classify_weather(img: str):
    """
    Classify the weather based on brightness, saturation, contrast, and edge density.

    Args:
        img (str): The path to the image file.

    Returns:
        dict: The detected weather condition.
    """

    image = cv2.imread(img)
    sky = _get_sky_region(image)
    brightness = _get_brightness(sky)
    saturation = _get_saturation(sky)
    contrast = _get_contrast(sky)
    edge_density = _get_edge_density(image)
    forest = _is_forest(image)

    # Adjust thresholds based on scene type
    sun_brightness = 0.6 if not forest else 0.45
    sun_saturation = 0.3 if not forest else 0.5
    sun_contrast = 0.1 if not forest else 0.08
    rain_edge_density = 0.08 if not forest else 0.15

    # Weather classification
    if brightness < 0.2:
        weather, weather_id = "Dark (Lowlight)", 0
    elif contrast < 0.07 and brightness > 0.3:
        weather, weather_id = "Foggy", 1
    elif edge_density > rain_edge_density and brightness < 0.5:
        weather, weather_id = "Rainy", 2
    elif brightness > sun_brightness and saturation > sun_saturation and contrast > sun_contrast:
        weather, weather_id = "Sunny", 3
    else:
        weather, weather_id = "Cloudy", 4

    return {
        "weather": weather,
        "weather_id": weather_id,
        "is_forest": forest,
        "brightness": brightness,
        "saturation": saturation,
        "contrast": contrast,
        "edge_density": edge_density
    }