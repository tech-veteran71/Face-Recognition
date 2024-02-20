from PyQt5.QtGui import QPixmap, QColor
from PyQt5.QtWidgets import QWidget
from view.recognition_parameters_window import Ui_Form as rpw_ui_form
from model.face_recognition_model import FaceRecognitionModel as FRM
from utils.cv_to_qt_converter import *
from utils.stream_types import StreamTypes

class FaceRecognitionController:
	
	def __init__(self, main_view, main_model):
		self.__main_view = main_view
		self.__model = main_model

		self.__main_view.controller = self
		self.__connect_signals()

		self.__output_img_width = 1280
		self.__output_img_height = 720

		self.__main_view.show()

	def set_stream_src(self, stream) -> None:
		self.__model.stream_src = stream

	def __stop_recognition(self) -> None:
		self.__model.stop()

	def __start_recognition(self) -> None:
		self.__model.start()

	def __open_parametres_win(self) -> None:
		self.__parameters_win = QWidget()
		parameters_win_ui = rpw_ui_form()
		parameters_win_ui.setupUi(self.__parameters_win)
		self.__parameters_win.show()

	def __set_output_image_size(self, size) -> None:
		self.__output_img_width = size[0]
		self.__output_img_height = size[1]

	def __update_image(self, cv_img) -> None:
		img = convert_cv_to_qt(
			cv_img, 
			self.__output_img_width, 
			self.__output_img_height
		)
		self.__main_view.update_image(img)

	def __load_face_images(self, images) -> None:
		self.__model.prepare_face_images(images)

	def __set_video_str_path(self, path) -> None:
		self.__model.video_src = path

	def __set_stream_type(self, stream_type) -> None:
		self.__model.stream_src = stream_type

	def __connect_signals(self) -> None:
		self.__model.change_image_signal.connect(self.__update_image)
		self.__main_view.change_image_output_size_signal.connect(
			self.__set_output_image_size
		)
		self.__main_view.open_recognition_parameters_win_signal.connect(
			self.__open_parametres_win
		)
		self.__main_view.start_recognition_signal.connect(
			self.__start_recognition
		)
		self.__main_view.stop_recognition_signal.connect(
			self.__stop_recognition
		)
		self.__main_view.face_images_load_signal.connect(
			self.__load_face_images
		)
		self.__main_view.video_src_load_signal.connect(
			self.__set_video_str_path
		)
		self.__main_view.stream_src_type_signal.connect(
			self.__set_stream_type
		)