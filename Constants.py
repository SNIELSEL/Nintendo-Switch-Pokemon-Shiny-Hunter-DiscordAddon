###########################################################################################################################
#################################################     IMAGE PROCESSING     ################################################
###########################################################################################################################

# ↓↓ [RGB] Default Ranges
LOWER_COLOR = (55, 110, 0)
UPPER_COLOR = (200, 255, 70)
# ↓↓ [PIXELS] Nintendo Switch captured frames' size 
ORIGINAL_FRAME_SIZE = (1920, 1080)
# ↓↓ [PIXELS] Size the captured frame is resized to
NEW_FRAME_SIZE = (500, 281)
# ↓↓ Text style for the FPS counter
TEXT_PARAMS = {
    'font_scale': 0.5,
    # ↓↓ [RGB]
    'font_color': (255, 0, 125),
    'thickness': 2,
    # ↓↓ [PIXELS]
    'position': (2, 15)
}
RECTANGLES_PARAMS = {
    'color': (0, 255, 0),
    'thickness': 4
}
# ↓↓ [PIXELS²] Minimum area to detect something as a match
MIN_DETECT_SIZE = 300

###########################################################################################################################
#######################################################     GUI     #######################################################
###########################################################################################################################

# ↓↓ GUI title
BOT_NAME = "FBot Shiny Hunter"
# ↓↓ [PIXELS] GUI size
BOT_WINDOW_SIZE = (1000, 562)
# ↓↓ All image paths must be relative paths from the main folder
SELECT_IMAGE_PATH = "./Media/Select Image.png"

###########################################################################################################################
##################################################     VIDEO CAPTURE     ##################################################
###########################################################################################################################

VIDEO_CAPTURE_INDEX = 1
FPS_COUNTER = True
# ↓↓ [SECONDS]
REFRESH_FPS_TIME = 1