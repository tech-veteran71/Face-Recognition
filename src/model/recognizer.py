import cv2
import numpy as np
import face_recognition as frn

class Recognizer:

	def __init__(self, unknown_face_title, faces_data, rec_params):
		self.__unknown_face_title = unknown_face_title
		self.__faces_data = faces_data
		self.__rec_params = rec_params

	def process_current_frame(self, frame: np.ndarray) -> list:
		faces_locations = frn.face_locations(frame)
		faces_encodings = frn.face_encodings(
			frame, faces_locations
		)

		faces_names = []

		for fe in faces_encodings:
			matches = frn.compare_faces(
				self.__faces_data.encodings.tolist(),
				fe,
				tolerance=self.__rec_params.rec_tolerance
			)

			name = self.__unknown_face_title

			face_distances = frn.face_distance(
				self.__faces_data.encodings.tolist(), fe
			)
			best_match_index = np.argmin(face_distances)

			if matches[best_match_index]:
				name = self.__faces_data.names[best_match_index]

			faces_names.append(name)

		return faces_locations, faces_names

	def identify_faces(self, frame, faces_locations, faces_names) -> np.ndarray:
		for face_location, name in zip(faces_locations, faces_names):
			top, right, bottom, left = self.__return_original_scale(
				list(face_location)
			)

			rect_color = self.__define_face_rect_color(name)			

			cv2.rectangle(
				frame, 
				(left, top), 
				(right, bottom), 
				rect_color, 
				self.__rec_params.face_rect_thick
			)

			font = cv2.FONT_HERSHEY_COMPLEX
			cv2.putText(
				frame, 
				name, 
				(left, bottom + 30),
				font, 
				self.__rec_params.face_rect_text_scale,
				self.__rec_params.face_rect_text_color,
				self.__rec_params.face_rect_text_thick
			)

		return frame

	def __define_face_rect_color(self, name) -> tuple:
		if name == self.__unknown_face_title:
			return self.__rec_params.unknown_face_rect_color
		else:
			return self.__rec_params.known_face_rect_color

	def __return_original_scale(self, location: list) -> list:
		scale = 1 / self.__rec_params.frame_resize_scale

		return [int(i * scale) for i in location]