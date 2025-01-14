# 1895번: 필터 - <img src="https://static.solved.ac/tier_small/7.svg" style="height:20px" /> Silver IV

<!-- performance -->

<!-- 문제 제출 후 깃허브에 푸시를 했을 때 제출한 코드의 성능이 입력될 공간입니다.-->

<!-- end -->

## 문제

[문제 링크](https://boj.kr/1895)


<p>숫자 9개가 오름차순이나 내림차순으로 정렬되어 있을 때, 중앙값은 다섯 번째 숫자이다. 예를 들어, 1, 3, 4, 1, 2, 6, 8, 4, 10의 중앙값은 4이다. (1 ≤ 1 ≤ 2 ≤ 3 ≤ 4 ≤ 4 ≤ 6 ≤ 8 ≤ 10)</p>

<p>이미지 I는 크기가 R&nbsp;× C인 2차원 픽셀이다. (3 ≤ R ≤ 40, 3 ≤ C ≤ 40) 각 픽셀은 어두운 정도 V를 나타낸다. (0 ≤ V ≤ 255)</p>

<p>중앙 필터는 이미지에 있는 노이즈를 제거하는 필터이다. 필터의 크기는 3&nbsp;× 3이고, 이미지의 중앙값을 찾으면서 잡음을 제거한다.</p>

<p>예를 들어, 아래와 같은 6&nbsp;× 5 이미지가 있다.</p>

<p><img alt="" src="https://www.acmicpc.net/upload/images/filter1.gif" style="height:160px; width:200px"></p>

<p>필터링된 이미지의 크기는 4&nbsp;× 3이고, 아래와 같다.</p>

<p><img alt="" src="https://www.acmicpc.net/upload/images/filter2.gif" style="height:110px; width:150px"></p>

<p>가장 왼쪽 윗 행에 필터를 두고, 오른쪽으로 움직이면서 중앙값을 찾는다. 한 행을 모두 이동했으면, 다음 행으로 이동해 다시 중앙값을 찾는다. 아래와 같은 순서를 가진다.</p>

<p><img alt="" src="https://www.acmicpc.net/upload/images/filter3.gif" style="height:160px; width:460px"></p>

<p>위의 그림에서 각각의 중앙값은 36, 36, 21이 된다. 이 값은 필터링된 이미지 J의 첫 행과 같다.&nbsp;</p>

<p>이미지 I가 주어졌을 때, 필터링 된 이미지 J를 구하고, 값이 T보다 크거나 같은 픽셀의 수를 구하는 프로그램을 작성하시오.</p>

<p>예를 들어, T = 40일 때, 위의 예에서 정답은 7이다.&nbsp;</p>



## 입력


<p>첫째 줄에 이미지의 크기 R과 C가 주어진다. 그 다음 R개의 각 줄에는 C개의 픽셀 값이 주어진다. 마지막 줄에는 T값이 주어진다.</p>



## 출력


<p>첫째 줄에 필터링 된 이미지 J의 각 픽셀 값 중에서 T보다 크거나 같은 것의 개수를 출력한다.</p>



## 소스코드

[소스코드 보기](필터.py)