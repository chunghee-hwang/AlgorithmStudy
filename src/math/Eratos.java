package math;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
// https://ko.wikipedia.org/wiki/%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98_%EC%B2%B4
public class Eratos {
    public static void main(String[] args) throws IOException {
        boolean[] primes;
        // 사용자로부터의 콘솔 입력
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        primes = new boolean[n+1]; // n+1만큼 할당
        // n <= 1 일 때 종료
        if(n <= 1) return;

        // 2~ n 까지 소수로 설정
        for(int i=2; i<=n; i++ )
            primes[i] = true;

        // 2 부터  ~ i*i <= n
        // 각각의 배수들을 지워간다.
        for(int i=2; (i*i)<=n; i++){
            if(primes[i])
                for(int j = i*i; j<=n;j+=i)
                    primes[j] = false;
        }
        StringBuilder sb = new StringBuilder();
        sb.append("{");
        for(int i=0; i<=n; i++){
            if(primes[i]){
                sb.append(i);
                sb.append(", ");
            }
        }
        sb.setCharAt(sb.length()-2, '}');
        System.out.println(sb.toString());
    }
}