// 단어 뒤집기
import java.util.*;

public class 백준9093 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String sentence = new String();
		StringBuffer sb;
		int T = sc.nextInt();
		sc.nextLine();
		
		for (int i=0; i<T; i++) {
			sentence = sc.nextLine();
			String[] strArray = sentence.split(" ");
			for (int j=0; j<strArray.length; j++) {
				sb = new StringBuffer(strArray[j]);
				System.out.print(sb.reverse() + " ");
			}
		}
		
		sc.close();
	}
}