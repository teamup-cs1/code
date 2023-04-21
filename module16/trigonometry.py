import matplotlib.pyplot as trigonometry
import numpy

cycles = int(input("Enter the number of cycles: "))

angles = numpy.arange(0, cycles*numpy.pi, 0.1)
sine_values = numpy.sin(angles)
cosine_values = numpy.cos(angles)

trigonometry.xlabel("Angles in radians")
trigonometry.ylabel("Sine or Cosine")
trigonometry.grid(color= "r")

trigonometry.plot(angles, sine_values, color='y', label="Sine wave")
trigonometry.plot(angles, cosine_values, color='m', label="Cosine wave")
trigonometry.legend()
trigonometry.title(f"Sine and cosine waves for {cycles} cycles")

trigonometry.savefig('sin-cos.png')
trigonometry.show()