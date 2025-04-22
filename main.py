from weathercv import classify_weather

if __name__ == "__main__":
    print(f"dark.jpg Detected Weather: {classify_weather('weathers/dark.jpg')}\n")
    print(f"foggy.jpg Detected Weather: {classify_weather('weathers/foggy.jpg')}\n")
    print(f"rainy.jpg Detected Weather: {classify_weather('weathers/rainy.jpg')}\n")
    print(f"sunny.jpg Detected Weather: {classify_weather('weathers/sunny.jpg')}\n")
    print(f"cloudy.jpg Detected Weather: {classify_weather('weathers/cloudy.jpg')}\n")
    print(f"forest.jpg Detected Weather: {classify_weather('weathers/forest.jpg')}\n")
    print(f"rainy_forest.jpg Detected Weather: {classify_weather('weathers/rainy_forest.jpg')}\n")
    print(f"cloudy_forest.jpg Detected Weather: {classify_weather('weathers/cloudy_forest.jpg')}\n")
    print(f"foggy_forest.jpg Detected Weather: {classify_weather('weathers/foggy_forest.jpg')}\n")
