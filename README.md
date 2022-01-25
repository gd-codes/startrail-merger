# startrail-merger

![Animated GIF of stars & clouds moving across the night sky](anim.gif)

An experiment to combine a time-lapse sequence of photographs of the night sky into one still photograph, while retaining only the stars and background.

-------

To composite a star trail from multiple short-exposure photos taken of the night sky in clear weather, is possible most often by directly merging them into one using tools such as the "*Lighten*" layer blend mode in Adobe Photoshop & other software, which creates a composite using only the brightest pixels at the same location in all the layers (images stacked one over another). However, if a small light-grey / white cloud moved across the frame, it obscures that entire region in the merged photo, because it may be lighter than the stars/sky behind it. This hides a lot of detail in the photograph that was otherwise visible most of the time.

### Methodology

To composite the images effectively, the stars can be identified and selected by generating a segmentation mask of each frame. Only areas that have been masked will be able to potentially appear in the final image, after similar *Lighten*-blending. I attempted 2 different ways of doing this :

- [**script1.ipynb**](script1.ipynb) - Using OpenCV and image processing operations such as Convolution and Dilation
- [**script2.ipynb**](script2.ipynb) - Using Tensorflow and a CNN trained to generate such a mask from the image.


### Results

Both of the algorithms achieved their goal ! The output images, along with a comparison to the regular "control" method of compositing without any processing, are visible in each of the notebooks. 

As expected, the images don't look as clean as a normal star trail because wherever the clouds did pass over any stars, they remain invisible in those pixels (the scripts don't *generate* image data or add artificial details, only remove information wherever necessary).

The Neural Network is a lot slower and lot more computatioanlly expensive, but produces a slightly cleaner result than the simple convolution kernel, which is quite fast but makes the star trails appear a bit grainy/broken.

### License

I took the photographs and drew the masks used to train the neural network by myself. These are present in the `data` folder. I have made this repository public after placing them under a [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/) license. That license file is within the [`data`](./data) folder and applies to its contents.

I don't wish to hold any copyright over the code (all `.ipynb` notebooks, `.py` files, etc, in this repo), so I released those under the [Unlicense](https://unlicense.org). That file is located in the root of this repository.
