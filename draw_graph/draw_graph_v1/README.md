graph
===============
.wav -> color graph or min,max graph
-
## "script.sh" 
�ɼǿ� ���� �׷����� ������
## "input_handler.py" 
.wav�� 1�ʾ� ��� zmq�� �۽���
## "fft.py" 
zmq�� ������ �����͸� fft��ȯ, dbv��ȯ �� ����� time_ndarray.txt, val_ndarray.txt�� ����
## "draw_graph.py" 
time_ndarray.txt, val_ndarray.txt�� �о�� ������ ǥ���� �׷����� �׸�
## "minmaxavg.py" 
time_ndarray.txt, val_ndarray.txt�� �о�� �� �ð��� ���ؼ� min, max, avg���� min���� index, max���� index�� .txt���Ͽ� ����
## "minmaxplot.py" 
minmaxavg.py���� ���� .txt�� �̿��Ͽ� (�ð�, �ּڰ�) �׷����� (�ð�, �ִ�) �׷����� �׸�