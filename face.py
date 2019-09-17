import face_recognition

image = face_recognition.load_image_file('./img/groups/team1.jpg')
image2 = face_recognition.load_image_file('./img/groups/team2.png')

face_locations = face_recognition.face_locations(image)
face_locations2 = face_recognition.face_locations(image2)
#Array of face coords

print(face_locations,"\n",face_locations2)

print(f"There are {len(face_locations)} people inside image 1", "\n", 
      f"There are {len(face_locations2)} people inside image 2")