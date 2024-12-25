# hex arrays of digits to be converted to framebuffer via framebuf.FrameBuffer(_,24,32,framebuf.MONO_HLSB)
# (height,width) = (32,24) for digits d0 to d9, = (32,8) for colon, = (16,24) for cake
# Font: DSEG14 classic bold
d0 = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x07, 0xff, 0xe0, 0x1f, 0xff, 0xf8, 0x1f, 0xff, 0xf8, 0x1e, 0x00, 0x78, 0x1e, 0x00, 0xf8, 0x1e, 0x01, 0xf8, 0x1e, 0x01, 0xf8, 0x1e, 0x03, 0xf8, 0x1e, 0x03, 0xf8, 0x1e, 0x03, 0xf8, 0x1e, 0x03, 0x78, 0x1e, 0x01, 0x38, 0x1c, 0x00, 0x38, 0x18, 0x00, 0x18, 0x18, 0x00, 0x18, 0x1c, 0x00, 0x18, 0x1c, 0x00, 0x38, 0x1e, 0x80, 0x38, 0x1f, 0xc0, 0x38, 0x1f, 0xc0, 0x38, 0x1f, 0xc0, 0x38, 0x1f, 0xc0, 0x38, 0x1f, 0x80, 0x38, 0x1f, 0x80, 0x38, 0x1f, 0x00, 0x38, 0x1f, 0xff, 0xf8, 0x1f, 0xff, 0xf8, 0x0f, 0xff, 0xe0, 0x07, 0xff, 0xe0, 0x00, 0x00, 0x00]
d1 = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x08, 0x00, 0x00, 0x18, 0x00, 0x00, 0x38, 0x00, 0x00, 0x38, 0x00, 0x00, 0x38, 0x00, 0x00, 0x38, 0x00, 0x00, 0x38, 0x00, 0x00, 0x38, 0x00, 0x00, 0x38, 0x00, 0x00, 0x38, 0x00, 0x00, 0x38, 0x00, 0x00, 0x38, 0x00, 0x00, 0x18, 0x00, 0x00, 0x18, 0x00, 0x00, 0x18, 0x00, 0x00, 0x38, 0x00, 0x00, 0x38, 0x00, 0x00, 0x38, 0x00, 0x00, 0x38, 0x00, 0x00, 0x38, 0x00, 0x00, 0x38, 0x00, 0x00, 0x38, 0x00, 0x00, 0x38, 0x00, 0x00, 0x38, 0x00, 0x00, 0x38, 0x00, 0x00, 0x18, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
d2 = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x07, 0xff, 0xe0, 0x07, 0xff, 0xf8, 0x03, 0xff, 0xf8, 0x00, 0x00, 0x38, 0x00, 0x00, 0x38, 0x00, 0x00, 0x38, 0x00, 0x00, 0x38, 0x00, 0x00, 0x38, 0x00, 0x00, 0x38, 0x00, 0x00, 0x38, 0x00, 0x00, 0x38, 0x00, 0x00, 0x38, 0x01, 0xc3, 0xf8, 0x03, 0xe7, 0xf8, 0x07, 0xe7, 0xc0, 0x1f, 0xe7, 0x80, 0x1e, 0x00, 0x00, 0x1e, 0x00, 0x00, 0x1e, 0x00, 0x00, 0x1e, 0x00, 0x00, 0x1e, 0x00, 0x00, 0x1e, 0x00, 0x00, 0x1e, 0x00, 0x00, 0x1e, 0x00, 0x00, 0x1e, 0x00, 0x00, 0x1f, 0xff, 0x80, 0x1f, 0xff, 0xc0, 0x0f, 0xff, 0xe0, 0x07, 0xff, 0xe0, 0x00, 0x00, 0x00]
d3 = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x0f, 0xff, 0xc0, 0x0f, 0xff, 0xf0, 0x07, 0xff, 0xf0, 0x00, 0x00, 0x70, 0x00, 0x00, 0x70, 0x00, 0x00, 0x70, 0x00, 0x00, 0x70, 0x00, 0x00, 0x70, 0x00, 0x00, 0x70, 0x00, 0x00, 0x70, 0x00, 0x00, 0x70, 0x00, 0x00, 0x70, 0x03, 0x87, 0xf0, 0x07, 0xcf, 0xf0, 0x07, 0xcf, 0xb0, 0x07, 0xcf, 0xf0, 0x00, 0x00, 0x70, 0x00, 0x00, 0x70, 0x00, 0x00, 0x70, 0x00, 0x00, 0x70, 0x00, 0x00, 0x70, 0x00, 0x00, 0x70, 0x00, 0x00, 0x70, 0x00, 0x00, 0x70, 0x00, 0x00, 0x70, 0x03, 0xff, 0xf0, 0x07, 0xff, 0xf0, 0x0f, 0xff, 0xc0, 0x0f, 0xff, 0xc0, 0x00, 0x00, 0x00]
d4 = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x10, 0x00, 0x08, 0x18, 0x00, 0x18, 0x1c, 0x00, 0x38, 0x1e, 0x00, 0x38, 0x1e, 0x00, 0x38, 0x1e, 0x00, 0x38, 0x1e, 0x00, 0x38, 0x1e, 0x00, 0x38, 0x1e, 0x00, 0x38, 0x1e, 0x00, 0x38, 0x1e, 0x00, 0x38, 0x1f, 0xc3, 0xf8, 0x1f, 0xe7, 0xf8, 0x03, 0xe7, 0xd8, 0x03, 0xe7, 0xf8, 0x00, 0x00, 0x38, 0x00, 0x00, 0x38, 0x00, 0x00, 0x38, 0x00, 0x00, 0x38, 0x00, 0x00, 0x38, 0x00, 0x00, 0x38, 0x00, 0x00, 0x38, 0x00, 0x00, 0x38, 0x00, 0x00, 0x38, 0x00, 0x00, 0x38, 0x00, 0x00, 0x18, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
d5 = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x07, 0xff, 0xe0, 0x1f, 0xff, 0xe0, 0x1f, 0xff, 0xc0, 0x1e, 0x00, 0x00, 0x1e, 0x00, 0x00, 0x1e, 0x00, 0x00, 0x1e, 0x00, 0x00, 0x1e, 0x00, 0x00, 0x1e, 0x00, 0x00, 0x1e, 0x00, 0x00, 0x1e, 0x00, 0x00, 0x1e, 0x00, 0x00, 0x1f, 0xc3, 0x80, 0x1f, 0xe7, 0xc0, 0x03, 0xe7, 0xc0, 0x03, 0xe7, 0xf8, 0x00, 0x00, 0x38, 0x00, 0x00, 0x38, 0x00, 0x00, 0x38, 0x00, 0x00, 0x38, 0x00, 0x00, 0x38, 0x00, 0x00, 0x38, 0x00, 0x00, 0x38, 0x00, 0x00, 0x38, 0x00, 0x00, 0x38, 0x01, 0xff, 0xf8, 0x03, 0xff, 0xf8, 0x07, 0xff, 0xe0, 0x07, 0xff, 0xe0, 0x00, 0x00, 0x00]
d6 = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x07, 0xff, 0xe0, 0x1f, 0xff, 0xe0, 0x1f, 0xff, 0xc0, 0x1e, 0x00, 0x00, 0x1e, 0x00, 0x00, 0x1e, 0x00, 0x00, 0x1e, 0x00, 0x00, 0x1e, 0x00, 0x00, 0x1e, 0x00, 0x00, 0x1e, 0x00, 0x00, 0x1e, 0x00, 0x00, 0x1e, 0x00, 0x00, 0x1f, 0xc3, 0x80, 0x1f, 0xe7, 0xc0, 0x1f, 0xe7, 0xc0, 0x1f, 0xe7, 0xf8, 0x1e, 0x00, 0x38, 0x1e, 0x00, 0x38, 0x1e, 0x00, 0x38, 0x1e, 0x00, 0x38, 0x1e, 0x00, 0x38, 0x1e, 0x00, 0x38, 0x1e, 0x00, 0x38, 0x1e, 0x00, 0x38, 0x1e, 0x00, 0x38, 0x1f, 0xff, 0xf8, 0x1f, 0xff, 0xf8, 0x0f, 0xff, 0xe0, 0x07, 0xff, 0xe0, 0x00, 0x00, 0x00]
d7 = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x07, 0xff, 0xe0, 0x1f, 0xff, 0xf8, 0x1f, 0xff, 0xf8, 0x1e, 0x00, 0x38, 0x1e, 0x00, 0x38, 0x1e, 0x00, 0x38, 0x1e, 0x00, 0x38, 0x1e, 0x00, 0x38, 0x1e, 0x00, 0x38, 0x1e, 0x00, 0x38, 0x1e, 0x00, 0x38, 0x1e, 0x00, 0x38, 0x1c, 0x00, 0x38, 0x18, 0x00, 0x18, 0x00, 0x00, 0x18, 0x00, 0x00, 0x18, 0x00, 0x00, 0x38, 0x00, 0x00, 0x38, 0x00, 0x00, 0x38, 0x00, 0x00, 0x38, 0x00, 0x00, 0x38, 0x00, 0x00, 0x38, 0x00, 0x00, 0x38, 0x00, 0x00, 0x38, 0x00, 0x00, 0x38, 0x00, 0x00, 0x38, 0x00, 0x00, 0x18, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
d8 = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x07, 0xff, 0xe0, 0x1f, 0xff, 0xf8, 0x1f, 0xff, 0xf8, 0x1e, 0x00, 0x38, 0x1e, 0x00, 0x38, 0x1e, 0x00, 0x38, 0x1e, 0x00, 0x38, 0x1e, 0x00, 0x38, 0x1e, 0x00, 0x38, 0x1e, 0x00, 0x38, 0x1e, 0x00, 0x38, 0x1e, 0x00, 0x38, 0x1f, 0xc3, 0xf8, 0x1f, 0xe7, 0xf8, 0x1f, 0xe7, 0xd8, 0x1f, 0xe7, 0xf8, 0x1e, 0x00, 0x38, 0x1e, 0x00, 0x38, 0x1e, 0x00, 0x38, 0x1e, 0x00, 0x38, 0x1e, 0x00, 0x38, 0x1e, 0x00, 0x38, 0x1e, 0x00, 0x38, 0x1e, 0x00, 0x38, 0x1e, 0x00, 0x38, 0x1f, 0xff, 0xf8, 0x1f, 0xff, 0xf8, 0x0f, 0xff, 0xe0, 0x07, 0xff, 0xe0, 0x00, 0x00, 0x00]
d9 = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x07, 0xff, 0xe0, 0x1f, 0xff, 0xf8, 0x1f, 0xff, 0xf8, 0x1e, 0x00, 0x38, 0x1e, 0x00, 0x38, 0x1e, 0x00, 0x38, 0x1e, 0x00, 0x38, 0x1e, 0x00, 0x38, 0x1e, 0x00, 0x38, 0x1e, 0x00, 0x38, 0x1e, 0x00, 0x38, 0x1e, 0x00, 0x38, 0x1f, 0xc3, 0xf8, 0x1f, 0xe7, 0xf8, 0x03, 0xe7, 0xd8, 0x03, 0xe7, 0xf8, 0x00, 0x00, 0x38, 0x00, 0x00, 0x38, 0x00, 0x00, 0x38, 0x00, 0x00, 0x38, 0x00, 0x00, 0x38, 0x00, 0x00, 0x38, 0x00, 0x00, 0x38, 0x00, 0x00, 0x38, 0x00, 0x00, 0x38, 0x01, 0xff, 0xf8, 0x03, 0xff, 0xf8, 0x07, 0xff, 0xe0, 0x07, 0xff, 0xe0, 0x00, 0x00, 0x00]
cake = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x08, 0x00, 0x00, 0x10, 0x00, 0x00, 0xff, 0x00, 0x1f, 0x10, 0xf8, 0x60, 0x10, 0x06, 0x80, 0x00, 0x01, 0xe0, 0x00, 0x07, 0x9f, 0x00, 0xf9, 0x80, 0xff, 0x01, 0x80, 0x00, 0x01, 0x60, 0x00, 0x06, 0x1f, 0x00, 0xf8, 0x00, 0xff, 0x80]
colon = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x18, 0x3c, 0x18, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x18, 0x3c, 0x18, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]