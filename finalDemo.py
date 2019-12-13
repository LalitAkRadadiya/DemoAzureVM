from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
import json
import os
files = []

prediction_key = "da9a862e889848f995acfaf0745bba0b"
ENDPOINT = "https://southcentralus.api.cognitive.microsoft.com/"
Project_id = "98196bb6-2a1b-4699-ac46-44a71fa0ae12"
publish_iteration_name = "Adit123"
base_image_url = "/home/lalit/Desktop/Demo/test/images.jpeg"
# Now there is a trained endpoint that can be used to make a prediction
predictor = CustomVisionPredictionClient(prediction_key, endpoint=ENDPOINT)

with open(base_image_url, "rb") as image_contents:
    results = predictor.classify_image(
        Project_id, publish_iteration_name, image_contents.read())

# Display the results.
    for prediction in results.predictions:
        print("\t" + prediction.tag_name)
        break
