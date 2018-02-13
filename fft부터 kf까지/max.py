import numpy as np
import sys

class maxindex_handler:
	def __init__(self):
		self.in_t = open("time_ndarray.txt", "r")
		self.in_val = open("val_ndarray.txt", "r")
		self.out_t = open("time_from_maxindex.txt", "w")
		self.out_distance = open("distance_from_maxindex.txt", "w")

		self.n = 882  # 나중에 테스트해보고 탐지 범위가 최대 100m라면 반으로 줄여도 됨
		self.lfm = [2260E6, 2590E6] #e6 = * 10^6
		self.max_detect = 3E8/(2*(self.lfm[1]-self.lfm[0]))*self.n/2  # 주파수로 탐지할 수 있는 거리 나타내는 식
		self.y_len = 1764

		self.ignore_range = 2.5  # 앞에 2.5정도 잘라 버림(노이즈때문에), 3m까진 버려도 될 듯
		self.ignore_index = int(self.ignore_range*self.y_len/self.max_detect)

		self.initial_t = -1
		self.initial_distance = -1
		self.min_initial_distance = 10
		self.front_val = []
		self.front_t = []

	def get_line(self, time):
		self.data_t = []
		self.data_val = []
		split_line = self.in_t.readline().split()
		split_line = [float(j) for j in split_line]  # change string to float
		split_line.append(float(time+1))
		self.data_t = np.array(split_line)
		self.data_tlen = len(self.data_t)

		for j in range (0, self.data_tlen-1):
			split_line = self.in_val.readline().split()
			k=0
			for item in split_line:
				split_line[k] = max(-80,float(item))  # -80을 넘어가면 버림
				k+=1
			self.data_val.append(split_line)
		self.data_vallen = len(split_line)
		self.data_val = np.array(self.data_val)
		return self.data_tlen, self.data_vallen

	def print_max(self):
		self.t = []
		self.max_range = []
		for j in range(0, self.data_tlen-1):
			self.t.append((self.data_t[j]+self.data_t[j+1])/2)
			max_index = np.argmax(self.data_val[j][self.ignore_index:])
			ignored = self.ignore_index*self.max_detect/self.y_len
			self.max_range.append(ignored + max_index*self.max_detect/self.y_len)
			self.out_t.write(str(self.t[-1])+' ')
			self.out_distance.write(str(self.max_range[-1])+' ')
		self.out_t.write("\n")
		self.out_distance.write("\n")
		if(self.initial_t == -1 and self.initial_distance == -1):
			self.set_initial()
		return self.t, self.max_range

	def set_initial(self):
		t = []
		val = []

		for i in range(0, self.data_tlen-1):
			if(self.max_range[i]>self.min_initial_distance):  # 최소 시작거리보다 먼 것을 찾음
				t.append(self.t[i])
				val.append(self.max_range[i])
		long_val = np.array(self.front_val + val)

		# 분산이 100 이하일때만 진행함, 평균에 가장 가까운 값을 찾는 코드
		if(len(long_val) > 10 and np.var(long_val) < 100):
			minimum = 100
			mean = np.mean(long_val)
			for i in range(0, len(long_val)):
				if abs(long_val[i] - mean) < minimum:  # 편차가 100보다 작을 때만 진행
					self.initial_t = (self.front_t + t)[i]
					self.initial_distance = long_val[i]
					minimum = abs(long_val[i] - mean)

		self.front_val = val
		self.front_t = t

total_t = []
total_max_range = []

def main():
	global total_t, total_max_range	
	print("start get max part")
	maxhandler = maxindex_handler()

	wav_time = int(25)
	for i in range(0, wav_time):
		tlen, vallen = maxhandler.get_line(i)
		print(i,tlen,vallen)
		t, max_range = maxhandler.print_max()
		total_t += t
		total_max_range += max_range
	print("Kalman Filter initial time:", maxhandler.initial_t, "/ initial distance:", maxhandler.initial_distance)
	print("end get max part")

	

main()