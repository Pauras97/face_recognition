import face_recognition
from PIL import Image, ImageDraw

image_of_mark = face_recognition.load_image_file('./img/known/Mark Zuckerberg.jpg')
mark_encoding = face_recognition.face_encodings(image_of_mark)[0]

image_of_snoop = face_recognition.load_image_file('./img/known/Snoop Dogg.jpg')
snoop_encoding = face_recognition.face_encodings(image_of_snoop)[0]

image_of_daniel = face_recognition.load_image_file('./img/known/Daniel Ek.jpg')
daniel_encoding = face_recognition.face_encodings(image_of_daniel)[0]

image_of_sean = face_recognition.load_image_file('./img/known/Sean Parker.jpg')
sean_encoding = face_recognition.face_encodings(image_of_sean)[0]

known_face_encodings = [
	mark_encoding,
	snoop_encoding,
	daniel_encoding,
	sean_encoding	
]

known_face_names = [
	"Mark Zuckerberg",
	"Snoop Dogg",
	"Daniel Ek",
	"Sean Parker"
]

#Load test iamge to find faces in
test_image = face_recognition.load_image_file('./img/groups/famous.jpg')

#Find faces in test image
face_locations = face_recognition.face_locations(test_image)
face_encodings = face_recognition.face_encodings(test_image, face_locations)

#Convert to PIL format
pil_image = Image.fromarray(test_image)


#Creat an image draw instance
draw = ImageDraw.Draw(pil_image)

#Loop through faces in test image
for(top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
	matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

	name = "Unknown Person"

	#If match
	if True in matches:
		first_match_index = matches.index(True)
		name = known_face_names[first_match_index]

	#Draw Box
	draw.rectangle(((left, top), (right, bottom)), outline=(0,0,0))

	#Draw Label
	text_width, text_height = draw.textsize(name)
	draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0,0,0), 
		outline=(0,0,0))
	draw.text((left + 6, bottom - text_height - 5), name, fill=(255,255,255))

del draw

#Display Image
pil_image.show()