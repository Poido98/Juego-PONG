class Boton():
	def __init__(self, image, pos, text_input, font, color_base, color_mouse_arriba):
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.color_base = color_base
		self.color_mouse_arriba = color_mouse_arriba
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.color_base)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, pantalla):
		"""Colocamos la imagen y el texto en la pantalla"""
		if self.image is not None:
			pantalla.blit(self.image, self.rect)
		pantalla.blit(self.text, self.text_rect)

	# def chequear_input(self, posicion):
	# 	"""Comprobamos si estamos haciendo click en el boton"""
	# 	if posicion[0] in range(self.rect.left, self.rect.right) and posicion[1] in range(self.rect.top, self.rect.bottom):
	# 		return True
	# 	return False

	# def cambiar_color(self, posicion):
	# 	"""Cambiamos de color si el mouse pasa por arriba del boton"""
	# 	if posicion[0] in range(self.rect.left, self.rect.right) and posicion[1] in range(self.rect.top, self.rect.bottom):
	# 		self.text = self.font.render(self.text_input, True, self.color_mouse_arriba)
	# 	else:
	# 		self.text = self.font.render(self.text_input, True, self.color_base)
	

	def chequear_input(self, posicion):
		return self.rect.collidepoint(posicion)

	def cambiar_color(self, posicion):
		color_actual = self.color_mouse_arriba if self.rect.collidepoint(posicion) else self.color_base
		self.text = self.font.render(self.text_input, True, color_actual)


	