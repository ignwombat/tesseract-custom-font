cd tesstrain

# Tesstrain will look for the ground truth in tesstrain/data/basename-ground-truth 
MODEL_NAME=mc

MAX_ITERATIONS=10000
EPOCHS=1000

# PSM 7 treats each training image as a single line of text
PSM=7

# Insert start model if applicable
START_MODEL=eng

TESSDATA_PREFIX=../tesseract/tessdata \
    make training \
    MODEL_NAME=$MODEL_NAME \
    MAX_ITERATIONS=$MAX_ITERATIONS \
    EPOCHS=1000 \
    PSM=$PSM \
    START_MODEL=$START_MODEL \
    TESSDATA=../tesseract/tessdata