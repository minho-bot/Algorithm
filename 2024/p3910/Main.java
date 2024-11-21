import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

/**

 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
 1 초	128 MB	81835	35276	23760	41.515%
 문제
 'Dummy' 라는 도스게임이 있다. 이 게임에는 뱀이 나와서 기어다니는데, 사과를 먹으면 뱀 길이가 늘어난다. 뱀이 이리저리 기어다니다가 벽 또는 자기자신의 몸과 부딪히면 게임이 끝난다.

 게임은 NxN 정사각 보드위에서 진행되고, 몇몇 칸에는 사과가 놓여져 있다. 보드의 상하좌우 끝에 벽이 있다. 게임이 시작할때 뱀은 맨위 맨좌측에 위치하고 뱀의 길이는 1 이다. 뱀은 처음에 오른쪽을 향한다.

 뱀은 매 초마다 이동을 하는데 다음과 같은 규칙을 따른다.

 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
 만약 벽이나 자기자신의 몸과 부딪히면 게임이 끝난다.
 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
 사과의 위치와 뱀의 이동경로가 주어질 때 이 게임이 몇 초에 끝나는지 계산하라.

 입력
 첫째 줄에 보드의 크기 N이 주어진다. (2 ≤ N ≤ 100) 다음 줄에 사과의 개수 K가 주어진다. (0 ≤ K ≤ 100)

 다음 K개의 줄에는 사과의 위치가 주어지는데, 첫 번째 정수는 행, 두 번째 정수는 열 위치를 의미한다. 사과의 위치는 모두 다르며, 맨 위 맨 좌측 (1행 1열) 에는 사과가 없다.

 다음 줄에는 뱀의 방향 변환 횟수 L 이 주어진다. (1 ≤ L ≤ 100)

 다음 L개의 줄에는 뱀의 방향 변환 정보가 주어지는데, 정수 X와 문자 C로 이루어져 있으며. 게임 시작 시간으로부터 X초가 끝난 뒤에 왼쪽(C가 'L') 또는 오른쪽(C가 'D')로 90도 방향을 회전시킨다는 뜻이다. X는 10,000 이하의 양의 정수이며, 방향 전환 정보는 X가 증가하는 순으로 주어진다.

 출력
 첫째 줄에 게임이 몇 초에 끝나는지 출력한다.

 예제 입력 1
 6
 3
 3 4
 2 5
 5 3
 3
 3 D
 15 L
 17 D
 예제 출력 1
 9
 예제 입력 2
 10
 4
 1 2
 1 3
 1 4
 1 5
 4
 8 D
 10 D
 11 D
 13 L
 예제 출력 2
 21
 예제 입력 3
 10
 5
 1 5
 1 3
 1 2
 1 6
 1 7
 4
 8 D
 10 D
 11 D
 13 L
 예제 출력 3
 13

 */
public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int[][] direction = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        int direction_index = 0;
//        for (int i=0; i<4; i++) {
//            System.out.println("direction = " + Arrays.toString(direction[i]));
//        }


        st = new StringTokenizer(bf.readLine());
        int N = Integer.parseInt(st.nextToken());
        int[][] map = new int[N][N];

//        System.out.println("N = " + N);

        st = new StringTokenizer(bf.readLine());
        int K = Integer.parseInt(st.nextToken());

        int x, y;
        for (int i=0; i<K; i++) {
            st = new StringTokenizer(bf.readLine());
            x = Integer.parseInt(st.nextToken());
            y = Integer.parseInt(st.nextToken());
//            System.out.println("x= " + x + "y= " + y);
            map[x-1][y-1] = 1;
        }

        st = new StringTokenizer(bf.readLine());
        int L = Integer.parseInt(st.nextToken());
        String c;
        String[] direction_change = new String[10001];


        for (int i=0; i<L; i++) {
            st = new StringTokenizer(bf.readLine());
            x = Integer.parseInt(st.nextToken());
            c = st.nextToken();
//            System.out.println("x= " + x + "c= " + c);
            direction_change[x] = c;
        }

        Deque<int[]> q = new LinkedList<>();
        q.offerFirst(new int[]{0, 0});

        int second = 0;
        while (q.size() > 0) {
            int[] head = q.peek();

            if (direction_change[second] != null) {
                if (direction_change[second].equals("D")) {
                    direction_index += 1;
                }
                else if (direction_change[second].equals("L")) {
                    direction_index -= 1;
                }
            }

            direction_index = (direction_index+4)%4;

            int next_x = head[0] + direction[direction_index][0];
            int next_y = head[1] + direction[direction_index][1];

            // 벽에 부딪히거나 몸에 부딪히면 종료
            if (next_x < 0 || next_x >= N || next_y < 0 || next_y >= N || map[next_x][next_y] == 2) {
//                System.out.println("next_x = " + next_x + ", next_y = " + next_y);
//                System.out.println("second = " + second);
                second += 1;
                break;
            }

            // 사과가 없으면 꼬리 빼기
            if (map[next_x][next_y] != 1) {
                int[] del = q.pollLast();
                map[del[0]][del[1]] = 0;
            }

            // 머리 넣기
            q.offerFirst(new int[]{next_x, next_y});
            map[next_x][next_y] = 2;
//            System.out.println("next_x = " + next_x + ", next_y = " + next_y);

            second += 1;
        }

        System.out.println(second);




    }


}