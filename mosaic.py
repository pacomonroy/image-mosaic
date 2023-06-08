from wordcloud import WordCloud
from PIL import Image
import numpy as np

# Your text
text = """
PATER noster, qui es in cœlis; sanctificetur nomen tuum: Adveniat regnum tuum; fiat voluntas tua, sicut in cœlo, et in terra. Panem nostrum cotidianum da nobis hodie: Et dimitte nobis debita nostra, sicut et nos dimittimus debitoribus nostris: et ne nos inducas in tentationem: sed libera nos a malo
"""

# Words to emphasize
emphasize = ["PATER", "regnum  ", "Panem"]

# Repeat emphasized words
for word in emphasize:
    text += (word + ' ') * 5  # Repeat each word 5 times

# Create a mask image
mask = np.array(Image.open('input_mask.png'))


# Function to always return black
def black_color_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    return "black"

# Generate a word cloud image
wordcloud = WordCloud(background_color="white", mask=mask, color_func=black_color_func, width=1200, height=800).generate(text)

# Save the image to a file
wordcloud.to_file("worldcloud_output.png")

# Display the generated image
import matplotlib.pyplot as plt
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()