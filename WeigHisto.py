# =======================================================================================
#
#	  							   2D WEIGHTENED HISTOGRAM
#
# =======================================================================================

# DESCRIPTION
# 

# © Ondřej Finke, 2020, Developed with Python 3.7 (64-bit)

# IMPORTS
import numpy as np
import matplotlib.pyplot as pt
from matplotlib import cm

# CLASS DEF
class WeigHisto():

	def __init__(self, d, w, b):
		self.data = d
		self.weight = w
		self.bins = b
		# CYCLE THROUGH BINS
		self.hiVal = np.zeros(len(self.bins))
		i = 0
		for i in range(self.bins.size - 1): 
			# create mask for specific bin 
			mask = (self.data > self.bins[i]) & (self.data < self.bins[i+1])
			self.hiVal[i] = np.sum(self.weight[mask])

	def PlotDetail(self):
		# DATA HEATMAP
		fig = pt.figure(figsize = [9,4.5])
		# plot intensity heatmap
		ax1 = pt.subplot(1,2,1)
		ax1.imshow(self.data, cmap = cm.hot, origin = "lower")
		ax1.set_xticks([])
		ax1.set_yticks([])
		ax1.set_title("Data")
		# plot intensity heatmap
		ax2 = pt.subplot(1,2,2)
		ax2.imshow(self.weight, cmap = cm.pink, origin = "lower")
		ax2.set_xticks([])
		ax2.set_yticks([])
		ax2.set_title("Weight")
		pt.draw()
		# weightened histogram
		fig = pt.figure(figsize = [4.5,4.5])
		fig.suptitle("2D Weightened Histogram")
		ax3 = pt.subplot(1,1,1)
		ax3.bar(np.arange(1,len(self.hiVal),1),self.hiVal[:-1],edgecolor='black')
		ax3.set_xticks((np.arange(1,len(self.hiVal),1)))
		pt.draw()
		

	def PlotRandMask(self):
		# pick random bin
		ind = np.random.choice(len(self.bins[:-1]))
		mask = (self.data > self.bins[ind]) & (self.data < self.bins[ind+1])
		
		# plot the mask
		fig = pt.figure(figsize = [9,4.5])
		fig.suptitle("Randomly selected mask")
		# plot intensity heatmap
		ax1 = pt.subplot(1,2,1)
		ax1.imshow(self.data, cmap = cm.hot, origin = "lower")
		ax1.set_xticks([])
		ax1.set_yticks([])
		ax1.set_title("Data")
		# plot intensity heatmap
		ax2 = pt.subplot(1,2,2)
		ax2.imshow(mask, cmap = cm.pink, origin = "lower")
		ax2.set_xticks([])
		ax2.set_yticks([])
		ax2.set_title("".join(["Mask for interval: ", str(np.around(self.bins[ind], decimals=3)),", ", \
						 str(np.around(self.bins[ind+1], decimals=3))]))
		pt.draw()

	def PlotHisto(self):
		# weightened histogram
		fig = pt.figure(figsize = [4.5,4.5])
		fig.suptitle("2D Weightened Histogram")
		ax1 = pt.subplot(1,1,1)
		ax1.bar(np.arange(1,len(self.hiVal),1),self.hiVal[:-1],edgecolor='black')
		ax1.set_xticks((np.arange(1,len(self.hiVal),1)))
		pt.draw()

	def ReturnResult(self):
		return self.hiVal[:-1]

# TESTING RUNTIME
# create root window
def main():
	print("--------------- 2D WEIGHTENED HISTOGRAM ---------------")
	print("Testing procedure...")

	# random data generation
	print("Generating random data...")
	data = np.random.rand(20,20)
	#weig = np.ones([20, 20])
	weig = np.empty([20, 20])
	for i in range(0,20):
		weig[:,i] = np.arange(1, 21, 1)
	bins = np.linspace(0,1,11)
	
	print("Starting timer...")

	# calculate histogram
	print("Calculating weightened histogram...")
	wh = WeigHisto(data, weig, bins)
	
	print("Calculation ran for:")
	
	# plot histogram
	print("Plotting result...")
	wh.PlotDetail()
	wh.PlotRandMask()
	pt.show()

if __name__ == "__main__":
	main()