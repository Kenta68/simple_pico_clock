# hex arrays of digits to be converted to framebuffer via framebuf.FrameBuffer(_,24,32,framebuf.MONO_HLSB)
# (height,width) = (32,24) for digits d0 to d9, = (32,8) for colon, = (16,24) for cake
# Font: Calibari
d0 = [0x00, 0x3e, 0x00, 0x00, 0xff, 0x80, 0x03, 0xff, 0xe0, 0x07, 0xff, 0xf0, 0x07, 0xc1, 0xf0, 0x0f, 0x00, 0xf8, 0x1f, 0x00, 0x78, 0x1e, 0x00, 0x7c, 0x1e, 0x00, 0x3c, 0x3c, 0x00, 0x3c, 0x3c, 0x00, 0x3c, 0x3c, 0x00, 0x3c, 0x3c, 0x00, 0x3c, 0x3c, 0x00, 0x3c, 0x3c, 0x00, 0x3c, 0x3c, 0x00, 0x3c, 0x3c, 0x00, 0x3c, 0x3c, 0x00, 0x3c, 0x3c, 0x00, 0x3c, 0x3c, 0x00, 0x3c, 0x3c, 0x00, 0x3c, 0x3c, 0x00, 0x3c, 0x3c, 0x00, 0x3c, 0x3c, 0x00, 0x3c, 0x3e, 0x00, 0x3c, 0x1e, 0x00, 0x78, 0x1f, 0x00, 0x78, 0x0f, 0x00, 0xf8, 0x0f, 0xc3, 0xf0, 0x07, 0xff, 0xe0, 0x03, 0xff, 0xc0, 0x00, 0xff, 0x00]
d1 = [0x00, 0x00, 0x00, 0x00, 0x1c, 0x00, 0x00, 0x7c, 0x00, 0x00, 0xfc, 0x00, 0x03, 0xfc, 0x00, 0x07, 0xfc, 0x00, 0x1f, 0xbc, 0x00, 0x1e, 0x3c, 0x00, 0x18, 0x3c, 0x00, 0x00, 0x3c, 0x00, 0x00, 0x3c, 0x00, 0x00, 0x3c, 0x00, 0x00, 0x3c, 0x00, 0x00, 0x3c, 0x00, 0x00, 0x3c, 0x00, 0x00, 0x3c, 0x00, 0x00, 0x3c, 0x00, 0x00, 0x3c, 0x00, 0x00, 0x3c, 0x00, 0x00, 0x3c, 0x00, 0x00, 0x3c, 0x00, 0x00, 0x3c, 0x00, 0x00, 0x3c, 0x00, 0x00, 0x3c, 0x00, 0x00, 0x3c, 0x00, 0x00, 0x3c, 0x00, 0x00, 0x3c, 0x00, 0x00, 0x3c, 0x00, 0x0f, 0xff, 0xf0, 0x1f, 0xff, 0xf8, 0x1f, 0xff, 0xf8, 0x00, 0x00, 0x00]
d2 = [0x00, 0xfc, 0x00, 0x03, 0xff, 0x00, 0x07, 0xff, 0xc0, 0x1f, 0xff, 0xe0, 0x1e, 0x07, 0xe0, 0x18, 0x01, 0xf0, 0x00, 0x01, 0xf0, 0x00, 0x00, 0xf0, 0x00, 0x00, 0xf0, 0x00, 0x00, 0xf0, 0x00, 0x00, 0xf0, 0x00, 0x00, 0xf0, 0x00, 0x01, 0xf0, 0x00, 0x01, 0xe0, 0x00, 0x03, 0xe0, 0x00, 0x03, 0xc0, 0x00, 0x07, 0xc0, 0x00, 0x0f, 0x80, 0x00, 0x0f, 0x00, 0x00, 0x1f, 0x00, 0x00, 0x3e, 0x00, 0x00, 0x7c, 0x00, 0x00, 0xf8, 0x00, 0x01, 0xf0, 0x00, 0x03, 0xe0, 0x00, 0x07, 0xc0, 0x00, 0x0f, 0x80, 0x00, 0x1f, 0x00, 0x00, 0x1f, 0xff, 0xf8, 0x1f, 0xff, 0xfc, 0x1f, 0xff, 0xfc, 0x00, 0x00, 0x00]
d3 = [0x00, 0x7c, 0x00, 0x01, 0xff, 0x00, 0x07, 0xff, 0xc0, 0x0f, 0xff, 0xe0, 0x1f, 0x07, 0xe0, 0x1c, 0x01, 0xf0, 0x08, 0x01, 0xf0, 0x00, 0x00, 0xf0, 0x00, 0x00, 0xf0, 0x00, 0x00, 0xf0, 0x00, 0x00, 0xf0, 0x00, 0x01, 0xe0, 0x00, 0x01, 0xe0, 0x00, 0x03, 0xc0, 0x00, 0x0f, 0x80, 0x03, 0xff, 0x00, 0x03, 0xff, 0x80, 0x03, 0xff, 0xc0, 0x00, 0x07, 0xf0, 0x00, 0x01, 0xf0, 0x00, 0x00, 0xf8, 0x00, 0x00, 0x78, 0x00, 0x00, 0x78, 0x00, 0x00, 0x78, 0x00, 0x00, 0x78, 0x00, 0x00, 0x78, 0x00, 0x00, 0xf8, 0x18, 0x01, 0xf0, 0x3f, 0x07, 0xf0, 0x1f, 0xff, 0xe0, 0x0f, 0xff, 0xc0, 0x03, 0xfe, 0x00]
d4 = [0x00, 0x00, 0x00, 0x00, 0x03, 0xc0, 0x00, 0x07, 0xe0, 0x00, 0x0f, 0xe0, 0x00, 0x1f, 0xe0, 0x00, 0x1f, 0xe0, 0x00, 0x3d, 0xe0, 0x00, 0x79, 0xe0, 0x00, 0x71, 0xe0, 0x00, 0xf1, 0xe0, 0x00, 0xe1, 0xe0, 0x01, 0xe1, 0xe0, 0x03, 0xc1, 0xe0, 0x03, 0x81, 0xe0, 0x07, 0x81, 0xe0, 0x07, 0x01, 0xe0, 0x0f, 0x01, 0xe0, 0x1e, 0x01, 0xe0, 0x1c, 0x01, 0xe0, 0x3c, 0x01, 0xe0, 0x38, 0x01, 0xe0, 0x7f, 0xff, 0xfc, 0x7f, 0xff, 0xfc, 0x7f, 0xff, 0xfc, 0x00, 0x01, 0xe0, 0x00, 0x01, 0xe0, 0x00, 0x01, 0xe0, 0x00, 0x01, 0xe0, 0x00, 0x01, 0xe0, 0x00, 0x01, 0xe0, 0x00, 0x01, 0xe0, 0x00, 0x00, 0x00]
d5 = [0x00, 0x00, 0x00, 0x07, 0xff, 0xe0, 0x0f, 0xff, 0xf0, 0x0f, 0xff, 0xf0, 0x0f, 0xff, 0xe0, 0x0e, 0x00, 0x00, 0x0e, 0x00, 0x00, 0x0e, 0x00, 0x00, 0x0e, 0x00, 0x00, 0x0e, 0x00, 0x00, 0x0e, 0x00, 0x00, 0x0e, 0x00, 0x00, 0x0e, 0x00, 0x00, 0x0f, 0xfc, 0x00, 0x0f, 0xff, 0x80, 0x0f, 0xff, 0xe0, 0x00, 0x03, 0xf0, 0x00, 0x01, 0xf0, 0x00, 0x00, 0xf8, 0x00, 0x00, 0x78, 0x00, 0x00, 0x7c, 0x00, 0x00, 0x7c, 0x00, 0x00, 0x7c, 0x00, 0x00, 0x7c, 0x00, 0x00, 0x7c, 0x00, 0x00, 0x78, 0x00, 0x00, 0xf8, 0x18, 0x01, 0xf0, 0x3e, 0x07, 0xe0, 0x3f, 0xff, 0xe0, 0x1f, 0xff, 0x80, 0x03, 0xfe, 0x00]
d6 = [0x00, 0x0f, 0xc0, 0x00, 0x3f, 0xf0, 0x00, 0xff, 0xf8, 0x01, 0xff, 0xf8, 0x03, 0xe0, 0x00, 0x07, 0xc0, 0x00, 0x07, 0x80, 0x00, 0x0f, 0x00, 0x00, 0x0f, 0x00, 0x00, 0x0f, 0x00, 0x00, 0x1e, 0x00, 0x00, 0x1e, 0x00, 0x00, 0x1e, 0x00, 0x00, 0x1e, 0x1f, 0x80, 0x1e, 0xff, 0xe0, 0x1f, 0xff, 0xf0, 0x1f, 0xe1, 0xf0, 0x1f, 0x00, 0x78, 0x1e, 0x00, 0x3c, 0x1e, 0x00, 0x3e, 0x1e, 0x00, 0x1e, 0x1e, 0x00, 0x1e, 0x1e, 0x00, 0x1e, 0x1e, 0x00, 0x1e, 0x1e, 0x00, 0x3e, 0x1f, 0x00, 0x3c, 0x0f, 0x00, 0x7c, 0x0f, 0x80, 0xf8, 0x07, 0xe1, 0xf0, 0x07, 0xff, 0xe0, 0x01, 0xff, 0xc0, 0x00, 0xff, 0x00]
d7 = [0x00, 0x00, 0x00, 0x1f, 0xff, 0xfc, 0x3f, 0xff, 0xfc, 0x3f, 0xff, 0xfc, 0x1f, 0xff, 0xfc, 0x00, 0x00, 0x7c, 0x00, 0x00, 0x78, 0x00, 0x00, 0x78, 0x00, 0x00, 0xf0, 0x00, 0x00, 0xf0, 0x00, 0x01, 0xe0, 0x00, 0x01, 0xe0, 0x00, 0x03, 0xe0, 0x00, 0x03, 0xc0, 0x00, 0x07, 0xc0, 0x00, 0x07, 0x80, 0x00, 0x07, 0x80, 0x00, 0x0f, 0x00, 0x00, 0x0f, 0x00, 0x00, 0x1f, 0x00, 0x00, 0x1e, 0x00, 0x00, 0x3e, 0x00, 0x00, 0x3c, 0x00, 0x00, 0x7c, 0x00, 0x00, 0x78, 0x00, 0x00, 0x78, 0x00, 0x00, 0xf0, 0x00, 0x00, 0xf0, 0x00, 0x01, 0xf0, 0x00, 0x01, 0xe0, 0x00, 0x03, 0xe0, 0x00, 0x00, 0x00, 0x00]
d8 = [0x00, 0x7f, 0x00, 0x01, 0xff, 0x80, 0x03, 0xff, 0xe0, 0x07, 0xff, 0xf0, 0x0f, 0x80, 0xf8, 0x1f, 0x00, 0x78, 0x1e, 0x00, 0x78, 0x1e, 0x00, 0x78, 0x1e, 0x00, 0x78, 0x1e, 0x00, 0x78, 0x1f, 0x00, 0x78, 0x0f, 0x80, 0xf0, 0x0f, 0xc1, 0xf0, 0x07, 0xe3, 0xe0, 0x03, 0xff, 0x80, 0x00, 0xff, 0x00, 0x00, 0xff, 0x80, 0x03, 0xff, 0xe0, 0x07, 0xc3, 0xf0, 0x0f, 0x81, 0xf8, 0x1f, 0x00, 0x7c, 0x1e, 0x00, 0x7c, 0x3c, 0x00, 0x3c, 0x3c, 0x00, 0x3c, 0x3c, 0x00, 0x3c, 0x3c, 0x00, 0x3c, 0x3e, 0x00, 0x3c, 0x1e, 0x00, 0x7c, 0x1f, 0x80, 0xf8, 0x0f, 0xff, 0xf0, 0x07, 0xff, 0xe0, 0x01, 0xff, 0x80]
d9 = [0x00, 0x7e, 0x00, 0x01, 0xff, 0x80, 0x03, 0xff, 0xc0, 0x07, 0xff, 0xe0, 0x0f, 0x81, 0xf0, 0x1f, 0x00, 0xf0, 0x1e, 0x00, 0x78, 0x3c, 0x00, 0x78, 0x3c, 0x00, 0x78, 0x3c, 0x00, 0x7c, 0x3c, 0x00, 0x3c, 0x3c, 0x00, 0x3c, 0x3c, 0x00, 0x3c, 0x3e, 0x00, 0x3c, 0x1e, 0x00, 0x3c, 0x1f, 0x00, 0xfc, 0x0f, 0xff, 0xfc, 0x07, 0xff, 0xfc, 0x03, 0xff, 0x3c, 0x00, 0x7c, 0x3c, 0x00, 0x00, 0x3c, 0x00, 0x00, 0x38, 0x00, 0x00, 0x78, 0x00, 0x00, 0x78, 0x00, 0x00, 0xf0, 0x00, 0x00, 0xf0, 0x00, 0x01, 0xf0, 0x00, 0x03, 0xe0, 0x1c, 0x0f, 0xc0, 0x1f, 0xff, 0x80, 0x1f, 0xff, 0x00, 0x07, 0xf8, 0x00]
cake = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x08, 0x00, 0x00, 0x10, 0x00, 0x00, 0xff, 0x00, 0x1f, 0x10, 0xf8, 0x60, 0x10, 0x06, 0x80, 0x00, 0x01, 0xe0, 0x00, 0x07, 0x9f, 0x00, 0xf9, 0x80, 0xff, 0x01, 0x80, 0x00, 0x01, 0x60, 0x00, 0x06, 0x1f, 0x00, 0xf8, 0x00, 0xff, 0x80]
colon = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x18, 0x3c, 0x3c, 0x3c, 0x18, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x18, 0x3c, 0x3c, 0x3c, 0x18, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
