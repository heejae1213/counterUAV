noise cancelling
===============
.wav -> noise cancel -> find max -> draw max graph
-
## ������ ĵ���� ���
������ �߿��� 2.5m �Ʒ��� �ִ� �����͸� ��� �����Ѵ�.

## "script.sh" 
������ ĵ���� �� max���� �׷����� �׷���
## "fft.py" 
wav������ �����͸� fft��ȯ, dbv��ȯ �� ����� time_ndarray.txt, val_ndarray.txt�� ����
## "max.py" 
time_ndarray.txt, val_ndarray.txt�� �о�� ����� ������ �� �� �ð��� ���ؼ� max���� index�� .txt���Ͽ� ����
## "maxplot.py" 
max.py���� ���� .txt�� �̿��Ͽ� (�ð�, max���� index) �׷����� �׸�

##range_test2_result.jpg
'range_test2.wav'������ �̿��Ͽ� ���� ���
