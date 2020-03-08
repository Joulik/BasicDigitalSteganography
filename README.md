# PythonBasicDigitalSteganography

BasicDigitalSteganography.py
============================

Imagine you want to send a secret message. You may want to have it in the form of a black and white image so you can hide it in another insignificant picture. This is the basic principle of steganography.

The code BasicSteganography.py enables you to do so through the following algorithm inspired by acfogarty.github.io
We use the fact that changing the weak bits of the rgb code of a pixel has an effect that cannot be detected by the human eye. For example, a pixel with the rgb code 127 253 78 looks very similar to a pixel 126 252 77. This means that someone could watch two pictures thinking they are both identical while the images are in fact different. The difference can then store information that is invisible to the person who sees the images. Someone who knows the encoding algorithm can then decipher the hidden information. 

Our algorithm uses the following steps:

Step 1. Choose an insignificant picture to be the carrier image.
Generate your message in a black and white picture having the same dimension as the carrier image.

Both images are treated as pixel arrays

Step 2. Turn the parity of the pixel arrays into boolean arrays.
For example, the pixel [ 125, 64, 33] yields [ False, True, False] (odd=False, even=True) 

Step 3. Construct a filter array through the XOR operation on the boolean arrays above.
filterBool = CarrierImageBool XOR InnocentImageBool

Step 4. Turn the filter boolean array filterBool into an array of integers (0s and 1s) called filter.

Step 5. Generate the image to send with hidden information through message = np.asolute(carrierImage - filter)

In order to decipher the message, it is sufficient to read the parity of the rgb code of the pixels.

BasicSteganography.py uses the GUI made with the Tkinter python library.

Give it a try
=============
Some files were prepared so you can test the tools.
1. To encrypt a message : 
-text.png is a black and white image file of a text and should be used as the image to hide.
-cat_PNG50488_pinkBG.png is an image file expected to be the carrier image.
Generate an image with the embedded text with the encrypt tool.
2. To decipher a message :
-kitty.png is a kitten image with an embedded text. Use the decipher tool to view this text.