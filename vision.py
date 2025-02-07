from google.cloud import vision
import io

client = vision.ImageAnnotatorClient.from_service_account_file('/Users/richardli/devfest25-f6e7385953bd.json')

image_path = "sailboat.jpg"

with io.open(image_path, 'rb') as image_file:
    content = image_file.read()

image = vision.Image(content=content)

response = client.label_detection(image=image)

labels = response.label_annotations

print("Labels: ")
for label in labels:
    print(label.description, label.score)

################
image_path = "pic_with_text.png"

with io.open(image_path, 'rb') as image_file:
    content = image_file.read()

image = vision.Image(content=content)

response = client.text_detection(image=image)

texts = response.text_annotations

print(texts[0].description)