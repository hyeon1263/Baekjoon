// 크로아티아 알파벳
import java.util.*;

public class 백준2941 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int cnt = 0;
		String input = sc.next();
		
		for (int i=0; i<input.length(); i++) {
			if ((i<input.length()-1)&&(input.charAt(i)=='c')) {
				if (input.charAt(i+1)=='=')
					i++;
				else if (input.charAt(i+1)=='-')
					i++;
			}
			else if ((i<input.length()-1)&&(input.charAt(i)=='d')) {
				if ((i<input.length()-2)&&(input.charAt(i+1)=='z')) {
					if (input.charAt(i+2)=='=')
						i+=2;
				}
				else if (input.charAt(i+1)=='-')
					i++;
			}
			else if ((i<input.length()-1)&&((input.charAt(i)=='l')||(input.charAt(i)=='n'))) {
				if (input.charAt(i+1)=='j')
					i++;
			}
			else if ((i<input.length()-1)&&((input.charAt(i)=='s')||(input.charAt(i)=='z'))) {
				if (input.charAt(i+1)=='=')
					i++;
			}
			cnt++;
		}
		
		System.out.println(cnt);
		
		sc.close();
	}
}