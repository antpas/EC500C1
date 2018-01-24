import ffmpy

ff = ffmpy.FFmpeg(
    inputs={'input.mp4': None},
    outputs={'output.avi': None}
)
ff.run()
