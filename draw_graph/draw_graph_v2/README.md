graph
===============
.wav -> color graph or max graph
-
## "script.sh" 
�ɼǿ� ���� �׷����� ������
## "fft.py" 
wav������ �����͸� fft��ȯ, dbv��ȯ �� ����� time_ndarray.txt, val_ndarray.txt�� ����
## "draw_graph.py" 
time_ndarray.txt, val_ndarray.txt�� �о�� ������ ǥ���� �׷����� �׸�
## "max.py" 
time_ndarray.txt, val_ndarray.txt�� �о�� �� �ð��� ���ؼ� max���� index�� .txt���Ͽ� ����
## "maxplot.py" 
max.py���� ���� .txt�� �̿��Ͽ� (�ð�, max���� index) �׷����� �׸�

## v1���� ����
* 'input_handler.py'�� 'fft.py'�� 'fft.py'�� ��ħ
* 'draw_graph.py'�� ������ ó�������� (�����͸� �������� �������ν�)��������
* 'minmaxavg.py'�� max���� ���ϴ� 'max.py'�� �ٲ�
* 'minmaxplot.py'�� max���� ���� �׷����� �׸��� 'maxplot.py'�� �ٲ�